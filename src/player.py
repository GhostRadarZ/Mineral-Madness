import pygame, random

class Human(object):
    def __init__(self, keyboard, joystick, character):
        self.keyboard = keyboard
        self.joystick = joystick
        self.character = character
    
    def updateInputs(self):
        keys = pygame.key.get_pressed()

        try:
            if keys[self.keyboard[0]]:
                up = True
            else:
                up = False

            if keys[self.keyboard[1]]:
                down = True
            else:
                down = False

            if keys[self.keyboard[2]]:
                left = True
            else:
                left = False
            
            if keys[self.keyboard[3]]:
                right = True
            else:
                right = False

            if keys[self.keyboard[4]]:
                upatk = True
            else:
                upatk = False

            if keys[self.keyboard[5]]:
                downatk = True
            else:
                downatk = False

            if keys[self.keyboard[6]]:
                leftatk = True
            else:
                leftatk = False

            if keys[self.keyboard[7]]:
                rightatk = True
            else:
                rightatk = False
            
            # Keyboard controls doesn't have a neutral attack button, so always set this to false
            neutralatk = False
        
        # If keyboard is None, then set all inputs to false (this shouldn't happen)
        except AttributeError:
            up = False
            down = False
            left = False
            right = False
            upatk = False
            downatk = False
            leftatk = False
            rightatk = False
            neutralatk = False
        
        try:

            #
            # GameCube Controller control scheme (m4sv's driver)
            #

            if self.joystick.get_name() == '8 axis 8 button device':

                # Check if A is being pressed
                a = self.joystick.get_button(0)

                # Check if B is being pressed
                b = self.joystick.get_button(1)

                # Check if X is being pressed
                x = self.joystick.get_button(2)

                # Check if Y is being pressed
                y = self.joystick.get_button(3)

                # Grab the position of the left stick
                ls_x = self.joystick.get_axis(0)
                ls_y = self.joystick.get_axis(1)

                # Grab the position of the right stick
                rs_x = self.joystick.get_axis(5)
                rs_y = self.joystick.get_axis(4)        
            
            #
            # Xbox Controller control scheme
            #

            elif self.joystick.get_name() == 'Controller (Xbox One For Windows)':

                # Check if A is being pressed
                a = self.joystick.get_button(0)

                # Check if B is being pressed
                b = self.joystick.get_button(1)

                # Check if X is being pressed
                x = self.joystick.get_button(2)

                # Check if Y is being pressed
                y = self.joystick.get_button(3)

                # Grab the position of the left stick
                ls_x = self.joystick.get_axis(0)
                ls_y = self.joystick.get_axis(1)

                # Grab the position of the right stick
                rs_x = self.joystick.get_axis(4)
                rs_y = self.joystick.get_axis(3)

            #
            # Official Nintendo Switch Pro Controller control scheme
            #

            elif self.joystick.get_name() == 'Pro Controller':

                # Check if A is being pressed
                a = self.joystick.get_button(1)

                # Check if B is being pressed
                b = self.joystick.get_button(0)

                # Check if X is being pressed
                x = self.joystick.get_button(3)

                # Check if Y is being pressed
                y = self.joystick.get_button(2)

                # Grab the position of the left stick
                ls_x = self.joystick.get_axis(0)
                ls_y = self.joystick.get_axis(1)

                # Grab the position of the right stick
                rs_x = self.joystick.get_axis(2)
                rs_y = self.joystick.get_axis(3)
            
            #
            # PDP Switch Pro Controller control scheme
            #
            
            elif self.joystick.get_name() == 'Faceoff Deluxe Wired Pro Controller for Nintendo Switch':
                
                # Check if A is being pressed
                a = self.joystick.get_button(2)

                # Check if B is being pressed
                b = self.joystick.get_button(1)

                # Check if X is being pressed
                x = self.joystick.get_button(3)

                # Check if Y is being pressed
                y = self.joystick.get_button(0)

                # Grab the position of the left stick
                ls_x = self.joystick.get_axis(0)
                ls_y = self.joystick.get_axis(1)

                # Grab the position of the right stick
                rs_x = self.joystick.get_axis(2)
                rs_y = self.joystick.get_axis(3)
            
            # If X or Y is being pressed, then send an up input (jump)
            if x or y:
                up = True
            
            # If the left stick is tilted down, send a down input (fall)
            if ls_y > 0.8:
                down = True
            
            # If the left stick is tilted left, send a left input
            if ls_x < -0.5:
                left = True

            # If the left stick is tilted right, send a right input
            if ls_x > 0.5:
                right = True
            
            # If A or B is being pressed and an up input is being registered, or if the right stick is being tilted up, then send an upatk input
            if (a or b) and ls_y < -0.8 or rs_y < -0.8:
                upatk = True
            
            # If A or B is being pressed and a down input is already registered, or if the right stick is being tilted down, then send a downatk input
            if (a or b) and ls_y > 0.8 or rs_y > 0.8:
                downatk = True
            
            # If A or B is being pressed and a left input is already registered, or if the right stick is being tilted left, then send an leftatk input
            if (a or b) and ls_x < -0.5 or rs_x < -0.5:
                leftatk = True
            
            # If A or B is being pressed and a right input is already registered, or if the right stick is being tilted right, then send an rightatk input
            if (a or b) and ls_x > 0.5 or rs_x > 0.5:
                rightatk = True
            
            # If A or B is being pressed without any left stick inputs, then send a neutralatk input
            if (a or b) and -0.5 < ls_x < 0.5 and -0.8 < ls_y < 0.8:
                neutralatk = True
        
        # If the joystick's controls can't be read properly, then pass
        except pygame.error:
            pass
    
        # If the joystick is None, then pass
        except AttributeError:
            pass
        
        self.inputs = [up, down, left, right, upatk, downatk, leftatk, rightatk, neutralatk]

        # After detecting the inputs, pass the inputs to their character
        self.character.parseInputs(self.inputs)
        

