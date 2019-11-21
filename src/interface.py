import pygame, os, cfg, assets

def Display(characters):
    x_seg = cfg.width / (len(characters) + 1)

    for c in range(0, len(characters)):
        character = characters[c]

        if character.__class__.__name__ == 'Pebble':
            headimage = assets.pebble_head_scaled
        
        elif character.__class__.__name__ == 'Crystal':
            headimage = assets.crystal_head_scaled

        elif character.__class__.__name__ == 'Magma':
            headimage = assets.magma_head_scaled
        
        elif character.__class__.__name__ == 'Pharaoh':
            headimage = assets.pharaoh_head_scaled

        if c == 0:
            banner = assets.banner1
            arrow = assets.p1arrow
        
        else:
            banner = assets.banner2
            arrow = assets.p2arrow
        
        x = (c + 1) * x_seg
        y = 0.12 * cfg.height

        fancyfontlives = assets.hud_lives_font.render('x ' + (str(character.lives)), True, (240,240,240)) 
        textRectObjlives = fancyfontlives.get_rect()
        textRectObjlives.center  = (x + 40 - pygame.Surface.get_width(banner)/2, y + 45 - pygame.Surface.get_height(banner)/2)
        
        fancyfontname = assets.hud_name_font.render((str(character.__class__.__name__)), True, (240,240,240)) 
        textRectObjname = fancyfontname.get_rect()
        textRectObjname.center  = (x - 35 , y + 3)
        
        fancyfontpercent = assets.hud_percent_font.render((str(character.damage) + '%'), True, (240,240,240)) 
        textRectObjpercent = fancyfontpercent.get_rect()
        textRectObjpercent.center  = (x + 35 , y - 35)
        
        cfg.window.blit(arrow, (character.hurtbox.centerx - pygame.Surface.get_width(arrow) / 2, character.hurtbox.top - 30))
        cfg.window.blit(banner,(x - pygame.Surface.get_width(banner)/2, y - pygame.Surface.get_height(banner)/2))
        cfg.window.blit(headimage,(x - 40 - pygame.Surface.get_width(headimage)/2, y - 15 - pygame.Surface.get_height(headimage)))
        cfg.window.blit(fancyfontlives,textRectObjlives)
        cfg.window.blit(fancyfontname,textRectObjname)
        cfg.window.blit(fancyfontpercent,textRectObjpercent)
    
                             