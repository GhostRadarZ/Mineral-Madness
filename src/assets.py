import pygame, os, cfg

background_image1 = pygame.image.load(os.path.join(cfg.menu_dir,'main_menu.png')).convert_alpha()
background_image2 = pygame.image.load(os.path.join(cfg.menu_dir,'alternate_menu_background.png')).convert_alpha()
start_image = pygame.image.load(os.path.join(cfg.menu_dir,'start_game.png')).convert_alpha()
start_image_highlight = pygame.image.load(os.path.join(cfg.menu_dir,'start_game_highlight.png')).convert_alpha()
Mineral_Maddness_image =pygame.image.load(os.path.join(cfg.menu_dir,'title.png')).convert_alpha()
mode_menu =  pygame.image.load(os.path.join(cfg.menu_dir,'mode_select.png')).convert_alpha()
mode_1_highlight = pygame.image.load(os.path.join(cfg.menu_dir,'1_player_highlight.png')).convert_alpha()
mode_2_highlight = pygame.image.load(os.path.join(cfg.menu_dir,'2_player_highlight.png')).convert_alpha()
mode_1_player = pygame.image.load(os.path.join(cfg.menu_dir,'1_player.png')).convert_alpha()
mode_2_player = pygame.image.load(os.path.join(cfg.menu_dir,'2_player.png')).convert_alpha()
options_image = pygame.image.load(os.path.join(cfg.menu_dir,'options.png')).convert_alpha()
options_highlight_image = pygame.image.load(os.path.join(cfg.menu_dir,'options_highlight.png')).convert_alpha()
back_image = pygame.image.load(os.path.join(cfg.menu_dir,'back_image.png')).convert_alpha()
back_image_highlight = pygame.image.load(os.path.join(cfg.menu_dir,'back_image_highlight.png')).convert_alpha()
exit_game_image = pygame.image.load(os.path.join(cfg.menu_dir,'exit_game_image.png')).convert_alpha()
exit_game_image_highlight = pygame.image.load(os.path.join(cfg.menu_dir,'exit_game_highlight.png')).convert_alpha()
return_to_title_image = pygame.image.load(os.path.join(cfg.menu_dir,'return_to_title.png')).convert_alpha()
return_to_title_highlight_image = pygame.image.load(os.path.join(cfg.menu_dir,'return_to_title_highlight.png')).convert_alpha()
stage_select_image =pygame.image.load(os.path.join(cfg.menu_dir,'stage_select.png')).convert_alpha()
character_selector_image = pygame.image.load(os.path.join(cfg.menu_dir,'N_Select.png')).convert_alpha()
character_selectorP2 = pygame.image.load(os.path.join(cfg.menu_dir,'P1_Select.png')).convert_alpha()
character_selectorP1 = pygame.image.load(os.path.join(cfg.menu_dir,'P2_Select.png')).convert_alpha()
arrow_up = pygame.image.load(os.path.join(cfg.menu_dir,'arrow_up.png')).convert_alpha()
arrow_down = pygame.image.load(os.path.join(cfg.menu_dir,'arrow_down.png')).convert_alpha()
arrow_left = pygame.image.load(os.path.join(cfg.menu_dir,'arrow_left.png')).convert_alpha()
arrow_right = pygame.image.load(os.path.join(cfg.menu_dir,'arrow_right.png')).convert_alpha()
character_select_image = pygame.image.load(os.path.join(cfg.menu_dir,'character_select.png')).convert_alpha()
lives_line_image = pygame.image.load(os.path.join(cfg.menu_dir,'lives_line.png')).convert_alpha()
exit_image = pygame.image.load(os.path.join(cfg.menu_dir, 'next.png')).convert_alpha()
exit_image_highlight = pygame.image.load(os.path.join(cfg.menu_dir, 'next_highlight.png')).convert_alpha()
player_controls = pygame.image.load(os.path.join(cfg.menu_dir,'player_controls.png')).convert_alpha() #Loads the diagram of the first players controls                              
sound_on_button = pygame.image.load(os.path.join(cfg.menu_dir,'sound_on_button.png')) .convert_alpha()                        
sound_off_button = pygame.image.load(os.path.join(cfg.menu_dir,'sound_off_button.png')).convert_alpha()
next_image = pygame.image.load(os.path.join(cfg.menu_dir, 'next.png')).convert_alpha()
next_image_highlight = pygame.image.load(os.path.join(cfg.menu_dir, 'next_highlight.png')).convert_alpha()
p1arrow = pygame.image.load(os.path.join(cfg.hud_dir, 'p1arrow.png')).convert_alpha()
p2arrow = pygame.image.load(os.path.join(cfg.hud_dir, 'p2arrow.png')).convert_alpha()
podium1_image = pygame.image.load(os.path.join(cfg.menu_dir, 'podium_1.png')).convert_alpha()
podium2_image = pygame.image.load(os.path.join(cfg.menu_dir, 'podium_2.png')).convert_alpha()
help_image = pygame.image.load(os.path.join(cfg.menu_dir, 'help.png')).convert_alpha()
help_highlight_image = pygame.image.load(os.path.join(cfg.menu_dir, 'help_highlight.png')).convert_alpha()

# Victory screen assets
podium_image_width = pygame.Surface.get_width(podium1_image)
podium_image_height = pygame.Surface.get_height(podium1_image)
podium1_image_scaled = pygame.transform.scale(podium1_image, (podium_image_width * 6, podium_image_height * 6))
podium2_image_scaled = pygame.transform.scale(podium2_image, (podium_image_width * 6, podium_image_height * 6))

