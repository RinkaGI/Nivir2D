################# RUNNER GAME IN PYGAME ###################

import pygame, sys

pygame.init()

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    text_surface = test_font.render(f'{current_time}', False, (64, 64, 64))
    text_rectangle = text_surface.get_rect(center = (400, 50))
    screen.blit(text_surface, text_rectangle)
    return current_time

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# text_surface = test_font.render('My game', False, 'Black').convert()
# text_rectangle =  text_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = -20
player_on_floor = False

#First screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand_scaled.get_rect(center=(400,200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169)).convert()
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to jump!', False, (111, 196, 169)).convert()
game_message_rect = game_message.get_rect(center = (400, 310))

  
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if game_active == True:

            if e.type == pygame.MOUSEBUTTONDOWN:
                player_gravity = -20

            if e.type == pygame.KEYDOWN:
                
                if e.key == pygame.K_SPACE:
                        if player_on_floor == True:
                            player_gravity = -20
                            player_on_floor = False
        
        else:
            if e.type == pygame.KEYDOWN:
                game_active = True
                snail_rectangle.left = 800
                start_time = int(pygame.time.get_ticks())

    if game_active == True:
        # Dibujar las cosas en pantalla
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, 'Pink', text_rectangle, 20)
        # screen.blit(text_surface, text_rectangle)
        score = display_score() 

        snail_rectangle.x -= 4
        if snail_rectangle.right <= 0: snail_rectangle.left = 800
        screen.blit(snail_surface, snail_rectangle)
        screen.blit(player_surface, player_rectangle)

        # Jugador
        player_gravity += 1
        player_rectangle.y += player_gravity
        player_on_floor = False

        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
            player_on_floor = True

        # colision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False 

    else:
        screen.fill((94, 129, 162))

        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_message, game_message_rect)

        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 390))
    

    # Actualizar la pantalla
    pygame.display.update()
    clock.tick(60)
 
