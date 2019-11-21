# Author: Aaron Castellino
# Date: 21/9/2018
# File Name: mwnu.py
# Description: This file stores the functions for the menus 

#import important libraries
import pygame, sys, time, random, os, cfg, assets

class Button(object): # Class for Buttons
    def __init__(self,image,xpos,ypos):
        self.image = image
        self.xpos = xpos - pygame.Surface.get_width(image)/2 # centers the x pos for picture
        self.ypos = ypos - pygame.Surface.get_height(image)/2 # centers the y pos for picture
        self.left = pygame.Surface.get_width(image) # stores width of image
        self.top = pygame.Surface.get_height(image) # stores height of image
        self.rect = pygame.Rect(self.xpos,self.ypos,self.left,self.top) # creates a rect object the same size as image
    def HighlightAuto(self,colour): # creates a highlight affect around the image
        pygame.draw.rect(cfg.window, colour, self.rect, 8)
    def HighlightManual(self,highlight_image):  # creates a highlight affect around the image by displaying highlighted image
        highlight_w = pygame.Surface.get_width(highlight_image)/2
        highlight_h = pygame.Surface.get_height(highlight_image)/2
        xcord = (self.xpos + pygame.Surface.get_width(self.image)/2) - highlight_w
        ycord = (self.ypos + pygame.Surface.get_height(self.image)/2) - highlight_h
        cfg.window.blit(highlight_image,(xcord,ycord))
    def Display(self,windowSurface): # Draws the image to the screen
        cfg.window.blit(self.image,(self.xpos,self.ypos))
        

class Portrait(object): #Class for Character Portraits
    def __init__(self,xpos,ypos): 
        #stores variables from input
        self.xpos = xpos
        self.ypos = ypos
        #creates variables for later use in code
        self.number = -1
        self.name = 'Pebble'
        self.framebuffer = 4
        self.frame = 0
        self.framecount = 0
    def update(self,number,windowSurface):
        if self.number != number: # if user changed the displayed image
            self.number = number # store number
            self.getCharacterAnimations() # gets the Idle animation for the character
            self.frame = 0 # reset the frame
            self.framecount = 0 # reset the frame count
                # Set the character's idle image
            self.image = self.animation[0] #set the first image in the animation.
            
            self.x = self.xpos - pygame.Surface.get_width(self.image)/2 # adjust xpos 
            self.y = self.ypos - pygame.Surface.get_height(self.image)# adjust ypos
    
            # Create a rect for entity collision detection (hitboxes)
            self.rect = pygame.rect.Rect(self.x, self.y, 0, 0)
            self.imageRect = pygame.Rect.copy(self.rect)
    
            # Calculate the width and height of the character
            self.rect.width = pygame.Surface.get_width(self.image)
            self.rect.height = pygame.Surface.get_height(self.image)
            
            #Display the image for the character
            cfg.window.blit(self.image,(self.imageRect.x,self.imageRect.y))

        else: #when the same character is still selected
            
                    # Once the frame delay is over, update the current frame of animation
            self.framecount += 1
            if self.framecount == self.framebuffer:
                self.framecount = 0
                self.frame = (self.frame + 1) % len(self.animation)
                self.image = self.animation[self.frame - 1]
    
                # If the width of the image has changed, then update the rect width
                if pygame.Surface.get_width(self.image) != self.rect.width:
                    #if self.facing == 'West':
                    #    self.rect.x -= pygame.Surface.get_width(self.image) - self.rect.width
                    self.rect.width = pygame.Surface.get_width(self.image)
    
                # If the height of the image has changed, then update the rect height
                if pygame.Surface.get_height(self.image) != self.imageRect.height:
                    self.rect.y -= pygame.Surface.get_height(self.image) - self.rect.height
                    self.rect.height = pygame.Surface.get_height(self.image)
            
            #Display image for the character        
            cfg.window.blit(self.image,(self.rect.x,self.rect.y))

    def getCharacterAnimations(self):
        #Depending on the Number Change the name and scale factors
        if self.number == 0:
            self.name = 'Pebble'
            self.scale_x = 11
            self.scale_y = 11
        elif self.number == 1:
            self.name = 'Crystal'
            self.scale_x = 7
            self.scale_y = 8
        elif self.number == 2:
            self.name = 'Magma'
            self.scale_x = 8
            self.scale_y = 8
        elif self.number == 3:
            self.name = 'Pharaoh'
            self.scale_x = 10
            self.scale_y = 10
        elif self.number == 4:
            self.name = 'Random'
            self.scale_x = 8
            self.scale_y = 8
        
        #gets the file location for the Character Sprite
        self.sprites = os.path.join(cfg.chranim_dir, self.name) 
        
        self.animation = [] # Clears the animation list
            
        for file in sorted(os.listdir(self.sprites)):
    
                # Store the full path of the current file
            filepath = os.path.join(self.sprites, file)
    
                # Upscale the animation frame by a factor of 4
            frame = pygame.image.load(filepath).convert_alpha()
            frame_width = pygame.Surface.get_width(frame)
            frame_height = pygame.Surface.get_height(frame)
            frame_scaled = pygame.transform.scale(frame, (frame_width * self.scale_x, frame_height * self.scale_y))
    
                # If it's an idle animation frame, add it to it's frame list
            if file.startswith('idle') and file.endswith('.png'):
                self.animation.append(frame_scaled)
        


