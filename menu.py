import pygame
import random
import my_settings as settings


def starter_menu(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    img = pygame.image.load('menu.png')
    screen.blit(img, (0, 0))
    pygame.display.set_caption("Tetris")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((255, 255, 255, 255))
                done = True
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] in range(85, 407) and pygame.mouse.get_pos()[1] in range(272, 431)):
                done = True
                return True
        pygame.display.flip()
    pygame.quit()


def game_over_menu(size):
    pygame.init()
    screen = pygame.display.set_mode(size)
    img = pygame.image.load('game_over.png')
    screen.blit(img, (0, 0))
    pygame.display.set_caption("Tetris")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill((255, 255, 255, 255))
                done = True
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] in range(76, 421) and pygame.mouse.get_pos()[1] in range(287, 484)):
                done = True
                return True
        pygame.display.flip()
    pygame.quit()