# Options menu assets
player_controls_width = pygame.Surface.get_width(player_controls)
player_controls_height = pygame.Surface.get_height(player_controls)
player_controls_scaled = pygame.transform.scale(player_controls, (player_controls_width * 2, player_controls_height * 2))
sound_on_button_width = pygame.Surface.get_width(sound_on_button)
sound_on_button_height = pygame.Surface.get_height(sound_on_button)
sound_on_button_scaled = pygame.transform.scale(sound_on_button, (sound_on_button_width * 3, sound_on_button_height * 3))
sound_off_button_scaled = pygame.transform.scale(sound_off_button, (sound_on_button_width * 3, sound_on_button_height * 3))

arrow_width = pygame.Surface.get_width(arrow_left)
arrow_height = pygame.Surface.get_height(arrow_left)
arrow_left_scaled = pygame.transform.scale(arrow_left, (arrow_width * 2, arrow_height * 2))
arrow_right_scaled = pygame.transform.scale(arrow_right, (arrow_width * 2, arrow_height * 2))

# Stage assets
# Salty Rock Ravine
srr_bg = pygame.image.load(os.path.join(cfg.env_dir, 'lake_bg.png')).convert_alpha()
srr_pl_s = pygame.image.load(os.path.join(cfg.env_dir, 'grass-solid.png')).convert_alpha()
srr_pl_t = pygame.image.load(os.path.join(cfg.env_dir, 'grass-transparent.png')).convert_alpha()

# Crystal Cove
cc_bg = pygame.image.load(os.path.join(cfg.env_dir, 'crystal_bg.png')).convert_alpha()
cc_pl_s = pygame.image.load(os.path.join(cfg.env_dir, 'crystal-solid.png')).convert_alpha()
cc_pl_t = pygame.image.load(os.path.join(cfg.env_dir, 'crystal-transparent.png')).convert_alpha()

# Rumble Volcano
rv_bg = pygame.image.load(os.path.join(cfg.env_dir, 'volcano_bg.png')).convert_alpha()
rv_pl_s = pygame.image.load(os.path.join(cfg.env_dir, 'magma-solid.png')).convert_alpha()

# Ancient Temple
at_bg = pygame.image.load(os.path.join(cfg.env_dir, 'temple_bg.png')).convert_alpha()
at_pl_s = pygame.image.load(os.path.join(cfg.env_dir, 'brick-solid.png')).convert_alpha()
at_pl_t = pygame.image.load(os.path.join(cfg.env_dir, 'brick-transparent.png')).convert_alpha()

# HUD elements
banner1 = pygame.image.load(os.path.join(cfg.hud_dir, 'banner1.png'))
banner2 = pygame.image.load(os.path.join(cfg.hud_dir, 'banner2.png'))
pebble_head = pygame.image.load(os.path.join(cfg.hud_dir, 'pebble.png'))
pebble_head_scaled = pygame.transform.scale(pebble_head, (pygame.Surface.get_width(pebble_head) * 6, pygame.Surface.get_height(pebble_head) * 6))
crystal_head = pygame.image.load(os.path.join(cfg.hud_dir, 'crystal.png'))
crystal_head_scaled = pygame.transform.scale(crystal_head, (pygame.Surface.get_width(crystal_head) * 6, pygame.Surface.get_height(crystal_head) * 6))
magma_head = pygame.image.load(os.path.join(cfg.hud_dir, 'magma.png'))
magma_head_scaled = pygame.transform.scale(magma_head, (pygame.Surface.get_width(magma_head) * 6, pygame.Surface.get_height(magma_head) * 6))
pharaoh_head = pygame.image.load(os.path.join(cfg.hud_dir, 'pharaoh.png'))
pharaoh_head_scaled = pygame.transform.scale(pharaoh_head, (pygame.Surface.get_width(pharaoh_head) * 6, pygame.Surface.get_height(pharaoh_head) * 6))
p1arrow = pygame.image.load(os.path.join(cfg.hud_dir, 'p1arrow.png')).convert_alpha()
p2arrow = pygame.image.load(os.path.join(cfg.hud_dir, 'p2arrow.png')).convert_alpha()
arrow_width = pygame.Surface.get_width(p1arrow)
arrow_height = pygame.Surface.get_height(p1arrow)
p1arrow_scaled = pygame.transform.scale(p1arrow, (arrow_width * 2, arrow_height * 2))
p2arrow_scaled = pygame.transform.scale(p2arrow, (arrow_width * 2, arrow_height * 2))

#Load fonts
stage_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 64)
lives_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 72)
name_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 44)
sound_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 90)
result_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 90)
countdown_font = pygame.font.Font(os.path.join(cfg.font_dir, 'DCC - Ash.otf'), 200)
hud_lives_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 26)
hud_percent_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 60)
hud_name_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 36)
page_font = pygame.font.Font(os.path.join(cfg.font_dir,'DCC - Ash.otf'), 90)

part_blast = []

for file in sorted(os.listdir(cfg.particle_dir)):

    # Store the full path of the current file
    filepath = os.path.join(cfg.particle_dir, file)

    if file.endswith('.png'):
        # Upscale the animation frame by a factor of 4
        frame = pygame.image.load(filepath).convert_alpha()
        frame_width = pygame.Surface.get_width(frame)
        frame_height = pygame.Surface.get_height(frame)
        frame_scaled = pygame.transform.scale(frame, (frame_width * 4, frame_height * 4))

    # If it's an idle animation frame, add it to it's frame list
    if file.startswith('explosion') and file.endswith('.png'):
        # Override the scaling to 12x instead of 4x
        frame_scaled = pygame.transform.scale(frame, (frame_width * 12, frame_height * 12))
        part_blast.append(frame_scaled)

        
        
        