import tetris.game as game
import tetris.menu as menu
import tetris.settings as settings

done = False
while not done:
    if menu.starter_menu(settings.SIZE):
        game.game(settings.SIZE)
        if menu.game_over_menu(settings.SIZE):
            game.game(settings.SIZE)
        else:
            done = True
    else:
        done = True
