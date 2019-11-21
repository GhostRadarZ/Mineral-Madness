import pygame, os, cfg, hitbox, particle

#
# Base entity structure
# Characters will inherit from this class
# 

class Character(pygame.sprite.Sprite):
    def __init__(self, lives, spawnpos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Path for the sprites of the entity
        self.sprites = os.path.join(cfg.chranim_dir, self.__class__.__name__)

        # Path for the sound effects of the entity
        self.sfx = os.path.join(cfg.chrsfx_dir, self.__class__.__name__)

        # Create the list of frames for the character's idle animation
        self.anim_idle = []

        # Create a flipped version of the character's idle animation
        self.anim_idle_west = []

        # Create the list of frames for the character's hurt animation
        self.anim_hurt = []

        # Create a flipped version of the character's hurt animation
        self.anim_hurt_west = []

        # Create the list of frames for the character's walking animation
        self.anim_walk = []

        # Create a flipped version of the character's walking animation
        self.anim_walk_west = []

        # Create the list of frames for the character's jumping animation
        self.anim_jump = []

        # Create a flipped version of the character's jumping animation
        self.anim_jump_west = []

        # Create the list of frames for the character's falling animation
        self.anim_fall = []

        # Create a flipped version of the character's falling animation
        self.anim_fall_west = []

        # Create the list of frames for the character's grounded forward attack animation
        self.anim_atkforward = []

        # Create a flipped version of the character's grounded forward attack animation
        self.anim_atkforward_west = []

        # Create the list of frames for the character's grounded up attack animation
        self.anim_atkup = []

        # Create a flipped version of the character's grounded forward attack animation
        self.anim_atkup_west = []

        # Create the list of frames for the character's grounded down attack animation
        self.anim_atkdown = []
        
        # Create a flipped version of the character's grounded down attack animation
        self.anim_atkdown_west = []

        # Create the list of frames for the character's aerial forward attack animation
        self.anim_aerialforward = []

        # Create a flipped version of the character's aerial forward attack animation
        self.anim_aerialforward_west = []

        # Create the list of frames for the character's aerial up attack animation
        self.anim_aerialup = []

        # Create a flipped version of the character's aerial up attack animation
        self.anim_aerialup_west = []

        # Create the list of frames for the character's aerial down attack animation
        self.anim_aerialdown = []

        # Create a flipped version of the character's aerial down attack animation
        self.anim_aerialdown_west = []

        # Create the list of frames for the character's projectile animation
        self.anim_projectile = []

        # Create a flipped version of the character's projectile animation
        self.anim_projectile_west = []

        # Iterate over the files in this character's sprite directory
        for file in sorted(os.listdir(self.sprites)):

            # Store the full path of the current file
            filepath = os.path.join(self.sprites, file)

            if file.endswith('.png'):
                # Upscale the animation frame by a factor of 4
                frame = pygame.image.load(filepath).convert_alpha()
                frame_width = pygame.Surface.get_width(frame)
                frame_height = pygame.Surface.get_height(frame)
                frame_scaled = pygame.transform.scale(frame, (frame_width * 4, frame_height * 4))
                frame_flipped = pygame.transform.flip(frame_scaled, True, False)

            # If it's an idle animation frame, add it to it's frame list
            if file.startswith('idle') and file.endswith('.png'):
                self.anim_idle.append(frame_scaled)
                self.anim_idle_west.append(frame_flipped)
            
            # If it's a hurt animation frame, add it to it's frame list
            elif file.startswith('hurt') and file.endswith('.png'):
                self.anim_hurt.append(frame_scaled)
                self.anim_hurt_west.append(frame_flipped)

            # If it's a walking animation frame, add it to it's frame list
            elif file.startswith('walk') and file.endswith('.png'):
                self.anim_walk.append(frame_scaled)
                self.anim_walk_west.append(frame_flipped)

            # If it's a jumping animation frame, add it to it's frame list
            elif file.startswith('jump') and file.endswith('.png'):
                self.anim_jump.append(frame_scaled)
                self.anim_jump_west.append(frame_flipped)
            
            # If it's a falling animation frame, add it to it's frame list
            elif file.startswith('fall') and file.endswith('.png'):
                self.anim_fall.append(frame_scaled)
                self.anim_fall_west.append(frame_flipped)
            
            # If it's a grounded forward attack animation frame, add it to it's list
            elif file.startswith('atkforward') and file.endswith('.png'):
                self.anim_atkforward.append(frame_scaled)
                self.anim_atkforward_west.append(frame_flipped)
            
            # If it's a grounded up attack animation frame, add it to it's list
            elif file.startswith('atkup') and file.endswith('.png'):
                self.anim_atkup.append(frame_scaled)
                self.anim_atkup_west.append(frame_flipped)
            
            # If it's a grounded down attack animation frame, add it to it's list
            elif file.startswith('atkdown') and file.endswith('.png'):
                self.anim_atkdown.append(frame_scaled)
                self.anim_atkdown_west.append(frame_flipped)
            
            # If it's an aerial forward attack animation frame, add it to it's list
            elif file.startswith('aerialforward') and file.endswith('.png'):
                self.anim_aerialforward.append(frame_scaled)
                self.anim_aerialforward_west.append(frame_flipped)
            
            # If it's an aerial up attack animation frame, add it to it's list
            elif file.startswith('aerialup') and file.endswith('.png'):
                self.anim_aerialup.append(frame_scaled)
                self.anim_aerialup_west.append(frame_flipped)
            
            # If it's an aerial down attack animation frame, add it to it's list
            elif file.startswith('aerialdown') and file.endswith('.png'):
                self.anim_aerialdown.append(frame_scaled)
                self.anim_aerialdown_west.append(frame_flipped)
            
            if file.startswith('projectile') and file.endswith('.png'):
                self.anim_projectile.append(frame_scaled)
                self.anim_projectile_west.append(frame_flipped)

        # Set the character's idle image
        self.image = self.anim_idle[0]

        # Set the character's default animation
        self.animation = self.anim_idle

        # Iterate over the files in this character's sound effects directory
        for file in os.listdir(self.sfx):

            # Store the full path of the current file
            filepath = os.path.join(self.sfx, file)
            
            # If it's a hurt sound effect file, use it as the sound effect for that action
            if file.startswith('hurt') and file.endswith('.ogg'):
                self.sfx_hurt = pygame.mixer.Sound(filepath)

            # If it's a jump sound effect file, use it as the sound effect for that action
            elif file.startswith('jump') and file.endswith('.ogg'):
                self.sfx_jump = pygame.mixer.Sound(filepath)
            
            # If it's a grounded forward attack sound effect file, use it as the sound effect for that action
            elif file.startswith('atkforward') and file.endswith('.ogg'):
                self.sfx_atkforward = pygame.mixer.Sound(filepath)
            
            # If it's a grounded up attack sound effect file, use it as the sound effect for that action
            elif file.startswith('atkup') and file.endswith('.ogg'):
                self.sfx_atkup = pygame.mixer.Sound(filepath)
            
            # If it's a grounded down attack sound effect file, use it as the sound effect for that action
            elif file.startswith('atkdown') and file.endswith('.ogg'):
                self.sfx_atkdown = pygame.mixer.Sound(filepath)
            
            # If it's an aerial forward attack sound effect file, use it as the sound effect for that action
            elif file.startswith('aerialforward') and file.endswith('.ogg'):
                self.sfx_aerialforward = pygame.mixer.Sound(filepath)
            
            # If it's an aerial up attack sound effect file, use it as the sound effect for that action
            elif file.startswith('aerialup') and file.endswith('.ogg'):
                self.sfx_aerialup = pygame.mixer.Sound(filepath)
            
            # If it's an aerial down attack sound effect file, use it as the sound effect for that action
            elif file.startswith('aerialdown') and file.endswith('.ogg'):
                self.sfx_aerialdown = pygame.mixer.Sound(filepath)
        
        # Iterate over the files in the misc sound effects directory
        for file in os.listdir(cfg.miscsfx_dir):

            # Store the full path of the current file
            filepath = os.path.join(cfg.miscsfx_dir, file)

            if file.startswith('death') and file.endswith('.ogg'):
                self.sfx_death = pygame.mixer.Sound(filepath)
        
        # Spawn points of the entity for when they die
        self.spawnpos = spawnpos

        self.x = self.spawnpos[0]
        self.y = self.spawnpos[1]

        # Make entities face east by default
        self.facing = 'East'

        # Entities are on the ground by default
        self.airbourne = False

        # Default base entity speeds
        self.x_base = 10
        self.y_base = 15

        # Default entity velocity
        self.x_vel = 0
        self.y_vel = 0

        # Default entity gravity
        self.gravity = 1

        # Frame counter for animations
        self.framecount = 0

        # Frame delay for animations (update the image after ? frames)
        self.framebuffer = 4

        # Index of the current frame of an animation
        self.frame = 0

        # Number of Lives for the entity
        self.lives = lives

        # Number of frames that the entity is intangible for
        self.invincibility = 0

        # Default fast fall speed
        self.y_base_fast = 20

        # Entities are not on attacking by default
        self.attacking = False
        
        # List of the entity's hitboxes that can damage other entities
        self.active_attacks = []

        # List of hitboxes that the entity can get damaged by
        self.enemy_attacks = []

        # List of on-screen particles
        self.active_particles = []
        
        # Number of frames where the character is in a hitstunned state
        self.hitstun = 0
        
        # Flag that determines if an attack input has already been processed
        self.attacked = True

        # Default number of multi-jumps (self.jumps stays static)
        self.jumps = 2
        self.jumpcounter = self.jumps

        # Flag that determines if the jump input has already been processed
        self.jumped = False

        # How much damage the entity has taken     
        self.damage = 0

        self.inputs = [False, False, False, False, False, False, False, False]

        # Create a rect for stage collision and attack collision
        self.hurtbox = pygame.Rect(self.x, self.y, 0, 0)

        # Create a rect for displaying animations
        self.rect = pygame.Rect(self.x, self.y, 0, 0)
        
    def update(self, camera, stage, entities):
        self.enemy_attacks = []
        # Store the camera offsets
        self.x_offset = camera.x_offset
        self.y_offset = camera.y_offset

        self.stage_hitboxes = stage
        
        for entity in entities:
            if entity is not self:
                for hitboxes in entity.active_attacks:
                    self.enemy_attacks.append(hitboxes)
        
        # Apply any physics to the entity
        self.applyPhysics()

        # Check for any collisions with any attack hitboxes
        self.checkHit() 

        # Update the x co-ordinates of the entity
        self.x += self.x_vel

        # Check for any platform collisions in the x-axis
        self.checkStageXCollision()

        # Update the y co-ordinates of the entity
        self.y += self.y_vel

        # Check for any platform collisions in the y-axis
        self.checkStageYCollision()

        # Decrement the hitstun counter every frame until it reaches 0
        if self.hitstun > 0:
            self.hitstun -= 1
        
        if self.invincibility > 0:
            self.invincibility -= 1

        # Change the character's animation depending on their current state
        self.changeAnimation()

        # Update the character's animation state
        self.updateAnimationFrame()

        # Update the character's active hitboxes
        self.updateHitboxes()

        # Update the x and y co-ordinates of the entity after processing modifications casued by collision and animation changes
        self.x = self.hurtbox.x + self.x_offset
        self.y = self.hurtbox.y + self.y_offset

        if self.x + self.hurtbox.width > 1500 or self.x < -700 or self.y + self.hurtbox.height > 1300 or self.y < -300:
            self.active_particles.append(particle.Blast(self))
            self.sfx_death.play()
            self.x = self.spawnpos[0] - self.hurtbox.width / 2
            self.y = self.spawnpos[1] - self.hurtbox.height
            self.invincibility = 60
            self.x_vel = 0
            self.y_vel = 0
            self.hitstun = 0
            self.damage = 0
            self.lives -= 1
        
        # Update the character's active particles
        self.updateParticles()
    
    def parseInputs(self, inputs):
        # Store the inputs that were passed to the entity
        self.inputs = inputs

        # The entity will not be able to attack again until all attack keys are released
        # If they press up attack, then do an up attack
        if self.inputs[4] and not self.attacked and not self.attacking and self.hitstun == 0:
            self.upAttack()
            self.attacked = True
        elif self.inputs[4] and self.attacked:
            pass

        # If they press down attack, then do a down attack
        elif self.inputs[5] and not self.attacked and not self.attacking and self.hitstun == 0:
            self.downAttack()
            self.attacked = True
        elif self.inputs[5] and self.attacked:
            pass

        # If they press left attack, then do a left attack
        elif self.inputs[6] and not self.attacked and not self.attacking and self.hitstun == 0:
            self.facing = 'West'
            self.forwardAttack()
            self.attacked = True
        elif self.inputs[6] and self.attacked:
            pass

        # If they press right attack, then do a right attack
        elif self.inputs[7] and not self.attacked and not self.attacking and self.hitstun == 0:
            self.facing = 'East'
            self.forwardAttack()
            self.attacked = True
        elif self.inputs[7] and self.attacked:
            pass
        
        # If they press neutral attack, then do a forward attack with the character's current facing direction
        elif self.inputs[8] and not self.attacked and not self.attacking and self.hitstun == 0:
            self.forwardAttack()
            self.attacked = True
        elif self.inputs[8] and self.attacked:
            pass

        else:
            self.attacked = False

        # If they press up, then make them jump. They won't be able to jump again until they release the key
        if self.inputs[0] and not self.jumped and self.hitstun == 0:
            self.jumpUp()
            self.jumped = True
        elif self.inputs[0] and self.jumped:
            pass
        else:
            self.jumped = False
        
        # If they press down, then do a fast fall
        if self.inputs[1] and self.hitstun == 0:
            self.fallFast()

        # If they press left, then move left
        if self.inputs[2] and self.hitstun == 0:
            self.moveLeft()
        
        # If they press right, then move right
        if self.inputs[3] and self.hitstun == 0:
            self.moveRight()
        
        # If neither right or left is being pressed, then stop moving the entity
        if not self.inputs[2] and not self.inputs[3] or self.hitstun != 0:
            self.stopMoving()

    def changeAnimation(self):
        # If the character is attacking, then only check to see if the animation has ended
        if self.attacking:        
            pass

        # If the character is hurt, play the hurt animation
        elif self.hitstun > 0 and self.facing == 'East':
            self.animation = self.anim_hurt
        elif self.hitstun > 0 and self.facing == 'West':
            self.animation = self.anim_hurt_west

        # If the character is jumping, play the jumping animation
        elif self.airbourne and self.facing == 'East' and self.y_vel < 0:
            self.animation = self.anim_jump
        elif self.airbourne and self.facing == 'West' and self.y_vel < 0:
            self.animation = self.anim_jump_west
        
        # If the character is falling, play the falling animation
        elif self.airbourne and self.facing == 'East' and self.y_vel >= 0:
            self.animation = self.anim_fall
        elif self.airbourne and self.facing == 'West' and self.y_vel >= 0:
            self.animation = self.anim_fall_west

        # If the character is grounded and moving, play the walking animation
        elif not self.airbourne and self.facing == 'East' and self.x_vel > 0:
            self.animation = self.anim_walk
        elif not self.airbourne and self.facing == 'West' and self.x_vel < 0:
            self.animation = self.anim_walk_west

        # Otherwise, play their idle animation
        elif self.facing == 'East':
            self.animation = self.anim_idle
        elif self.facing == 'West':
            self.animation = self.anim_idle_west

    def updateAnimationFrame(self):
        # Increment the frame count
        self.framecount += 1

        # Once the frame delay is over, update the entity's animation
        if self.framecount == self.framebuffer:
            # Reset the frame counter
            self.framecount = 0

            # Update the frame index
            self.frame += 1

            if self.frame == len(self.animation):
                self.attacking = False
                self.changeAnimation()

            # Display the new animation frame
            self.image = self.animation[self.frame % len(self.animation)]

        # Update the length and width of the image rect in case it changes
        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)
        
        # Update the position of the image rect
        self.rect.center = self.hurtbox.center
    
    def updateHitboxes(self):
        for attack in self.active_attacks:
            attack.update(self)

            if attack.active == False:
                self.active_attacks.remove(attack)
    
    def updateParticles(self):
        for particle in self.active_particles:
            particle.update(self)

            if particle.active == False:
                self.active_particles.remove(particle)

    def applyPhysics(self):
        if self.airbourne:
            # If they're fast-falling, don't do anything to their falling speed
            if self.y_vel == self.y_base_fast:
                pass

            # Otherwise, if their falling is speed is faster than the base value, then set their falling speed to the base value
            elif self.y_vel >= self.y_base and self.hitstun == 0:
                self.y_vel = self.y_base

            # Otherwise, apply gravity to their falling speed
            else:
                self.y_vel += self.gravity
            
            # If they're moving faster than their max speed horizontally, then gradually decrease their speed
            if self.x_vel > self.x_base and self.hitstun == 0:
                self.x_vel -= 2
            elif self.x_vel < self.x_base * -1 and self.hitstun == 0:
                self.x_vel += 2
        
    def checkStageXCollision(self):
        # Update the co-ordinates of the hurtbox before testing for collision
        self.hurtbox.x = self.x - self.x_offset
        self.hurtbox.y = self.y - self.y_offset

        for element in self.stage_hitboxes:
            if element.__class__.__name__ == 'Platform':
                # Test for collision with a platform in the stage
                colliding = self.hurtbox.colliderect(element.rect)

                if colliding and not element.transparent:
                    # Push the character out if they're moving forward into a platform
                    if self.x_vel > 0:
                        self.x_vel = 0
                        self.hurtbox.right = element.rect.left

                    # Push the character out if they're moving backward into a platform
                    if self.x_vel < 0:
                        self.x_vel = 0
                        self.hurtbox.left = element.rect.right
    
    def checkStageYCollision(self):
        # Update the y co-ordinate of the hurtbox before testing for collision
        self.hurtbox.y = self.y - self.y_offset

        # Assume the character is airbourne before testing for any collision
        self.airbourne = True

        for element in self.stage_hitboxes:
            if element.__class__.__name__ == 'Platform':
                self.hurtbox.height += 1

                # Test for collision with a platform in the stage
                colliding = self.hurtbox.colliderect(element.rect)

                self.hurtbox.height -= 1

                if element.transparent:
                    # Put the entity in a grounded state if they are falling or standing on the ground
                    if colliding and self.y_vel >= 0 and self.hurtbox.centery < element.rect.centery and not self.inputs[1]:
                        self.airbourne = False
                        self.y_vel = 0
                        self.jumpcounter = self.jumps
                        self.hurtbox.bottom = element.rect.top

                elif not element.transparent:
                    # Put the entity in a grounded state if they are falling or standing on the ground
                    if colliding and self.y_vel >= 0:
                        self.airbourne = False
                        self.y_vel = 0
                        self.jumpcounter = self.jumps
                        self.hurtbox.bottom = element.rect.top
                    
                    # Stop the character from jumping if they hit a ceiling
                    if colliding and self.y_vel < 0:
                        self.y_vel = 0
                        self.hurtbox.top = element.rect.bottom

    def checkHit(self):
        for enemy_attack in self.enemy_attacks:
            for hitbox in enemy_attack.active_hitboxes:
                # Test for collision with harmful hitboxes
                colliding = self.hurtbox.colliderect(hitbox.rect)

                if colliding and self.invincibility == 0:
                    # Calculate the amount of knockback in the x-direction
                    self.x_vel = hitbox.power_x * (self.damage + 100) / 50

                    # Calculate the amount of knockback in the y-direction
                    self.y_vel = hitbox.power_y * -1 * (self.damage + 100) / 50

                    # Put the character in a hitstunned state for a number of frames
                    self.hitstun = hitbox.hitstun

                    # Apply damage to the entity
                    self.damage += hitbox.damage

                    # If the enemy's hitbox was a projectile, then disable the hitbox
                    if hitbox.__class__.__name__ == 'Projectile':
                        enemy_attack.active_hitboxes.remove(hitbox)
                        enemy_attack.lingering.remove(hitbox)
                    
                    # Grant the character 15 frames of invincibility if they get hit by a melee attack
                    else:
                        self.invincibility = 15

                    for self_attack in self.active_attacks:
                        # Disable any currently active melee hitboxes
                        for hitbox in self_attack.active_hitboxes:
                            if hitbox.__class__.__name__ == 'Melee':
                                self_attack.active_hitboxes.remove(hitbox)
                        
                        # Prevent further hitboxes from loading
                        self_attack.attackdata = []
                    
                    # Set them into a non-attacking state
                    self.attacking = False

                    # Play the character's hurt sound effect
                    if cfg.sound:
                        self.sfx_hurt.play()
                    
    def jumpUp(self):
        # Jump only if the user has 1 or more jumps available, and isn't attacking. Decrease the jump counter if successful
        if self.jumpcounter > 0 and not self.attacking:
            self.y_vel = self.y_base * -1
            self.jumpcounter -= 1

            if cfg.sound:
                self.sfx_jump.play()
    
    def fallFast(self):
        # If the user is falling, then increase their falling speed
        if self.airbourne and self.y_vel >= 0:
            self.y_vel = self.y_base_fast
    
    def moveRight(self):
        # If the character is grounded and not attacking, change their facing direction and start moving instantly
        if not self.airbourne and not self.attacking:
            self.facing = 'East'
            self.x_vel = self.x_base
        
        elif not self.airbourne and self.attacking:
            self.x_vel = 0
        
        # If the character is airbourne, and isn't at peak speed, increase their speed gradually
        elif self.x_vel < self.x_base:
            self.x_vel += 2

    def moveLeft(self):
        # If the character is grounded and not attacking, change their facing direction and start moving instantly
        if not self.airbourne and not self.attacking:
            self.facing = 'West'
            self.x_vel = self.x_base * -1
        
        # Stop the character from moving if they are doing a grounded attack
        elif not self.airbourne and self.attacking:
            self.x_vel = 0
        
        # If the character is airbourne, and isn't at peak speed, increase their speed gradually
        elif self.x_vel > self.x_base * -1:
            self.x_vel -= 2
                
    def stopMoving(self):
        # If the character is grounded, stop moving instantly
        if not self.airbourne:
            self.x_vel = 0

        # If the character is airbourne, stop moving gradually
        elif self.airbourne and self.x_vel < 0 and self.hitstun == 0:
            self.x_vel += 1
        elif self.airbourne and self.x_vel > 0 and self.hitstun == 0:
            self.x_vel -= 1

    def forwardAttack(self):
        # Indicate that this entity is currently attacking
        self.attacking = True

        # Perform a grounded forward attack
        if not self.airbourne:
            self.active_attacks.append(hitbox.Attack(self.atkforward_attack, self))

            if cfg.sound:
                self.sfx_atkforward.play()

            if self.facing == 'East':
                # Use the east-facing version of the grounded forward attack animation
                self.animation = self.anim_atkforward

            else:            
                # Use the west-facing version of the grounded forward attack animation
                self.animation = self.anim_atkforward_west
        
        # Perform a forward aerial attack
        else:
            # Add the forward aerial to the list of active hitboxes
            self.active_attacks.append(hitbox.Attack(self.aerialforward_attack, self))

            if cfg.sound:
                self.sfx_aerialforward.play()

            if self.facing == 'East':
                # Use the east-facing version of the forward aerial attack animation
                self.animation = self.anim_aerialforward

            else:
                # Use the west-facing version of the forward aerial attack animation
                self.animation = self.anim_aerialforward_west
        
        # Force the attack animation to start immediately
        self.frame = 0
        self.framecount = 0
        self.image = self.animation[0]
            
    def upAttack(self):
        # Indicate that this entity is currently attacking
        self.attacking = True

        # Perform a grounded up attack
        if not self.airbourne:
            # Add the grounded up attack to the list of active hitboxes
            self.active_attacks.append(hitbox.Attack(self.atkup_attack, self))

            if cfg.sound:
                self.sfx_atkup.play()

            if self.facing == 'East':
                # Use the east-facing version of the grounded up attack animation
                self.animation = self.anim_atkup

            else:
                # Use the west-facing version of the grounded up attack animation
                self.animation = self.anim_atkup_west
        
        # Perform an up aerial attack
        else:
            # Add the aerial up attack to the list of active hitboxes
            self.active_attacks.append(hitbox.Attack(self.aerialup_attack, self))

            if cfg.sound:
                self.sfx_aerialup.play()

            if self.facing == 'East':
                # Use the east-facing version of the up aerial attack animation
                self.animation = self.anim_aerialup

            else:
                # Use the west-facing version of the up aerial attack animation
                self.animation = self.anim_aerialup_west
        
        # Force the attack animation to start immediately
        self.frame = 0
        self.framecount = 0
        self.image = self.animation[0]

    def downAttack(self):
        # Indicate that this entity is currently attacking
        self.attacking = True

        if not self.airbourne:
            # Add the grounded down attack to the list of active hitboxes
            self.active_attacks.append(hitbox.Attack(self.atkdown_attack, self))

            if cfg.sound:
                self.sfx_atkdown.play()

            if self.facing == 'East':
                # Use the east-facing version of the grounded down attack animation
                self.animation = self.anim_atkdown

            else:
                # Use the west-facing version of the grounded down attack animation
                self.animation = self.anim_atkdown_west
            
        else:
            # Add the aerial down attack to the list of active hitboxes
            self.active_attacks.append(hitbox.Attack(self.aerialdown_attack, self))

            if cfg.sound:
                self.sfx_aerialdown.play()

            if self.facing == 'East':
                # Use the east-facing verison of the down aerial attack animation
                self.animation = self.anim_aerialdown

            else:
                # Use the west-facing version of the down aerial attack animation
                self.animation = self.anim_aerialdown_west
        
        # Force the attack animation to start immediately
        self.frame = 0
        self.framecount = 0
        self.image = self.animation[0]
