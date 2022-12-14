import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))   # 1280x720

character = pygame.image.load('graphics/psychopath_derek.png').convert_alpha()     # 520x730
character = pygame.transform.scale(character, (120, 170))   # 150x220
background_graveyard_1 = pygame.image.load('graphics/background_1.png').convert_alpha()   # 1863x455
background_graveyard_2 = background_graveyard_1
ground = pygame.image.load('graphics/ground.png').convert_alpha()   # 1387x180
grave = pygame.image.load('graphics/grave.png').convert_alpha()    # 800x840
grave = pygame.transform.scale(grave, (100, 105))
background = pygame.Surface((1280, 720))
background.fill('grey')
game_clock = pygame.time.Clock()

background_x_coord = 0
ground_x_coord = 0
game_speed = 6
jump = 0
player_x_coord = 650
player_x_coord_change = 24
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    screen.blit(background, (0, 0))

    background_graveyard_1_rect = background_graveyard_1.get_rect(bottomleft=(background_x_coord, 720))
    screen.blit(background_graveyard_1, background_graveyard_1_rect)

    background_graveyard_2_rect = background_graveyard_2.get_rect(bottomleft=(background_x_coord + 1863, 720))
    screen.blit(background_graveyard_2, background_graveyard_2_rect)

    ground_rect = ground.get_rect(bottomleft=(ground_x_coord, 770))
    screen.blit(ground, ground_rect)

    ground_2_rect = ground.get_rect(bottomleft=(ground_x_coord+1387, 770))
    screen.blit(ground, ground_2_rect)

    screen.blit(grave, (0, 0))

    character_rect = character.get_rect(bottomleft=(20, player_x_coord))
    screen.blit(character, character_rect)

    # move of graves and tree background
    background_x_coord -= game_speed
    ground_x_coord -= game_speed

    if background_x_coord < -1863:
        background_x_coord = 0
    if ground_x_coord < -1387:
        ground_x_coord = 0

    # jump
    if keys[pygame.K_SPACE] and game_speed != 0:
        jump = 1

    if jump:
        if i < 30:
            i += 1
            player_x_coord_change -= 0.8
            player_x_coord -= player_x_coord_change
        if i == 30:
            player_x_coord_change = 0
            i += 1
        if 30 < i < 60:
            i += 1
            player_x_coord_change += 0.8
            player_x_coord += player_x_coord_change
        if i == 60:
            jump = 0
            i = 0
            player_x_coord_change = 24

    pygame.display.update()
    game_clock.tick(60)
