import pygame, os, cfg

#
# Base environment element structure
# Environment elements will inherit from this class
#

class Environment(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load the image of the environment element
        self.image = image

        # Set the co-ordinates of the environment element
        self.x = x
        self.y = y

        # Create a rect of the environment element
        self.rect = pygame.Rect(self.x, self.y, 0, 0)

        # Get the width and height of the environment element
        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)

    def update(self, camera):
        # Apply camera offset to draw to the screen
        self.rect.x = self.x - camera.x_offset
        self.rect.y = self.y - camera.y_offset

#
# Environment planes
#

class Background(Environment):
    def __init__(self, image, x, y):
        # Inherit from the Environment class
        super(Background, self).__init__(image, x, y)

        # Upscale elements on the background plane by a factor of 3
        image_width = pygame.Surface.get_width(self.image)
        image_height = pygame.Surface.get_height(self.image)
        self.image = pygame.transform.scale(self.image, (image_width * 3, image_height * 3))

        # Set the rescaled width and height of the environment element
        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)

    def update(self, camera):
        # Apply camera offset to draw to the screen (parallaxed for the illusion of depth)
        # Simplified form of self.rect.x = self.x - (camera.x_offset - (400 - cfg.width / 2)) * 0.2 - (400 - cfg.width / 2)
        self.rect.x = self.x - 0.2 * camera.x_offset - 0.8 * (400 - cfg.width / 2)
        # Simplified form of self.rect.y = self.y - (camera.y_offset - (300 - cfg.height / 2)) * 0.2 - (300 - cfg.height / 2)
        self.rect.y = self.y - 0.2 * camera.y_offset - 0.8 * (300 - cfg.height / 2)

class Foreground(Environment):
    def __init__(self, image, x, y):
        # Inherit from the Environment class
        super(Foreground, self).__init__(image, x, y)

        # Upscale elements on the foreground plane by a factor of 4
        image_width = pygame.Surface.get_width(self.image)
        image_height = pygame.Surface.get_height(self.image)
        self.image = pygame.transform.scale(self.image, (image_width * 4, image_height * 4))

        # Set the rescaled width and height of the environment element
        self.rect.width = pygame.Surface.get_width(self.image)
        self.rect.height = pygame.Surface.get_height(self.image)

    def update(self, camera):
        # Apply camera offset to draw to the screen
        self.rect.x = self.x - camera.x_offset
        self.rect.y = self.y - camera.y_offset
        
#
# Foreground elements
#

class Platform(Foreground):
    def __init__(self, image, x, y, transparent = False):
        super(Platform, self).__init__(image, x, y)      
          
        # Determines if the player can jump through the platform or not (False by default)
        self.transparent = transparent

#
# Background elements
#

class Scenery(Background):
    def __init__(self, image):
        # Inherit from the Environment class
        super(Scenery, self).__init__(image, 0, 0)

        # Center the scenery image
        self.x = 400 - self.rect.width / 2
        self.y = 300 - self.rect.height / 2

#
# Camera
# Used to set offsets based on character positioning.
# Environment elements and entities use the generated offsets to draw theirselves to the screen in the proper position
#

class Camera(object):
    def __init__(self):
        # Set the initial co-ordinates for the camera (0, 0 by default)
        self.x_offset = 400 - cfg.width / 2
        self.y_offset = 300 - cfg.height / 2

        # Create variables that store the co-ordinates of the camera's desired position
        self.x_dest = 0
        self.y_dest = 0
    
    def updatePos(self, entities):
        # Set the baseline co-ordinates for comparison
        leftmost_x = entities[0].x + entities[0].hurtbox.width
        rightmost_x = entities[0].x + entities[0].hurtbox.width
        top_y = entities[0].y + entities[0].hurtbox.height
        bottom_y = entities[0].y + entities[0].hurtbox.height

        # Iterate over the list of on-screen entities
        for entity in entities:

            # If the current entity's x value is lower than the leftmost x value, then set it as the new leftmost x value
            if entity.x + entity.hurtbox.width / 2 < leftmost_x:
                leftmost_x = entity.x + entity.hurtbox.width / 2

            # If the current entity's x value is greater than the rightmost x value, then set it as the new rightmost x value
            elif entity.x + entity.hurtbox.width / 2 > rightmost_x:
                rightmost_x = entity.x + entity.hurtbox.width / 2
            
            # If the current entity's y value is less than the top y value, then set it as the new top y value
            if entity.y + entity.hurtbox.height / 2 < top_y:
                top_y = entity.y + entity.hurtbox.height
            
            # If the current entity's y value is greater than the bottom y value, then set it as the new bottom y value
            elif entity.y + entity.hurtbox.height / 2 > bottom_y:
                bottom_y = entity.y + entity.hurtbox.height

        # Calculate the camera's desired destination on the x and y axis (centered between the two furthest entities)
        self.x_dest = (leftmost_x + rightmost_x) / 2 - cfg.width / 2
        self.y_dest = (top_y + bottom_y) / 2 - cfg.height / 2

        # Calculate the velocity of the camera based on the difference between the camera's desired position and the camera's current position
        self.x_vel = (self.x_dest - self.x_offset) / 10
        self.y_vel = (self.y_dest - self.y_offset) / 10

        # Apply the velocity to calculate the camera's new position
        self.x_offset += int(self.x_vel)
        self.y_offset += int(self.y_vel)
        