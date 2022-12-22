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
grave_2 = pygame.image.load('graphics/grave.png').convert_alpha()    # 800x840
grave_2 = pygame.transform.scale(grave_2, (100, 105))
background = pygame.Surface((1280, 720))
background.fill('grey')
game_clock = pygame.time.Clock()

background_x_coord = 0  # always 0
ground_x_coord = 0  # always 0
game_speed = 12

grave_x_coord = 1300
grave_y_coord = 650
grave_2_x_coord = 2000
grave_2_y_coord = 650

#   jump setup

jump = 0  # always 0
player_x_coord = 650
jump_count_down = 0  # always 0
jump_len = 40   # jump length in frames
player_x_coord_change_base = 30  # changes speed of jump
player_x_coord_change = player_x_coord_change_base
player_acceleration = 2*player_x_coord_change_base/jump_len

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

    grave_rect = grave.get_rect(bottomleft=(grave_x_coord, grave_y_coord))
    screen.blit(grave, grave_rect)
    pygame.draw.circle(grave, (255, 255, 255), (grave_x_coord + 55, grave_y_coord - 60), 45)

    grave_2_rect = grave_2.get_rect(bottomleft=(grave_2_x_coord, grave_2_y_coord))
    screen.blit(grave_2, grave_2_rect)
    pygame.draw.circle(grave_2, (255, 255, 255), (grave_2_x_coord + 55, grave_2_y_coord - 60), 45)

    character_rect = character.get_rect(bottomleft=(20, player_x_coord))
    screen.blit(character, character_rect)

    # move of graves and tree background
    background_x_coord -= game_speed
    ground_x_coord -= game_speed
    grave_x_coord -= game_speed
    grave_2_x_coord -= game_speed

    if background_x_coord < -1863:
        background_x_coord = 0
    if ground_x_coord < -1387:
        ground_x_coord = 0

    # jump
    if keys[pygame.K_SPACE] and game_speed != 0:
        jump = 1

    if jump:
        if jump_count_down < jump_len/2:
            jump_count_down += 1
            player_x_coord_change -= player_acceleration
            player_x_coord -= player_x_coord_change
        if jump_count_down == jump_len/2:
            player_x_coord_change = 0
            jump_count_down += 1
        if jump_len/2 < jump_count_down < jump_len:
            jump_count_down += 1
            player_x_coord_change += player_acceleration
            player_x_coord += player_x_coord_change
        if jump_count_down == jump_len:
            jump = 0
            jump_count_down = 0
            player_x_coord_change = player_x_coord_change_base

    pygame.display.update()
    game_clock.tick(60)