class AnimatedBackground(object):
    def __init__(self,xpos,ypos): 
        #stores variables from input
        self.xpos = xpos
        self.ypos = ypos
        #creates variables for later use in code
        self.framebuffer = 8
        self.frame = 0
        self.framecount = 0
        
        self.animation = [] # Clears the animation list
            
        for file in sorted(os.listdir(cfg.menu_dir)):
    
                # Store the full path of the current file
            filepath = os.path.join(cfg.menu_dir, file)
    
                # Upscale the animation frame by a factor of 4
            frame = pygame.image.load(filepath).convert_alpha()
            frame_width = pygame.Surface.get_width(frame)
            frame_height = pygame.Surface.get_height(frame)
            frame_scaled = pygame.transform.scale(frame, (frame_width * 1, frame_height * 1))
    
                # If it's an idle animation frame, add it to it's frame list
            if file.startswith('results') and file.endswith('.png'):
                self.animation.append(frame_scaled)
        self.image = self.animation[0]  
    def Update(self):    
        # Once the frame delay is over, update the current frame of animation
        self.framecount += 1
        if self.framecount == self.framebuffer:
            self.framecount = 0
            self.frame = (self.frame + 1) % len(self.animation)
            self.image = self.animation[self.frame - 1]           
        #Display image for the character        
        cfg.window.blit(self.image,(self.xpos,self.ypos))


def GetPos(ratio_w,ratio_h): # Function which converts ratios to appropriate pixel display coords
    xpos = ratio_w * cfg.width # multiply screen width by ratio
    ypos = ratio_h * cfg.height # multiply screen height by ratio 
    return xpos,ypos # return coords

def GetPosCentre(ratio_w,ratio_h,image):# Function which converts ratios to appropriate pixel display coords centered with image
    xpos = ratio_w * cfg.width - pygame.Surface.get_width(image)/2 # multiply screen width by ratio and centre for width
    ypos = ratio_h * cfg.height - pygame.Surface.get_height(image)/2 # multiply screen height by ratio and centre for height
    return xpos,ypos # return coords

def MainMenu(settings):
    
    #sets mouse event variables
    mouseClicked = False
    mousex = 0 
    mousey = 0
    
    if not pygame.mixer.music.get_busy():
        #load and play music
        pygame.mixer.music.load(os.path.join(cfg.music_dir,'mainmenu.ogg'))
        if cfg.sound:
            pygame.mixer.music.play(-1,0)
            
    #get coords for images
    startbutton_x,startbutton_y = GetPos(1/2, 8/10)
    exit_x , exit_y = GetPos(1/8, 1/16)
    mineralmadness_x,mineralmadness_y = GetPosCentre(1/2, 1/4,assets.Mineral_Maddness_image)

    #creates instance of start button
    startButton = Button(assets.start_image,startbutton_x,startbutton_y)
    exitButton = Button(assets.exit_game_image,exit_x,exit_y)
    
    #sets main menu loop to True
    main_menu = True
    
    while main_menu == True:
        
        mouseClicked = False
        
        for event in pygame.event.get():# checks events
            if event.type == pygame.QUIT: # quits if exit
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos # get mouse location
    
            if event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos
                mouseClicked = True


    
        # draw the black background onto the surface
        cfg.window.blit(assets.background_image1,(0,0))
    
    
        if startButton.rect.collidepoint(mousex, mousey):# checks if mouse if above start button image
            if mouseClicked == True: # if clicked stop looping and end function mouse click to True
                main_menu = False
                button = "Mode Menu" 
                
            else:# if button is not clicked highlight it
                startButton.HighlightManual(assets.start_image_highlight)
        
        elif exitButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Sprites
            if mouseClicked == True: #Creates a condition if the user chooses to exit
                pygame.quit() #Calls upon the quit function from the pygame library
                sys.exit()    #Exits the game    
            else:
                exitButton.HighlightManual(assets.exit_game_image_highlight) #If the mouse is over the button but not clicking the button, the button will highlight so the user knows they are accessing the button
        
                
        startButton.Display(cfg.window) # draw start button to surface
        exitButton.Display(cfg.window)
        cfg.window.blit(assets.Mineral_Maddness_image,(mineralmadness_x,mineralmadness_y)) # draw title to surface
    
        # draw the window onto the screen
        pygame.display.flip()
        cfg.clock.tick(60) #Lock FPS
    return button

