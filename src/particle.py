import os, pygame, cfg, assets

class Particle(object):
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.x_vel = data[2]
        self.y_vel = data[3]
        self.gravity = data[4]
        self.x_base = self.x_vel
        self.y_base = self.y_vel
        self.airbourne = True
        self.framecount = 0
        self.frame = 0
        self.framebuffer = 4

    def update(self, character):
        # Store the camera offsets
        self.x_offset = character.x_offset
        self.y_offset = character.y_offset

        self.stage_hitboxes = character.stage_hitboxes

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

            if self.frame == len(self.animation):
                self.active = False
            
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

class Blast(Particle):
    def __init__(self, character):
        data = [0, 0, 0, 0, 0]
        super(Blast, self).__init__(data)

        self.active = True

        self.animation = assets.part_blast

        self.image = self.animation[0]

        self.rect = pygame.Rect(0, 0, 0, 0)

        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)
            
        self.x = character.x + character.hurtbox.width / 2 - self.rect.width / 2
        self.y = character.y + character.hurtbox.height / 2 - self.rect.height / 2

    # Blast particle should ignore stage collision
    def checkStageCollision(self):
        # Update the co-ordinates of the hurtbox before testing for collision
        self.rect.x = self.x - self.x_offset
        self.rect.y = self.y - self.y_offset
