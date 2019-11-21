import pygame, os

# Window Dimensions
width = 1280
height = 720

# Main window surface that will be drawn to
window = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.FULLSCREEN)
#window = pygame.display.set_mode((width, height), pygame.HWSURFACE )


# Flag that determines if sounds should be played
sound = True

# Main clock that will be used to track time and limit framerate
clock = pygame.time.Clock()

# Folder path for fonts
font_dir = os.path.join(os.path.dirname(__file__), 'Font')

# Folder path for in-game music
music_dir = os.path.join(os.path.dirname(__file__), 'Music')

# Folder path for character sound effects
sfx_dir = os.path.join(os.path.dirname(__file__), 'SFX')

# Folder path for sprite images
sprite_dir = os.path.join(os.path.dirname(__file__), 'Sprites')

# Folder path for the video frames
video_dir = os.path.join(os.path.dirname(__file__), 'Video')

# Folder path for character sound effects
chrsfx_dir = os.path.join(sfx_dir, 'Entity')

# Folder path for voice lines
voice_dir = os.path.join(sfx_dir, 'Voice')

# Folder path for miscellaneous sound effects
miscsfx_dir = os.path.join(sfx_dir, 'Misc')

# Folder path for character animations
chranim_dir = os.path.join(sprite_dir, 'Entity')

# Folder path for in-game world environment images
env_dir = os.path.join(sprite_dir, 'World')

# Folder path for in-game HUD
hud_dir = os.path.join(sprite_dir, 'UI')

# Folder path for the menu images
menu_dir = os.path.join(sprite_dir, 'Menu')

# Folder path for particle images
particle_dir = os.path.join(sprite_dir, 'Particles')