def ModeMenu(settings):
 #Launch Secondary Menu
    
    
    if not pygame.mixer.music.get_busy():
        #load and play music
        pygame.mixer.music.load(os.path.join(cfg.music_dir,'mainmenu.ogg'))
        if cfg.sound:
            pygame.mixer.music.play(-1,0)
    
    #sets mouse event variables
    mouseClicked = False
    mousex = 0 
    mousey = 0
    
    #get coords to display images
    mode_1_x , mode_1_y = GetPos(1/4, 5/8)
    mode_2_x , mode_2_y = GetPos(3/4, 5/8)
    options_x , options_y = GetPos(15/16, 1/16)
    back_x , back_y = GetPos(1/8, 1/16)
    help_x , help_y = GetPos(17/20, 1/16)
    mode_select_x, mode_select_y = GetPosCentre(1/2, 1/4, assets.mode_menu)
    
    #creates an instance for both buttons
    mode_1_Button = Button(assets.mode_1_player,mode_1_x,mode_1_y)
    mode_2_Button = Button(assets.mode_2_player,mode_2_x,mode_2_y)
    options = Button(assets.options_image,options_x,options_y)
    backButton = Button(assets.back_image,back_x,back_y)
    help = Button(assets.help_image,help_x,help_y)
    

    # loop runs while game is True
    game = True
    while game == True:
        
        mouseClicked = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user quits close program
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION: # gets location of mouse if it moves
                mousex, mousey = event.pos
    
            if event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos
                mouseClicked = True


    
        # draw the black background onto the surface
        cfg.window.blit(assets.background_image1,(0,0))
    
    
        if mode_1_Button.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Smash
            if mouseClicked == True:
                game = False
                button = "Stage"
                settings[2] = ['Human', 'Bot']
                
            else:
                mode_1_Button.HighlightManual(assets.mode_1_highlight)
        elif mode_2_Button.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                game = False
                button = "Stage"
                settings[2] = ['Human', 'Human']
                
            else:
                mode_2_Button.HighlightManual(assets.mode_2_highlight)
                 
        elif options.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                Options("Menu")
                 
                
            else:
                options.HighlightManual(assets.options_highlight_image)
        elif help.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                Help()
                 
                
            else:
                help.HighlightManual(assets.help_highlight_image)
        elif backButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                game = False
                button = "Main"
                
            else:
                backButton.HighlightManual(assets.back_image_highlight)
         
        #Draws all images to screen  
        cfg.window.blit(assets.mode_menu,(mode_select_x,mode_select_y)) # draw title to surface 
        backButton.Display(cfg.window)    
        mode_1_Button.Display(cfg.window)
        mode_2_Button.Display(cfg.window)
        options.Display(cfg.window)
        help.Display(cfg.window)
    
        # draw the window onto the screen
        pygame.display.flip()
        cfg.clock.tick(60)
    return button , settings

