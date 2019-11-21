# Author: Aaron Castellino
# Date: 21/9/2018
# File Name: main.py
# Description: This file is the hub file for Mineral Maddness and will launch the game when run

#import important libraries
import pygame

# Manually setup pygame's audio sample rates to reduce audio delay
pygame.mixer.pre_init(44100, -16, 2, 1024)

# set up pygame before importing global game config
pygame.init()

import os, sys, cfg, menu, fight

pygame.display.set_caption('Mineral Madness')
icon = pygame.image.load(os.path.join(cfg.menu_dir, 'logo.png')).convert_alpha()
pygame.display.set_icon(icon)

# Create the list of frames for the intro video
frames = []

# Iterate over the files in the Video directory
for f in sorted(os.listdir(cfg.video_dir)):

    # Store the full path of the current file
    path = os.path.join(cfg.video_dir, f)

    # If the file is a jpg, load it as a video frame
    if f.endswith('.jpg'):
        frames.append(pygame.image.load(path))

    # If the file is an ogg, load it as the video's audio
    if f.endswith('.ogg'):
        pygame.mixer.music.load(path)

# Play the video audio
pygame.mixer.music.play()

# Iterate over the list of frames in the video
for f in frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if user quits close program
            pygame.quit()
            sys.exit()

    # Blit the current frame of the video to the screen
    cfg.window.blit(f, (0, 0))

    # Update the display at 30 fps
    pygame.display.flip()
    cfg.clock.tick(30)

#  default game settings
settings = [
    5, # Lives
    [0, 0], # Characters
    ['Human', 'Bot'], # Player Types
    [0, 1], # Bot Difficulties
    1, # Stage
]

#First Screen Loaded into
mode = "Start Menu"

#load and play music
pygame.mixer.music.load(os.path.join(cfg.music_dir, 'mainmenu.ogg'))
pygame.mixer.music.play(-1,0)

mode = menu.MainMenu(settings) # Runs Main Menu Screen

#each function runs its own screen and outputs the screen it wants to go to
while True: # Runs Game Loop
    if mode == "Character": # Character Select Screen
        mode , settings = menu.CharacterSelect(settings) 
    elif mode == "Game": # Actual Game Screen
        mode , settings , loser = fight.fightLoop(settings)
    elif mode == "Results": # Help Menu Screen
        mode = menu.VictoryScreen(settings, loser)
    elif mode == "Stage": # Help Menu Screen
        mode , settings  = menu.StageMenu(settings) # Runs Main Menu Screen
    elif mode == "Mode Menu": # Mode Select Screen
        mode , settings = menu.ModeMenu(settings) # Runs Mode Screen
    else: #Start Screen
        mode = menu.MainMenu(settings) # Runs Main Menu Screen

