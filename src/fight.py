import pygame, os, sys, random, interface, character, environment, player, menu, cfg, assets

def fightLoop(settings):
    # Store the match settings
    lives = settings[0]
    characters = settings[1]
    playertypes = settings[2]
    botdiffs = settings[3]
    stage = settings[4]

    return_to_title = False

    # Create a sprite group for the objects in the world environment
    # OrderedUpdates type to make sure everything updates and draws in the order they were appended to the group
    world = pygame.sprite.OrderedUpdates()

    if stage == 4:
        stage = random.randint(0, 3)

    if stage == 0:
        # Add the stage background as part of the world environment
        world.add(environment.Scenery(assets.srr_bg))

        # Add platforms as part of the world environment (has collision)
        world.add(environment.Platform(assets.srr_pl_s, 50, 700))
        world.add(environment.Platform(assets.srr_pl_t, 50, 500, True))
        world.add(environment.Platform(assets.srr_pl_t, 510, 500, True))

        spawnpoints = [(170, 500), (630, 500)]

        # Load the stage music
        pygame.mixer.music.load(os.path.join(cfg.music_dir, 'Green_Stage.mp3'))

    elif stage == 1:
        # Add the stage background as part of the world environment
        world.add(environment.Scenery(assets.cc_bg))

        # Add platforms as part of the world environment (has collision)
        world.add(environment.Platform(assets.cc_pl_s, 50, 700))
        world.add(environment.Platform(assets.cc_pl_s, 280, 700))
        world.add(environment.Platform(assets.cc_pl_s, 510, 700))
        world.add(environment.Platform(assets.cc_pl_t, 150, 500, True))

        spawnpoints = [(170, 700), (630, 700)]

        # Load the stage music
        pygame.mixer.music.load(os.path.join(cfg.music_dir, 'Crystal_stage.mp3'))

    elif stage == 2:
        # Add the stage background as part of the world environment
        world.add(environment.Scenery(assets.rv_bg))

        # Add platforms as part of the world environment (has collision)
        world.add(environment.Platform(assets.rv_pl_s, 50, 700))

        spawnpoints = [(150, 700), (650, 700)]

        # Load the stage music
        pygame.mixer.music.load(os.path.join(cfg.music_dir, 'Fire_Stage.mp3'))
    
    elif stage == 3:
        # Add the stage background as part of the world environment
        world.add(environment.Scenery(assets.at_bg))

        # Add platforms as part of the world environment (has collision)
        world.add(environment.Platform(assets.at_pl_s, 150, 700))
        world.add(environment.Platform(assets.at_pl_t, -50, 532, True))
        world.add(environment.Platform(assets.at_pl_t, 650, 532, True))

        spawnpoints = [(50, 532), (750, 532)]

        # Load the stage music
        pygame.mixer.music.load(os.path.join(cfg.music_dir, 'Sand_Stage.mp3'))

    # Play the stage music
    if cfg.sound:
        pygame.mixer.music.play(-1)

    # Create the camera (used for updating the offset values used for drawing objects to the screen)
    camera = environment.Camera()

    # Create a sprite group for on-screen entities
    # OrderedUpdates type to make sure everything draws in the order they were appended to the group
    entities = pygame.sprite.OrderedUpdates()

    # Create a list of players
    humans = []
    bots = []

    for plyr in range(0, len(characters)):
        # If the player chose random, then generate a random character index
        if characters[plyr] == 4:
            characters[plyr] = random.randint(0, 3)
            settings[1] = characters

        # Set the current player's character to Pebble with the specified amount of lives
        if characters[plyr] == 0:
            char = character.Pebble(lives, spawnpoints[plyr])

        # Set the current player's character to Crystal with the specified amount of lives
        elif characters[plyr] == 1:
            char = character.Crystal(lives, spawnpoints[plyr])

        # Set the current player's character to Magma with the specified amount of lives
        elif characters[plyr] == 2:
            char = character.Magma(lives, spawnpoints[plyr])

        # Set the current player's character to Pharaoh with the specified amount of lives
        elif characters[plyr] == 3:
            char = character.Pharaoh(lives, spawnpoints[plyr])
        
        entities.add(char)

        try:
            joystick = pygame.joystick.Joystick(plyr)
            joystick.init()
        
        except pygame.error:
            joystick = None

        if plyr == 0:
            keyboard = [
                pygame.K_w, # Up
                pygame.K_s, # Down
                pygame.K_a, # Left
                pygame.K_d, # Right
                pygame.K_t, # Up attack
                pygame.K_g, # Down attack
                pygame.K_f, # Left attack
                pygame.K_h # Right attack
            ]

        elif plyr == 1:
            keyboard = [
                pygame.K_i, # Up
                pygame.K_k, # Down
                pygame.K_j, # Left
                pygame.K_l, # Right
                pygame.K_UP, # Up attack
                pygame.K_DOWN, # Down attack
                pygame.K_LEFT, # Left attack
                pygame.K_RIGHT # Right attack
            ]
        
        else:
            keyboard = None
        
        if playertypes[plyr] == 'Human':
            humans.append(player.Human(keyboard, joystick, char))
        
        else:
            bots.append(player.Bot(char, botdiffs[plyr]))

    # # Load the font for the HUD
    # dbgfont = pygame.font.SysFont(None, 25)

    # Countdown timer that lasts 181 frames (~3 seconds at 60fps)
    countdown = 181

    # Render the font for the countdown in advance
    text_1 = assets.countdown_font.render('1', True, (255,255,255))
    text_2 = assets.countdown_font.render('2', True, (255,255,255))
    text_3 = assets.countdown_font.render('3', True, (255,255,255))
    text_go = assets.countdown_font.render('GO!', True, (255,255,255))

    # Start the loop
    running = True

    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                return_to_title = menu.Options("Fight")
                if return_to_title:
                    running = False
                    loser = ""

        if countdown < 0:
            for human in humans:
                human.updateInputs()

            for bot in bots:
                bot.updateInputs(entities.sprites(), stage)
            
        # Update the camera offsets according to the position of on-screen entities
        camera.updatePos(entities.sprites())

        # Update the position of the world objects relative to the camera position
        world.update(camera)

        # Draw the environment sprites to the screen
        world.draw(cfg.window)

        # Update the state of every entity
        entities.update(camera, world.sprites(), entities.sprites())

        # Draw the entities to the screen
        entities.draw(cfg.window)

        # Draw the in-game HUD
        interface.Display(entities.sprites())

        if countdown > -30:
            countdown -= 1

            if countdown == 180:
                if cfg.sound:
                    pygame.mixer.Sound(os.path.join(cfg.voice_dir, '3.ogg')).play()

            elif countdown == 120:
                if cfg.sound:
                    pygame.mixer.Sound(os.path.join(cfg.voice_dir, '2.ogg')).play()

            elif countdown == 60:
                if cfg.sound:
                    pygame.mixer.Sound(os.path.join(cfg.voice_dir, '1.ogg')).play()

            elif countdown == 0:
                if cfg.sound:
                    pygame.mixer.Sound(os.path.join(cfg.voice_dir, 'Go.ogg')).play()
            
            if 121 < countdown <= 180:
                cfg.window.blit(text_3, (cfg.width / 2 - pygame.Surface.get_width(text_3) / 2, cfg.height / 2 - pygame.Surface.get_height(text_3) / 2))
            
            elif 61 < countdown <= 120:
                cfg.window.blit(text_2, (cfg.width / 2 - pygame.Surface.get_width(text_2) / 2, cfg.height / 2 - pygame.Surface.get_height(text_2) / 2))
            
            elif 0 < countdown <= 60:
                cfg.window.blit(text_1, (cfg.width / 2 - pygame.Surface.get_width(text_1) / 2, cfg.height / 2 - pygame.Surface.get_height(text_1) / 2))
            
            elif -30 < countdown <= 0:
                cfg.window.blit(text_go, (cfg.width / 2 - pygame.Surface.get_width(text_go) / 2, cfg.height / 2 - pygame.Surface.get_height(text_go) / 2))

        # # Draw collision boxes (DEBUG)
        # for e in entities.sprites():
        #     pygame.draw.rect(cfg.window, (0,255,0), e.hurtbox, 1)
        #     pygame.draw.rect(cfg.window, (0,0,255), e.rect, 1)

        #     for attack in e.active_attacks:
        #         for hitbox in attack.active_hitboxes:
        #             pygame.draw.rect(cfg.window, (255,0,0), hitbox.rect, 1)

        # for p in world.sprites():
        #     pygame.draw.rect(cfg.window, (0,255,0), p.rect, 1)

        # # Render and draw text to the screen (DEBUG)
        # cfg.window.blit(dbgfont.render('x: ' + str(humans[0].character.x) + ' y: ' + str(humans[0].character.y), True, (255,255,255)), (10, 10))
        # cfg.window.blit(dbgfont.render('rx: ' + str(humans[0].character.hurtbox.x) + ' ry: ' + str(humans[0].character.hurtbox.y), True, (255,255,255)), (10, 30))
        # cfg.window.blit(dbgfont.render('cx: ' + str(camera.x_offset) + ' cy: ' + str(camera.y_offset), True, (255,255,255)), (10, 50))
        # cfg.window.blit(dbgfont.render('airbourne: ' + str(humans[0].character.airbourne), True, (255,255,255)), (10, 70))
        # cfg.window.blit(dbgfont.render('xv: ' + str(humans[0].character.x_vel) + ' yv: ' + str(humans[0].character.y_vel), True, (255,255,255)), (10, 90))
        # cfg.window.blit(dbgfont.render('attacking: ' + str(humans[0].character.attacking), True, (255,255,255)), (10, 110))
        # cfg.window.blit(dbgfont.render('fps: ' + str(cfg.clock.get_fps()), True, (255,255,255)), (10, 130))

        # try:
        #     for a in range(0, humans[0].joystick.get_numaxes()):
        #         cfg.window.blit(dbgfont.render(str(a) + ': ' + str(humans[0].joystick.get_axis(a)), True, (255,255,255)), (10, 150 + a * 20))
            
        #     for b in range(0, humans[0].joystick.get_numbuttons()):
        #         cfg.window.blit(dbgfont.render(str(b) + ': ' + str(humans[0].joystick.get_button(b)), True, (255,255,255)), (300, 10 + b * 20))
        
        # except AttributeError:
        #     pass

        # Check if anyone has no lives. If so, end the game
        for e in entities.sprites():
            if e.lives <= 0:
                running = False
                loser = entities.sprites().index(e)

        # Update the screen
        pygame.display.flip()
        cfg.clock.tick(60)
    
    #print("ok1")
    pygame.mixer.music.stop()
    if cfg.sound:
        pygame.mixer.Sound(os.path.join(cfg.voice_dir, 'Game_Over.ogg')).play()

    while pygame.mixer.get_busy():
        pass
    
    #print("ok2")
    if return_to_title:
        next_scene = "Title Screen"
    else:
        next_scene = "Results"
    #print("ok3")
    return next_scene, settings, loser