def StageMenu(settings):
    
    #sets mouse event variables
    mouseClicked = False
    mousex = 0 
    mousey = 0
    
    stage = 0
    
    if not pygame.mixer.music.get_busy():
        #load and play music
        pygame.mixer.music.load(os.path.join(cfg.music_dir,'mainmenu.ogg'))
        if cfg.sound:
            pygame.mixer.music.play(-1,0)
            
    stage_previews = []
    for stage_position in range (1,6):
        #Load Each image into Array
        current_image = pygame.image.load(os.path.join(cfg.menu_dir,'stage_preview' + str(stage_position) +'.png')).convert_alpha()
        stage_previews.append(current_image)
    


    #get coords to display images
    options_x , options_y = GetPos(15/16, 1/16)
    back_x , back_y = GetPos(1/8, 1/16)
    help_x , help_y = GetPos(17/20, 1/16)
    stage_select_x, stage_select_y = GetPosCentre(1/2, 1/10, assets.stage_select_image)
    stage_preview_x, stage_preview_y = GetPosCentre(1/2, 9/20, stage_previews[0])
    stage_font_x ,stage_font_y = GetPos(1/2, 13/20)
    
    #creates instance of start button
    #startButton = Button(assets.start_image,400,475)
    backButton = Button(assets.back_image,back_x,back_y)
    options = Button(assets.options_image,options_x,options_y)
    help = Button(assets.help_image,help_x,help_y)

  
    #array for character buttons
    stage_buttons = []
    for stage_position in range (1,6):
        #Load Each image into Array
        current_image = pygame.image.load(os.path.join(cfg.menu_dir,'stage_icon' + str(stage_position) +'.png')).convert_alpha()
        # Even on one side odd on the other for 2 columns
        if stage_position % 3 == 1:
            stage_x = 7/20 * cfg.width
        elif stage_position % 3 == 2:
            stage_x = 1/2 * cfg.width
        else:
            stage_x = 13/20 * cfg.width
        #redduce character position for so numbers are 0 -6 and so first 2 numbers floor division are 0 second 2 are 1 and so on
        stage_position -= 1
        stage_y = 23/30 * cfg.height + (stage_position // 3) * 3/20 * cfg.height # adds 70 pixel space to each row
        # Build Buttons
        current_image = Button(current_image,stage_x,stage_y)
        #Add Buttons to List
        stage_buttons.append(current_image)
       
        

    #sets main menu loop to True
    mode_menu = True
    
    while mode_menu == True:
        
        mouseClicked = False
        
        for event in pygame.event.get():# checks events
            if event.type == pygame.QUIT: # quits if exit
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos # get mouse location
    
            if event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos
                mouseClicked = True


    
        # draw the black background onto the surface
        cfg.window.blit(assets.background_image2,(0,0))
    
        if backButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
                if mouseClicked == True:
                    mode_menu = False
                    button = "Mode Menu"
                
                else:
                    backButton.HighlightManual(assets.back_image_highlight)
        elif options.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                Options("Menu") 
                
            else:
                options.HighlightManual(assets.options_highlight_image)
        elif help.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                Help()
                 
                
            else:
                help.HighlightManual(assets.help_highlight_image)
        
        #Checks All character Buttons if they have been hit       
        for stage_position in range (0,5):
            if stage_buttons[stage_position].rect.collidepoint(mousex, mousey):
                if mouseClicked:
                    mode_menu = False
                    button = "Character"
                    settings[4] = stage_position 
                else:
                    stage = stage_position 
                    
        if stage == 0:
            stage_name = "Salty Rock Ravine"
        elif stage == 1:
            stage_name = "Crystal Cove"
        elif stage == 2:
            stage_name = "Rumble Volcano"
        elif stage == 3:
            stage_name = "Ancient Temple"
        else:
            stage_name = "Random"
            
        fancyfontStage = assets.stage_font.render((stage_name), True, (150,150,150)) 
        textRectObjStage = fancyfontStage.get_rect()
        textRectObjStage.center  = (stage_font_x,stage_font_y)
        
        cfg.window.blit(assets.stage_select_image,(stage_select_x,stage_select_y)) # draw title to surface
        backButton.Display(cfg.window)
        cfg.window.blit(stage_previews[stage], (stage_preview_x,stage_preview_y))
        cfg.window.blit(fancyfontStage,textRectObjStage)
        options.Display(cfg.window)
        help.Display(cfg.window)
               #Display the Character Buttons
        for stage_position in range (0,5):
            stage_buttons[stage_position].Display(cfg.window)
        # draw the window onto the screen
        pygame.display.flip()
        cfg.clock.tick(60) #Lock FPS
    return button , settings

def CharacterSelect(settings): #Launch Secondary Menu


    #sets mouse event variables
    mouseClicked = False
    mousex = 0 
    mousey = 0
    
    if not pygame.mixer.music.get_busy():
        #load and play music
        pygame.mixer.music.load(os.path.join(cfg.music_dir,'mainmenu.ogg'))
        if cfg.sound:
            pygame.mixer.music.play(-1,0)
    
    #array for character buttons
    character_buttons = []
    for character_position in range (1,6):
        #Load Each image into Array
        current_image = pygame.image.load(os.path.join(cfg.menu_dir,'character_icon' + str(character_position) +'.png')).convert_alpha()
        # Even on one side odd on the other for 2 columns
        if character_position % 2 == 1:
            character_x = 73/160 * cfg.width
        else:
            character_x = 87/160 * cfg.width
        #redduce character position for so numbers are 0 -6 and so first 2 numbers floor division are 0 second 2 are 1 and so on
        character_position -= 1
        character_y = 7/15 * cfg.height + (character_position // 2) * 7/60 * cfg.height # adds 70 pixel space to each row
        # Build Buttons
        current_image = Button(current_image,character_x,character_y)
        #Add Buttons to List
        character_buttons.append(current_image)
     
    
    # Store settings
    lives = settings[0]
    characters = settings[1]
    playertypes = settings[2]
    botdiffs = settings[3]
    
    #stores which character selector is currently selected
    character_selector = 0
    
    #get coords to display images
    options_x , options_y = GetPos(15/16, 1/16)
    back_x , back_y = GetPos(1/8, 1/16)
    help_x , help_y = GetPos(17/20, 1/16)
    character_portrait1_x, character_portrait1_y = GetPos(27/160, 505/600)
    character_portrait2_x, character_portrait2_y = GetPos(131/160, 505/600)
    start_x , start_y = GetPos(1/2, 13/15)
    arrowr_x , arrowr_y = GetPos(49/80, 1/3)
    arrowl_x , arrowl_y = GetPos(41/80, 1/3)
    select1_x,select1_y = GetPos(7/40, 41/60)
    select2_x,select2_y = GetPos(33/40, 41/60)
    text_lives_x, text_lives_y = GetPos(45/80,26/75)
    arrowu_x, arrowu_y =GetPos(35/40, 86/100)
    arrowd_x, arrowd_y =GetPos(35/40, 89/100)
    lives_line_x , lives_line_y = GetPosCentre(1/2, 1/3, assets.lives_line_image)
    character_select_x , character_select_y = GetPosCentre(1/2, 127/600, assets.character_select_image)
    
    


    
    #create instances for the character portraits
    character_portrait1 = Portrait(character_portrait1_x,character_portrait1_y)
    character_portrait2 = Portrait(character_portrait2_x,character_portrait2_y)
    
    #Creates Instance for all Buttons
    startButton = Button(assets.start_image,start_x,start_y)
    arrowRButton = Button(assets.arrow_right,arrowr_x,arrowr_y)
    arrowLButton = Button(assets.arrow_left,arrowl_x,arrowl_y)
    backButton = Button(assets.back_image,back_x,back_y)
    selectorButton1 = Button(assets.character_selector_image,select1_x,select1_y)
    selectorButton2 = Button(assets.character_selector_image,select2_x,select2_y)
    options = Button(assets.options_image,options_x,options_y)
    help = Button(assets.help_image,help_x,help_y)
    
    if playertypes[1] == 'Bot':
        arrowUPButton = Button(assets.arrow_up,arrowu_x,arrowu_y)
        arrowDOWNButton = Button(assets.arrow_down,arrowd_x,arrowd_y)
        p2text = "CPU"
    else:
        p2text = "Player 2"
        
    fancyfontNameP1 = assets.name_font.render(("Player 1"), True, (240,240,240)) 
    textRectObjNameP1 = fancyfontNameP1.get_rect()
    textRectObjNameP1.center  = (character_portrait1.xpos,character_portrait1.ypos - 40/120 * cfg.height)
        
    fancyfontNameP2 = assets.name_font.render((p2text), True, (240,240,240)) 
    textRectObjNameP2 = fancyfontNameP2.get_rect()
    textRectObjNameP2.center  = (character_portrait2.xpos,character_portrait2.ypos - 40/120 * cfg.height)
        

    # loop runs while game is True
    game = True
    while game == True:

        #resets mouse variable
        mouseClicked = False
        cheat_part = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if user quits close program
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION: # gets location of mouse if it moves
                mousex, mousey = event.pos
    
            if event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos
                mouseClicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    cheat_part = True # if x is pressed activate part of cheat
        if pygame.key.get_mods() == 65 and cheat_part: # if Ctrl + Shift + x is pressed cheat activates
            cheats = True
        
        # draw the black background onto the surface
        cfg.window.blit(assets.background_image2,(0,0))
        
        if playertypes[1] == 'Bot':
            if arrowUPButton.rect.collidepoint(mousex, mousey) and mouseClicked == True:
                botdiffs[1] += 1 
                if botdiffs[1] > 2:# if Right Arrow Clicked increase Lives , Maximum is 99
                    botdiffs[1] = 2
            elif arrowDOWNButton.rect.collidepoint(mousex, mousey) and mouseClicked == True:
                botdiffs[1] -= 1 
                if botdiffs[1] < 1:# if Right Arrow Clicked increase Lives , Maximum is 99
                    botdiffs[1] = 1
            elif selectorButton1.rect.collidepoint(mousex, mousey) and mouseClicked == True:
                character_selector = 1 #Character Selector Selected is 1 if it is clicked
            elif selectorButton2.rect.collidepoint(mousex, mousey) and mouseClicked == True:
                character_selector = 2 #Character Selector Selected is 1 if it is clicked
        else:
            if selectorButton1.rect.collidepoint(mousex, mousey) and mouseClicked == True:
                character_selector = 1 #Character Selector Selected is 1 if it is clicked
            elif selectorButton2.rect.collidepoint(mousex, mousey) and mouseClicked == True:
                character_selector = 2 #Character Selector Selected is 1 if it is clicked
        

    

        if arrowRButton.rect.collidepoint(mousex, mousey) and mouseClicked == True:
            lives += 1 
            if lives > 99:# if Right Arrow Clicked increase Lives , Maximum is 99
                lives = 99
        elif arrowLButton.rect.collidepoint(mousex, mousey) and mouseClicked == True:
            lives -= 1
            if lives < 1:# if Right Arrow Clicked Decrease Lives , Minimum is 1
                lives = 1
        elif backButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                game = False # ends loop
                button = "Mode Menu" # return to the Mode menu
                #rebuild settings with new values

                settings[0] = lives
                settings[1] = characters
                settings[2] = playertypes
                settings[3] = botdiffs
                
            else:
                backButton.HighlightManual(assets.back_image_highlight) #Highlight Back Button when not clicked
        elif startButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                game = False # ends loop
                button = "Game" # go to Game Screen
                #rebuild settings with new values
                settings[0] = lives
                settings[1] = characters
                settings[2] = playertypes
                settings[3] = botdiffs
                
            else:
                startButton.HighlightManual(assets.start_image_highlight) # highlight button when not clicked
        elif options.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                Options("Menu")
                
            else:
                options.HighlightManual(assets.options_highlight_image)
        elif help.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Spirits
            if mouseClicked == True:
                Help()
                 
                
            else:
                help.HighlightManual(assets.help_highlight_image)
         #Checks All character Buttons if they have been hit       
        for character_position in range (0,5):
            if character_buttons[character_position].rect.collidepoint(mousex, mousey) and mouseClicked == True:
                if character_selector == 1:
                    characters[0] = character_position
                elif character_selector == 2:
                    characters[1] = character_position
                character_selector = 0 # No Character
         
        #Create Font of Lives variable to be Displayed    
        fancyfontLives = assets.lives_font.render(str(lives), True, (240,240,240)) 
        textRectObjLives = fancyfontLives.get_rect()
        textRectObjLives.center  = (text_lives_x,text_lives_y)
        
        #Create a font for the Names to be Displayed
        fancyfontName = assets.name_font.render(str(character_portrait1.name), True, (240,240,240)) 
        textRectObjName = fancyfontName.get_rect()
        textRectObjName.center  = (character_portrait1.xpos,character_portrait1.ypos + 6/150 * cfg.height )
        
        
        if playertypes[1] == 'Human':
            fancyfontName2 = assets.name_font.render(str(character_portrait2.name), True, (240,240,240)) 
            textRectObjName2 = fancyfontName2.get_rect()
            textRectObjName2.center  = (character_portrait2.xpos,character_portrait2.ypos + 6/150 * cfg.height)
        else:
            if botdiffs[1] == 1:
                difficulty_text = "Normal"
            elif botdiffs[1] == 2:
                difficulty_text = "Expert"
            elif botdiffs[1] == 3:
                difficulty_text = "Impossible"
            else:
                difficulty_text = "ERROR"
            fancyfontName2 = assets.name_font.render(difficulty_text, True, (240,240,240)) 
            textRectObjName2 = fancyfontName2.get_rect()
            textRectObjName2.center  = (character_portrait2.xpos - 1/50 * cfg.width ,character_portrait2.ypos + 6/150 * cfg.height)
            

#                

        if character_selector == 1:
            selectorButton1.HighlightManual(assets.character_selectorP1) #Highlight Character Selector 1 if Selected
        else:
            selectorButton1.Display(cfg.window)# Display Regular image if not selected
        if character_selector == 2:
            selectorButton2.HighlightManual(assets.character_selectorP2) #Highlight Character Selector 1 if Selected
        else:
            selectorButton2.Display(cfg.window) # Display Regular image if not selected
        
        #Display Images
        cfg.window.blit(assets.lives_line_image,(lives_line_x,lives_line_y))
        cfg.window.blit(assets.character_select_image,(character_select_x,character_select_y))
        arrowRButton.Display(cfg.window)
        arrowLButton.Display(cfg.window)
        backButton.Display(cfg.window)
        startButton.Display(cfg.window)
        character_portrait1.update(characters[0],cfg.window)
        character_portrait2.update(characters[1],cfg.window)
        if playertypes[1] == 'Bot':
            arrowUPButton.Display(cfg.window)
            arrowDOWNButton.Display(cfg.window)
        
       #Display the Character Buttons
        for character_position in range (0,5):
            character_buttons[character_position].Display(cfg.window)
        cfg.window.blit(fancyfontLives,textRectObjLives)
        cfg.window.blit(fancyfontName,textRectObjName)
        cfg.window.blit(fancyfontNameP1,textRectObjNameP1)
        cfg.window.blit(fancyfontNameP2,textRectObjNameP2)
        cfg.window.blit(fancyfontName2,textRectObjName2)
        options.Display(cfg.window)
        help.Display(cfg.window)
                
        # draw the window onto the screen
        pygame.display.flip()
        cfg.clock.tick(60)
        
    return button, settings # end loop returns next screen and the settings selected

def VictoryScreen(settings, results):
    
    
    #sets mouse event variables
    mouseClicked = False
    mousex = 0 
    mousey = 0
    
    characters = settings[1] 
    player_type = settings[2]
    
    if results == 1:
            podium_image = assets.podium1_image_scaled
            y1 = 92/120 * cfg.height
            y2 = 102/120 * cfg.height
            result_text = "Player 1 Wins!"
            if cfg.sound:
                pygame.mixer.Sound(os.path.join(cfg.voice_dir, 'Victory_Screech.ogg')).play()
    else:
            podium_image = assets.podium2_image_scaled
            y1 = 102/120 * cfg.height
            y2 = 92/120 * cfg.height
            if player_type[1] == "Bot":
                result_text = "Computer Wins!"
                if cfg.sound:
                    pygame.mixer.Sound(os.path.join(cfg.voice_dir, 'Loser.ogg')).play()
            else:
                result_text = "Player 2 Wins!"
                if cfg.sound:
                    pygame.mixer.Sound(os.path.join(cfg.voice_dir, 'Defeat.ogg')).play()
    
    #get coords to display images
    result_x , result_y = GetPos(1/2, 7/30)
    next_x , next_y = GetPos(69/80, 1/12)
    podium_x, podium_y = GetPosCentre(1/2,1, podium_image)
    podium_y -= pygame.Surface.get_height(podium_image)/2

                
    fancyfontResult = assets.result_font.render((result_text), True, (240,240,240)) 
    textRectObjResult = fancyfontResult.get_rect()
    textRectObjResult.center  = (result_x,result_y)
    
     #create instances for the character portraits
    character_portrait1 = Portrait(70/160 * cfg.width,y1)
    character_portrait2 = Portrait(90/160 * cfg.width,y2)
    
    backgroundAnimated = AnimatedBackground(0,0)
            
    
    
    if not pygame.mixer.music.get_busy():
        #load and play music
        pygame.mixer.music.load(os.path.join(cfg.music_dir,'mainmenu.ogg'))
        if cfg.sound:
            pygame.mixer.music.play(-1,0)

    #creates instance of start button
    nextButton = Button(assets.next_image,next_x,next_y)

    
    #sets main menu loop to True
    main_menu = True
    
    while main_menu == True:
        
        mouseClicked = False
        
        for event in pygame.event.get():# checks events
            if event.type == pygame.QUIT: # quits if exit
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos # get mouse location
    
            if event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos
                mouseClicked = True


    
        # draw the black background onto the surface
        #cfg.window.blit(background_image,(0,0))
        backgroundAnimated.Update()
        
        # loads the podium image to the victory screen
        cfg.window.blit(podium_image,(podium_x,podium_y))
        cfg.window.blit(fancyfontResult,textRectObjResult)
    
        if nextButton.rect.collidepoint(mousex, mousey):# checks if mouse if above start button image
            if mouseClicked == True: # if clicked stop looping and end function mouse click to True
                main_menu = False
                button = "Mode Menu" 
                
            else:# if button is not clicked highlight it
                nextButton.HighlightManual(assets.next_image_highlight)
                
        nextButton.Display(cfg.window) # draw start button to surface
        
        characters = settings[1]
        
        
        character_portrait1.update(characters[0],cfg.window)
        character_portrait2.update(characters[1],cfg.window)
        
                # Draw the in-game HUD
        cfg.window.blit(assets.p1arrow_scaled, (145/320 * cfg.width - 1/30 * cfg.width,character_portrait1.rect.top - 1/15 * cfg.height))
        cfg.window.blit(assets.p2arrow_scaled, (185/320 * cfg.width - 1/30 * cfg.width,character_portrait2.rect.top  - 1/15 * cfg.height))
        
    
        # draw the window onto the screen
        pygame.display.flip()
        cfg.clock.tick(60) #Lock FPS
    return button

def Options(scene): #Creates a function that displays an options menu. The options menu contains help and instructions and the option to turn off the sound.   
       
    #get coords to display images
    back_x , back_y = GetPos(1/8, 1/16)
    exit_x , exit_y = GetPos(7/8, 1/16)
    return_x , return_y = GetPos(1/2, 1/16)
    sound_x, sound_y = GetPos(5/8, 1/4)
    s_text_x, s_text_y =GetPos(7/16, 1/4)
    player_controls_x, player_controls_y =GetPosCentre(1/2, 2/3,assets.player_controls_scaled)
    
    #creates an instance for both buttons
    sound_on_button = Button(assets.sound_on_button_scaled,sound_x,sound_y) #Creates an instance for the "sound on" button
    sound_off_button = Button(assets.sound_off_button_scaled,sound_x,sound_y) #Creates an instance for the "sound off" button
    backButton = Button(assets.back_image,back_x,back_y)
    exitButton = Button(assets.exit_game_image,exit_x,exit_y)
    returnButton = Button(assets.return_to_title_image,return_x,return_y)
    
    
    fancyfontSound = assets.sound_font.render(("Sound:"), True, (240,240,240)) 
    textRectObjSound = fancyfontSound.get_rect()
    textRectObjSound.center  = (s_text_x,s_text_y)

    return_to_title = False
                      
    #sets mouse event variables
    mouseClicked = False #Creates a condition for the mouse. "False" means the mouse is not being clicked
    mousex = 0 #Sets a placeholder variable for the x-coordinate of the mouse's position
    mousey = 0 #Sets a placeholder variable for the y-coordinate of the mouse's position
    # loop runs while game is True
    game = True #Sets a condition for the game to run on and the game will only exit when the user chooses to do so
    while game == True:  #Runs the game loop until the user quits     
        mouseClicked = False #Creates a condition for the mouse. "False" means the mouse is not being clicked
                       
        for event in pygame.event.get(): #Imports a module from the python library
            if event.type == pygame.QUIT: # if user quits close program
                pygame.quit() #Calls upon the quit function from the pygame library
                sys.exit()    #Exits the game          
            elif event.type == pygame.MOUSEMOTION: # gets location of mouse if it moves
                mousex, mousey = event.pos #Creates a location in the style of a tuple depending on where the mouse is on the screen
 
            elif event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos #Creates a location in the style of a tuple depending on where the mouse is on the screen
                
                mouseClicked = True   #Creates a condition for the mouse. "True" means the mouse is being clicked
                
        cfg.window.blit(assets.background_image2,(0,0))
        
        if sound_on_button.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked, it will end the music
            if mouseClicked == True: #If the mouse is clicked on the sound on button
                if cfg.sound == True:#Defines the sound as "on"
                    cfg.sound = False
                    pygame.mixer.music.pause()
                else:
                    cfg.sound = True
                    pygame.mixer.music.unpause()
                    if not pygame.mixer.music.get_busy():
                        #load and play music
                        pygame.mixer.music.play(-1,0)

        
        elif backButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Sprites
            if mouseClicked == True: #Creates a condition if the user chooses to exit
                game = False #Ends the Options menu loop  
            else:
                backButton.HighlightManual(assets.back_image_highlight) #If the mouse is over the button but not clicking the button, the button will highlight so the user knows they are accessing the button
        
                
        elif returnButton.rect.collidepoint(mousex, mousey) and  scene == "Fight": # Highlights Button and if clicked ends loop and return Sprites
            if mouseClicked == True: #Creates a condition if the user chooses to exit
                game = False #Ends the Options menu loop
                return_to_title = True  
            else:
                returnButton.HighlightManual(assets.return_to_title_highlight_image) #If the mouse is over the button but not clicking the button, the button will highlight so the user knows they are accessing the button
        
        elif exitButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Sprites
            if mouseClicked == True: #Creates a condition if the user chooses to exit
                pygame.quit() #Calls upon the quit function from the pygame library
                sys.exit()    #Exits the game   
            else:
                exitButton.HighlightManual(assets.exit_game_image_highlight) #If the mouse is over the button but not clicking the button, the button will highlight so the user knows they are accessing the button
        
        #Draws all images to screen
        
        backButton.Display(cfg.window) #Draws the back button to the screen
        if cfg.sound == True:
            sound_on_button.Display(cfg.window) #Draws the sound on button to the screen
        else:
            sound_off_button.Display(cfg.window) #Draws the sound off button to the screen
        cfg.window.blit(fancyfontSound,textRectObjSound)
        cfg.window.blit(assets.player_controls_scaled, (player_controls_x,player_controls_y))
        exitButton.Display(cfg.window)
        if scene == "Fight":
            returnButton.Display(cfg.window)
        
        # draw the window onto the screen
        pygame.display.flip() #Updates the onscreen image
        cfg.clock.tick(30) #Sets a speed for the game to run at
    return return_to_title

def Help():
    
    help_text = []
    for stage_position in range (1,7):
        #Load Each image into Array
        current_image = pygame.image.load(os.path.join(cfg.menu_dir,'help_text' + str(stage_position) +'.png')).convert_alpha()
        help_text.append(current_image)
    

    
    #get coords to display images
    back_x , back_y = GetPos(1/8, 1/16)
    arrowr_x, arrowr_y =GetPos(7/8, 67/75)
    arrowl_x, arrowl_y =GetPos(31/40, 67/75)
    pg_text_x,pg_text_y = GetPos(1/2, 9/10)
    help_text_x,help_text_y = GetPos(1/2, 1/6)
    pg_help_x,pg_help_y = GetPosCentre(1/2,21/40,help_text[0])
    
    #setup buttons
    backButton = Button(assets.back_image,back_x,back_y)
    arrowRButton = Button(assets.arrow_right_scaled,arrowr_x,arrowr_y)
    arrowLButton = Button(assets.arrow_left_scaled,arrowl_x,arrowl_y)
    #sets mouse event variables
    mouseClicked = False #Creates a condition for the mouse. "False" means the mouse is not being clicked
    mousex = 0 #Sets a placeholder variable for the x-coordinate of the mouse's position
    mousey = 0 #Sets a placeholder variable for the y-coordinate of the mouse's position
    page = 1
    
    fancyfontPage = assets.page_font.render("Page: " + str(page) + "/6", True, (240,240,240)) 
    textRectObjPage = fancyfontPage.get_rect()
    textRectObjPage.center  = (pg_text_x,pg_text_y)
    
    fancyfontHelp = assets.page_font.render("Help", True, (240,240,240)) 
    textRectObjHelp = fancyfontHelp.get_rect()
    textRectObjHelp.center  = (help_text_x,help_text_y)
    
    game = True #Sets a condition for the game to run on and the game will only exit when the user chooses to do so
    while game == True:  #Runs the game loop until the user quits     
        mouseClicked = False #Creates a condition for the mouse. "False" means the mouse is not being clicked
                       
        for event in pygame.event.get(): #Imports a module from the python library
            if event.type == pygame.QUIT: # if user quits close program
                pygame.quit() #Calls upon the quit function from the pygame library
                sys.exit()    #Exits the game          
            elif event.type == pygame.MOUSEMOTION: # gets location of mouse if it moves
                mousex, mousey = event.pos #Creates a location in the style of a tuple depending on where the mouse is on the screen
 
            elif event.type == pygame.MOUSEBUTTONUP: # check if mouse pressed and gets location
                mousex, mousey = event.pos #Creates a location in the style of a tuple depending on where the mouse is on the screen
                mouseClicked = True   #Creates a condition for the mouse. "True" means the mouse is being clicked
                
        cfg.window.blit(assets.background_image2,(0,0)) # draw the black background onto the surface
                
        if backButton.rect.collidepoint(mousex, mousey): # Highlights Button and if clicked ends loop and return Sprites
            if mouseClicked == True: #Creates a condition if the user chooses to exit
                game = False #Ends the Options menu loop
                
            
               
            else:
                backButton.HighlightManual(assets.back_image_highlight) #If the mouse is over the button but not clicking the button, the button will highlight so the user knows they are accessing the button
        if arrowRButton.rect.collidepoint(mousex, mousey) and mouseClicked == True:
            page += 1 
            if page > 6:# if Right Arrow Clicked increase Lives , Maximum is 99
                page = 6
            fancyfontPage = assets.page_font.render("Page: " + str(page) + "/6", True, (240,240,240)) 
            textRectObjPage = fancyfontPage.get_rect()
            textRectObjPage.center  = (pg_text_x,pg_text_y)
        elif arrowLButton.rect.collidepoint(mousex, mousey) and mouseClicked == True:
            page -= 1
            if page < 1:# if Right Arrow Clicked Decrease Lives , Minimum is 1
                page = 1
        
            fancyfontPage = assets.page_font.render("Page: " + str(page) + "/6", True, (240,240,240)) 
            textRectObjPage = fancyfontPage.get_rect()
            textRectObjPage.center  = (pg_text_x,pg_text_y)
            
        #Draws all images to screen
        backButton.Display(cfg.window) #Draws the back button to the screen
        arrowRButton.Display(cfg.window)
        arrowLButton.Display(cfg.window)
        cfg.window.blit(fancyfontPage,textRectObjPage)
        cfg.window.blit(fancyfontHelp,textRectObjHelp)
        cfg.window.blit(help_text[page - 1],(cfg.width/2 - (pygame.Surface.get_width(help_text[page - 1])/2), cfg.height/40 * 21 - (pygame.Surface.get_height(help_text[page - 1])/2)))
        
        # draw the window onto the screen
        pygame.display.flip() #Updates the onscreen image
        cfg.clock.tick(30) #Sets a speed for the game to run at
    return 