class Bot(object):
    def __init__(self, character, difficulty):
        self.character = character
        self.difficulty = difficulty
        self.jumpcooldown = 10
        self.atkcooldown = 10
        self.fastfallcooldown = 60
        
        self.adjustments = BotDebuff()

        self.character_length = self.character.hurtbox.width
        self.character_height = self.character.hurtbox.height

        # Attack ranges for each of Pebble's attacks
        if self.character.__class__.__name__ == 'Pebble':
            self.prime_range_x = 60
            self.prime_range_y = 10
            self.f_smash_range = 80
            self.f_air_range = 25
            self.up_air_range = 50
            self.down_air_range = 90
        
        # Attack ranges for each of Crystal's attacks
        elif self.character.__class__.__name__ == 'Crystal':
            self.prime_range_x = 50
            self.prime_range_y = 30
            self.f_smash_range = 80
            self.f_air_range = 80
            self.up_air_range = 50
            self.down_air_range = 90
            
        # Attack ranges for each of Magma's attacks
        elif self.character.__class__.__name__ == 'Magma':
            self.prime_range_x = 50
            self.prime_range_y = 40
            self.f_smash_range = 700
            self.f_air_range = 700
            self.up_air_range = 50
            self.down_air_range = 130
            self.projectilecooldown = 200
            self.down_smash_range = 200
        
        # Attack ranges for each of Pharaoh's attacks
        elif self.character.__class__.__name__ == 'Pharaoh':
            self.prime_range_x = 180
            self.prime_range_y = 40
            self.f_smash_range = 250
            self.f_air_range = 250
            self.up_air_range = 50
            self.down_air_range = 70
            self.projectilecooldown = 30
            
        # safety net for now
        else:
            self.prime_range_x = 50
            self.prime_range_y = 40
            self.f_smash_range = 60
            self.f_air_range = 25
            self.up_air_range = 50
            self.down_air_range = 90
    
    def doJump(self):
        #if bot has no jumps it stops trying to jump until it hits the ground
        if self.character.jumps == 0:
            up = False      
        #delays the bot's jump for 10 frames   
        elif self.jumpcooldown > 0:
            self.jumpcooldown -= 1
            up = False
        #makes bot jump and resets the jump cooldown
        elif self.jumpcooldown == 0:
            up = True
            self.jumpcooldown = 10
        #does not jump
        else:
            up = False
        
        return up
    
    def ravineSD(self, entities, stage, target):
        character_mid = self.character.x + (self.character_length / 2)
        up = self.inputs[0]
        down = self.inputs[1]
        left = self.inputs[2]
        right = self.inputs[3]
        upatk = self.inputs[4]
        downatk = self.inputs[5]
        leftatk = self.inputs[6]
        rightatk = self.inputs[7]
        
        self.left_edge = 50
        self.right_edge = 730
        
        if character_mid < (self.left_edge + 30):
            left = False
            
        if character_mid > (self.right_edge - 30):
            right = False
        
        # Don't attack when offstage
        if character_mid < self.left_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        elif character_mid > self.right_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
            
        return [up, down, left, right, upatk, downatk, leftatk, rightatk]
        
    def crystalCoveSD(self, entities, stage, target):
        character_mid = self.character.x + (self.character_length / 2)
        
        up = self.inputs[0]
        down = self.inputs[1]
        left = self.inputs[2]
        right = self.inputs[3]
        upatk = self.inputs[4]
        downatk = self.inputs[5]
        leftatk = self.inputs[6]
        rightatk = self.inputs[7]
        
        self.left_edge = 50
        self.right_edge = 750
        self.gap_left = 300
        self.gap_right = 500
        self.gap_mid = 400
        
        if character_mid < (self.left_edge + 20):
            left = False
            
        if character_mid > (self.right_edge - 20):
            right = False
        
        # Don't attack when offstage
        if character_mid < self.left_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        elif character_mid > self.right_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        
        # If the bot is below the transparent platform
        if self.character.y > 500 - self.character_height:
        # If the bot is in the middle of the gap
            if character_mid < self.gap_right and character_mid > self.gap_left:
                # Don't attack in the pit
                upatk = False 
                downatk = False
                leftatk = False
                rightatk = False
                down = False
                
                #bot tries to jump out the pit
                up = self.doJump()
                # Go to the left if the player is on the left side
                if target.x < self.gap_mid:
                    left = True
                    right = False
                # Go to the right if the player is on the right side
                elif target.x > self.gap_mid:
                    right = True
                    left = False
                else:
                    upatk = True
                
        else:
            pass
        
        return [up, down, left, right, upatk, downatk, leftatk, rightatk]
        
    def rumbleVocanoSD(self, entities, stage, target):
        character_mid = self.character.x + (self.character_length / 2)

        up = self.inputs[0]
        down = self.inputs[1]
        left = self.inputs[2]
        right = self.inputs[3]
        upatk = self.inputs[4]
        downatk = self.inputs[5]
        leftatk = self.inputs[6]
        rightatk = self.inputs[7]
        
        self.left_edge = 50
        self.right_edge = 750
        
        if character_mid < (self.left_edge + 20):
            left = False
            
        if character_mid > (self.right_edge - 20):
            right = False
        
        # Don't attack when offstage
        if character_mid < self.left_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        elif character_mid > self.right_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        
        return [up, down, left, right, upatk, downatk, leftatk, rightatk]
    
    def templeSD(self, entities, stage, target):
        character_mid = self.character.x + (self.character_length / 2)
      
        up = self.inputs[0]
        down = self.inputs[1]
        left = self.inputs[2]
        right = self.inputs[3]
        upatk = self.inputs[4]
        downatk = self.inputs[5]
        leftatk = self.inputs[6]
        rightatk = self.inputs[7]
      
        self.left_edge = -50
        self.right_edge = 850
        self.bridge_left = 150
        self.bridge_right = 650
        
        if character_mid < (self.left_edge + 30):
            left = False
            
        if character_mid > (self.right_edge - 30):
            right = False
        
        # Don't attack when offstage
        if character_mid < self.left_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        elif character_mid > self.right_edge:
            upatk = False 
            downatk = False
            leftatk = False
            rightatk = False
        
        # Don't let the bot fall through the sides of the map
        if self.character.y > (525 - self.character_height):
            if character_mid < (self.bridge_left + 20) or character_mid > (self.bridge_right - 20):
                down = False
    
        return [up, down, left, right, upatk, downatk, leftatk, rightatk]
    
    
    def sdProof(self, entities, stage, target):
        stage
        
        if stage == 0:
            movement = self.ravineSD(entities, stage, target)
        elif stage == 1:
            movement = self.crystalCoveSD(entities, stage, target)
        elif stage == 2:
            movement = self.rumbleVocanoSD(entities, stage, target)
        elif stage == 3:
            movement = self.templeSD(entities, stage, target)
        else:
            pass
            
        return movement
    
    def randomJump(self):
        chance = random.randint(0, 100)
        
        if chance > 50:
            jump = True
        else:
            jump = False
        
        return jump
    
    def pebbleMovement(self, entities, target):
        character_mid = self.character.x + (self.character_length / 2)
        #print('bot mid ' + str(character_mid))
        
        down = False

        # Reset attacks
        leftatk = False
        rightatk = False
        upatk = False
        downatk = False
    
        #makes bot jump if player is above it and resets the jump cooldown
        if self.character.y > target.y + self.prime_range_y:
            up = self.doJump()
        #does not jump
        else:
            up = False
        
        #bot fast falls to reach player
        if self.character.y < (target.y - self.prime_range_y):
            if self.fastfallcooldown > 0:
                self.fastfallcooldown -= 1
                down = False
            #makes bot jump and resets the jump cooldown
            elif self.fastfallcooldown <= 0:
                down = True
            elif self.fastfallcooldown == -4:
                down = True
                self.fastfallcooldown = 60
            #does not jump
            else:
                up = False  
        
        #bot moves to the right if the player is on the right of it
        if character_mid < (target.x - self.prime_range_x):
            right = True
            if up == False:
                # 1 in 2 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            right = False
            
        #bot moves to the left if the player is on the left of it
        if character_mid > (target.x + self.prime_range_x):
            left = True
            if up == False:
                # 1 in 100 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            left = False
        
        #Use ground attacks if bot is on the ground 
        if self.character.airbourne == False:

            #space between player and bot x axis
            dif_x = target.x - character_mid
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #print(str(dif_x))
            
            if character_mid > target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        leftatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        leftatk = True
                    else:
                        pass
            elif character_mid < target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y + self.prime_range_y: #player is above bot
                leftatk = False
                rightatk = False
                upatk = False
            else:
                #bot uses up smash if player is too close to bot (literally inside it)
                if (target.x > character_mid and target.x < (self.character.x + self.character_length)) or (target.x < character_mid and target.x > (self.character.x - self.character_length)): #player is inside of the bot
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                        leftatk = False
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
                        leftatk = False
                        rightatk = False
                    else:
                        pass
        
        #Do airial attacks if bot is airbourne
        if self.character.airbourne == True:
            #print('Airials')
            leftatk = False
            rightatk = False
            upatk = False
            downatk = False
            
            #space between player and bot x axis
            dif_x = target.x - self.character.x
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #space between player and bot y axis
            dif_y = target.y - self.character.y
            if dif_y < 0:
                dif_y = dif_y * (-1) #absolute value
            
            #dif = target.x - self.character.x
            #print(str(dif))
            
            if self.character.x > target.x:
                if dif_x < self.f_air_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        leftatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        leftatk = True
                    else:
                        pass
            elif self.character.x < target.x:
                if dif_x < self.f_air_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y: #player is above bot
                #print('its coming')
                if dif_y < self.up_air_range:
                    #print('YAAAAAAAAAAAAASSSSSSSSSSSSSSS QUEEEEEEEEEEEEEEEEEEEN')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
            
            if self.character.y < target.y: #player is below bot
                #print('its kinda coming')
                if dif_y < self.down_air_range:
                    #print('nooooooooooooooooooooo QUEEEEEEEEEEEEEEEEEEEN')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        downatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        downatk = True
        
            
        #if leftatk or rightatk == True:
            #print('F AIR')
            
        #if upatk == True:
            #print('UP AIR')
                
        #if downatk == True:
            #print('D AIR')
                
        # Disable movement during attacks
        #if upatk == True or downatk == True or leftatk == True or rightatk == True:
        #   up = False
        #    down = False
        #    left = False
        #    right = False
            
        # Update the inputs
        self.inputs = [up, down, left, right, upatk, downatk, leftatk, rightatk]
        
    
    def crystalMovement(self, entities, target):
        character_mid = self.character.x + (self.character_length / 2)
        #print('bot mid ' + str(character_mid))
        
        down = False
        
        # Reset attacks
        leftatk = False
        rightatk = False
        upatk = False
        downatk = False
    
        #makes bot jump if player is above it and resets the jump cooldown
        if self.character.y > target.y + self.prime_range_y:
            up = self.doJump()
        #does not jump
        else:
            up = False
        
        #bot fast falls to reach player
        if self.character.y < (target.y - self.prime_range_y):
            if self.fastfallcooldown > 0:
                self.fastfallcooldown -= 1
                down = False
            #makes bot jump and resets the jump cooldown
            elif self.fastfallcooldown <= 0:
                down = True
            elif self.fastfallcooldown == -4:
                down = True
                self.fastfallcooldown = 60
            #does not jump
            else:
                up = False 
        
        #bot moves to the right if the player is on the right of it
        if character_mid < (target.x - self.prime_range_x):
            right = True
            if up == False:
                # 1 in 2 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            right = False
            
        #bot moves to the left if the player is on the left of it
        if character_mid > (target.x + self.prime_range_x):
            left = True
            if up == False:
                # 1 in 100 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            left = False
        
        #Use ground attacks if bot is on the ground 
        if self.character.airbourne == False:

            #space between player and bot x axis
            dif_x = target.x - character_mid
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #print(str(dif_x))
            
            if character_mid > target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        leftatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        leftatk = True
                    else:
                        pass
            elif character_mid < target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y + self.prime_range_y: #player is above bot
                leftatk = False
                rightatk = False
                upatk = False
            else:
                #bot uses up smash if player is too close to bot (literally inside it)
                if (target.x > character_mid and target.x < (self.character.x + self.character_length)) or (target.x < character_mid and target.x > (self.character.x - self.character_length)): #player is inside of the bot
                    if target.y < self.character.y:
                        if self.atkcooldown > 0:
                            self.atkcooldown -= 1
                            upatk = False
                            leftatk = False
                            rightatk = False
                        elif self.atkcooldown == 0:
                            self.atkcooldown = 10
                            upatk = True
                            leftatk = False
                            rightatk = False
                        else:
                            pass
        
        #Do airial attacks if bot is airbourne
        if self.character.airbourne == True:
            #print('Airials')
            leftatk = False
            rightatk = False
            upatk = False
            downatk = False
            
            #space between player and bot x axis
            dif_x = target.x - self.character.x
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #space between player and bot y axis
            dif_y = target.y - self.character.y
            if dif_y < 0:
                dif_y = dif_y * (-1) #absolute value
            
            #dif = target.x - self.character.x
            #print(str(dif))
            
            if self.character.x > target.x:
                if dif_x < self.f_air_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        leftatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        leftatk = True
                    else:
                        pass
            elif self.character.x < target.x:
                if dif_x < self.f_air_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y: #player is above bot
                #print('its coming')
                if dif_y < self.up_air_range:
                    #print('YAAAAAAAAAAAAASSSSSSSSSSSSSSS QUEEEEEEEEEEEEEEEEEEEN')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
            
            if self.character.y < target.y: #player is below bot
                #print('its kinda coming')
                if dif_y < self.down_air_range:
                    #print('nooooooooooooooooooooo QUEEEEEEEEEEEEEEEEEEEN')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        downatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        downatk = True
            
        # Update the inputs
        self.inputs = [up, down, left, right, upatk, downatk, leftatk, rightatk]
         
          
    def magmaMovement(self, entities, target):
        character_mid = self.character.x + (self.character_length / 2)
        #print('bot mid ' + str(character_mid))
        
        down = False
        
        # Reset attacks
        leftatk = False
        rightatk = False
        upatk = False
        downatk = False
    
        #makes bot jump if player is above it and resets the jump cooldown
        if self.character.y > target.y + self.prime_range_y:
            up = self.doJump()
        #does not jump
        else:
            up = False
        
        #bot fast falls to reach player
        if self.character.y < (target.y - self.prime_range_y):
            if self.fastfallcooldown > 0:
                self.fastfallcooldown -= 1
                down = False
            #makes bot jump and resets the jump cooldown
            elif self.fastfallcooldown <= 0:
                down = True
            elif self.fastfallcooldown == -4:
                down = True
                self.fastfallcooldown = 60
            #does not jump
            else:
                up = False 
                
        #bot moves to the right if the player is on the right of it
        if character_mid < (target.x - self.prime_range_x):
            right = True
            if up == False:
                # 1 in 2 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            right = False
            
        #bot moves to the left if the player is on the left of it
        if character_mid > (target.x + self.prime_range_x):
            left = True
            if up == False:
                # 1 in 100 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            left = False
        
        #Use ground attacks if bot is on the ground 
        if self.character.airbourne == False:

            #space between player and bot x axis
            dif_x = target.x - character_mid
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #print(str(dif_x))
            
            if character_mid > target.x:
                #print('ok')
                if dif_x < self.down_smash_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        downatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        downatk = True
                    else:
                        pass
                elif dif_x < self.f_smash_range:
                    #print('better')
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        leftatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 200
                        leftatk = True
                    else:
                        pass
                    
            elif character_mid < target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        rightatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 90
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y + self.prime_range_y: #player is above bot
                leftatk = False
                rightatk = False
                upatk = False
            else:
                #bot uses up smash if player is too close to bot (literally inside it)
                if (target.x > character_mid and target.x < (self.character.x + self.character_length)) or (target.x < character_mid and target.x > (self.character.x - self.character_length)): #player is inside of the bot
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                        leftatk = False
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
                        leftatk = False
                        rightatk = False
                    else:
                        pass
        
        #Do airial attacks if bot is airbourne
        if self.character.airbourne == True:
            #print('Airials')
            leftatk = False
            rightatk = False
            upatk = False
            downatk = False
            
            #space between player and bot x axis
            dif_x = target.x - self.character.x
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #space between player and bot y axis
            dif_y = target.y - self.character.y
            if dif_y < 0:
                dif_y = dif_y * (-1) #absolute value
            
            #dif = target.x - self.character.x
            #print(str(dif))
            
            if self.character.x > target.x:
                if dif_x < self.f_air_range:
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        leftatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 200
                        leftatk = True
                    else:
                        pass
            elif self.character.x < target.x:
                if dif_x < self.f_air_range:
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        rightatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 200
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y: #player is above bot
                if dif_y < self.up_air_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
            
            if self.character.y < target.y: #player is below bot
                if dif_y < self.down_air_range:
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        downatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        downatk = True
            
        #if leftatk or rightatk == True:
            #print('F AIR')
            
        #if upatk == True:
            #print('UP AIR')
                
        #if downatk == True:
            #print('D AIR')
                
        # Disable movement during attacks
        #if upatk == True or downatk == True or leftatk == True or rightatk == True:
        #    up = False
        #    down = False
        #    left = False
        #    right = False
            
        # Update the inputs
        self.inputs = [up, down, left, right, upatk, downatk, leftatk, rightatk]
         
        
    def pharaohMovement(self, entities, target):
        character_mid = self.character.x + (self.character_length / 2)
        #print('bot mid ' + str(character_mid))
        
        down = False
        
        # Reset attacks
        leftatk = False
        rightatk = False
        upatk = False
        downatk = False
    
        #makes bot jump if player is above it and resets the jump cooldown
        if self.character.y > target.y + self.prime_range_y:
            up = self.doJump()
        #does not jump
        else:
            up = False
        
        #bot fast falls to reach player
        if self.character.y < (target.y - self.prime_range_y):
            if self.fastfallcooldown > 0:
                self.fastfallcooldown -= 1
                down = False
            #makes bot jump and resets the jump cooldown
            elif self.fastfallcooldown <= 0:
                down = True
            elif self.fastfallcooldown == -4:
                down = True
                self.fastfallcooldown = 60
            #does not jump
            else:
                up = False 
        
        #bot moves to the right if the player is on the right of it
        if character_mid < (target.x - self.prime_range_x):
            right = True
            if up == False:
                # 1 in 2 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            right = False
            
        #bot moves to the left if the player is on the left of it
        if character_mid > (target.x + self.prime_range_x):
            left = True
            if up == False:
                # 1 in 100 chance of jumping to get out of conflict
                up = self.randomJump()
        else:
            left = False
        
        #Use ground attacks if bot is on the ground 
        if self.character.airbourne == False:

            #space between player and bot x axis
            dif_x = target.x - character_mid
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #print(str(dif_x))
            
            if character_mid > target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        leftatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 20
                        leftatk = True
                    else:
                        pass
            elif character_mid < target.x:
                #print('ok')
                if dif_x < self.f_smash_range:
                    #print('better')
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        rightatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 20
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y + self.prime_range_y: #player is above bot
                leftatk = False
                rightatk = False
                upatk = False
            else:
                #bot uses up smash if player is too close to bot (literally inside it)
                if (target.x > character_mid and target.x < (self.character.x + self.character_length)) or (target.x < character_mid and target.x > (self.character.x - self.character_length)): #player is inside of the bot
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                        leftatk = False
                        rightatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
                        leftatk = False
                        rightatk = False
                    else:
                        pass
        
        #Do airial attacks if bot is airbourne
        if self.character.airbourne == True:
            #print('Airials')
            
            #space between player and bot x axis
            dif_x = target.x - self.character.x
            if dif_x < 0:
                dif_x = dif_x * (-1) #absolute value
            
            #space between player and bot y axis 
            dif_y = target.y - self.character.y
            if dif_y < 0:
                dif_y = dif_y * (-1) #absolute value
            
            #dif = target.x - self.character.x
            #print(str(dif))
            
            if self.character.x > target.x:
                if dif_x < self.f_air_range:
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        leftatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 20
                        leftatk = True
                    else:
                        pass
            elif self.character.x < target.x:
                if dif_x < self.f_air_range:
                    if self.projectilecooldown > 0:
                        self.projectilecooldown -= 1
                        rightatk = False
                    elif self.projectilecooldown == 0:
                        self.projectilecooldown = 20
                        rightatk = True
                    else:
                        pass
            
            if self.character.y > target.y: #player is above bot
                #print('its coming')
                if dif_y < self.up_air_range:
                    #print('YAAAAAAAAAAAAASSSSSSSSSSSSSSS QUEEEEEEEEEEEEEEEEEEEN')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        upatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        upatk = True
            
            if self.character.y < target.y: #player is below bot
                #print('its kinda coming')
                if dif_y < self.down_air_range:
                    #print('nooooooooooooooooooooo QUEEEEEEEEEEEEEEEEEEEN')
                    if self.atkcooldown > 0:
                        self.atkcooldown -= 1
                        downatk = False
                    elif self.atkcooldown == 0:
                        self.atkcooldown = 10
                        downatk = True
            
        #if leftatk or rightatk == True:
            #print('F AIR')
            
        #if upatk == True:
            #print('UP AIR')
                
        #if downatk == True:
            #print('D AIR')
                
        # Disable movement during attacks
        #if upatk == True or downatk == True or leftatk == True or rightatk == True:
        #    up = False
        #    down = False
        #    left = False
        #    right = False
            
        # Update the inputs
        self.inputs = [up, down, left, right, upatk, downatk, leftatk, rightatk]
         
     
    
    def updateInputs(self, entities, stage):
        for entity in entities:
            if entity is not self.character:
                target = entity
        
        self.stage = stage
        
        # Reset all movement options
        up = False
        down = False
        left = False
        right = False
        upatk = False
        downatk = False
        leftatk = False
        rightatk = False
        
        self.inputs = (up, down, left, right, upatk, downatk, leftatk, rightatk)

        # Declare which character the bot is playing as and use moves according to that character
        if self.character.__class__.__name__ == 'Pebble':
            self.pebbleMovement(entities, target)
            self.inputs = self.sdProof(entities, stage, target)
        if self.character.__class__.__name__ == 'Crystal':
            self.crystalMovement(entities, target)
            self.inputs = self.sdProof(entities, stage, target)
        if self.character.__class__.__name__ == 'Magma':
            self.magmaMovement(entities, target)
            self.inputs = self.sdProof(entities, stage, target)
        if self.character.__class__.__name__ == 'Pharaoh':
            self.pharaohMovement(entities, target)
            self.inputs = self.sdProof(entities, stage, target)
        
        self.inputs = self.sdProof(entities, stage, target)
        
        
        if self.difficulty == 1:
            self.inputs = self.adjustments.slowerMovement(self.inputs)
        #print(x_difference)
        #print(leftatk)
        #print(rightatk)
        #print(str(movement))
        #print(str(self.character.jumps))
        #print(str(target.y))
        #print('target' + str(target.x))
        #print(str(self.character.y))
        #print('bot ' + str(self.character.x))

        neutralatk = False
        self.inputs.append(neutralatk)

        # After detecting the inputs, pass the inputs to their character
        self.character.parseInputs(self.inputs)
        
