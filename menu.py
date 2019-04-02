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
                screen.fill(settings.WHITE)
                done = True
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] in settings.LEFT_RIGHT_PLAYBUTTON
                                                         and pygame.mouse.get_pos()[1] in settings.UP_DOWN_PLAYBUTTON):
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
                screen.fill(settings.WHITE)
                done = True
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0] in settings.LEFT_RIGHT_QUITBUTTON
                                                         and pygame.mouse.get_pos()[1] in settings.UP_DOWN_QUITBUTTON):
                done = True
                return True
        pygame.display.flip()
    pygame.quit()
