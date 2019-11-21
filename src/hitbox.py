import pygame, cfg

class Attack(object):
    def __init__(self, framedata, character):
        self.attackdata = []
        self.active_hitboxes = []
        self.lingering = []
        self.active = True

        self.frame = 0
        self.framebuffer = 4
        self.framecounter = 0

        # Iterate through the frame data of the character's attack
        for frame in range(0, len(framedata)):
            
            # Create a new frame of data
            self.attackdata.append([])

            # Iterate through the hitboxes in the current frame
            for hitbox in framedata[frame]:
                try:
                    # Build the hitbox object
                    self.attackdata[frame].append(hitbox[0](hitbox[1]))
                
                except AttributeError:
                    # If there is no hitbox to build, then pass
                    pass
                
                except IndexError:
                    # If there is no hitbox to build, then pass
                    pass

    def update(self, character):
        self.framecounter += 1

        if self.framecounter == self.framebuffer:
            self.framecounter = 0
            self.frame += 1

            self.active_hitboxes = []

            for hitbox in self.lingering:
                self.active_hitboxes.append(hitbox)

            try:
                for hitbox in self.attackdata[self.frame]:
                    hitbox.activate(character)
                    self.active_hitboxes.append(hitbox)

                    if hitbox.__class__.__name__ == 'Projectile':
                        self.lingering.append(hitbox)
            
            except AttributeError:
                pass
            
            except IndexError:
                if len(self.active_hitboxes) == 0:
                    self.active = False

        for hitbox in self.active_hitboxes:
            hitbox.update(character)

            if hitbox.__class__.__name__ == 'Projectile' and hitbox.active == False:
                self.active_hitboxes.remove(hitbox)
                self.lingering.remove(hitbox)


#
# Base hitbox structure
#

class Hitbox(object):
    def __init__(self, power_x, power_y, damage, hitstun):
        # Amount of knockback the hitbox deals in the x-direction
        self.power_x = power_x

        # Amount of knockback the hitbox deals in the y-direction
        self.power_y = power_y

        # Amount of damage the hitbox deals to an entity
        self.damage = damage

        # Number of frames that the entity will be in the hitstunned state
        self.hitstun = hitstun

#
# Hitbox Types
#

class Melee(Hitbox):
    def __init__(self, data):
        super(Melee, self).__init__(data[1], data[2], data[3], data[4])
        self.rect = data[0].copy()
        self.x_offset = self.rect.x
        self.y_offset = self.rect.y
    
    def activate(self, character):
        # Update the x co-ordinates of the hitbox if the character moves
        if character.facing == 'East':
            self.rect.left = character.hurtbox.centerx + self.x_offset
        else:
            self.rect.right = character.hurtbox.centerx + self.x_offset * -1
            self.power_x *= -1
        
        # Update the y co-ordinates of the hitbox if the character moves
        self.rect.top = character.hurtbox.top + self.y_offset
    
    def update(self, character):
        # Update the x co-ordinates of the hitbox if the character moves
        if character.facing == 'East':
            self.rect.left = character.hurtbox.centerx + self.x_offset
        else:
            self.rect.right = character.hurtbox.centerx + self.x_offset * -1
        
        # Update the y co-ordinates of the hitbox if the character moves
        self.rect.top = character.hurtbox.top + self.y_offset

class Projectile(Hitbox):
    def __init__(self, data):
        super(Projectile, self).__init__(data[5], data[6], data[7], data[8])
        self.x_spawn_offset = data[0]
        self.y_spawn_offset = data[1]
        self.x_vel = data[2]
        self.y_vel = data[3]
        self.gravity = data[4]
        self.x_base = self.x_vel
        self.y_base = self.y_vel
        self.airbourne = True
        self.framecount = 0
        self.frame = 0
        self.framebuffer = 4

        self.time = 120

    def activate(self, character):
        self.active = True

        if character.facing == 'East':
            self.animation = character.anim_projectile
            self.x = character.x + character.hurtbox.width / 2 + self.x_spawn_offset
        else:
            self.animation = character.anim_projectile_west
            self.x = character.x - character.hurtbox.width / 2 - self.x_spawn_offset
            self.power_x *= -1
            self.x_vel *= -1

        self.image = self.animation[0]

        self.x_offset = character.x_offset
        self.y_offset = character.y_offset

        self.y = character.y + self.y_spawn_offset

        self.rect = pygame.Rect(self.x - self.x_offset, self.y - self.y_offset, 0, 0)

        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)

    def update(self, character):
        # Store the camera offsets
        self.x_offset = character.x_offset
        self.y_offset = character.y_offset

        self.stage_hitboxes = character.stage_hitboxes

        self.time -= 1

        if self.time <= 0:
            self.active = False

        if self.airbourne:
            self.y_vel += self.gravity

        # Update the x co-ordinates of the entity
        self.x += self.x_vel

        # Update the y co-ordinates of the entity
        self.y += self.y_vel

        # Check for any platform collisions in the x-axis
        self.checkStageCollision()

        # Update the character's animation state
        self.updateAnimation()

        cfg.window.blit(self.image, (self.rect.x, self.rect.y))

    def updateAnimation(self):
        # Increment the frame count
        self.framecount += 1

        # Once the frame delay is over, update the entity's animation
        if self.framecount == self.framebuffer:
            # Reset the frame counter
            self.framecount = 0

            # Update the frame index
            self.frame += 1
            
            # Display the new animation frame
            self.image = self.animation[self.frame % len(self.animation)]

        # Update the length and width of the image rect in case it changes
        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)

    def checkStageCollision(self):
        # Update the co-ordinates of the hurtbox before testing for collision
        self.rect.x = self.x - self.x_offset
        self.rect.y = self.y - self.y_offset

        for element in self.stage_hitboxes:
            if element.__class__.__name__ == 'Platform':
                # Test for collision with a platform in the stage
                colliding = self.rect.colliderect(element.rect)

                if colliding:
                    self.active = False