class BotDebuff(object):
    def __init__(self):
        self.move_left = [0,0,0,0,0,0,0,0,0,0]
        self.move_right = [0,0,0,0,0,0,0,0,0,0]
        self.jump = [0,0,0,0,0,0,0,0,0,0]
        self.atkup = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.atkdown = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.atklft = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.atkrgt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def slowerMovement(self,inputs):
        self.up = inputs[1]
        self.left = inputs[2]
        self.right = inputs[3]
        self.upatk = inputs[4]
        self.downatk = inputs[5]
        self.leftatk = inputs[6]
        self.rightatk = inputs[7]
        
        self.jump.append(self.up)
        self.up = self.jump.pop(0)
        
        self.move_left.append(self.left)
        self.left = self.move_left.pop(0)
        
        self.move_right.append(self.right)
        self.right = self.move_right.pop(0)
        
        self.atkup.append(self.upatk)
        self.upatk = self.atkup.pop(0)
        
        self.atkdown.append(self.downatk)
        self.downatk = self.atkdown.pop(0)
        
        self.atklft.append(self.leftatk)
        self.leftatk = self.atklft.pop(0)
        
        self.atkrgt.append(self.rightatk)
        self.rightatk = self.atkrgt.pop(0)
        
        inputs[1] = self.up 
        inputs[2] = self.left
        inputs[3] = self.right
        inputs[4] = self.upatk
        inputs[5] = self.downatk
        inputs[6]  = self.leftatk
        inputs[7] = self.rightatk
        

        return inputs

        
    
    