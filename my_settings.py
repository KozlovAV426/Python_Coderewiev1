WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
BACKGROUND_COLOR = (250, 131, 230, 2)
LEFT_RIGHT_PLAYBUTTON = list(range(85, 407))
UP_DOWN_PLAYBUTTON = list(range(272, 431))
LEFT_RIGHT_QUITBUTTON = list(range(76, 421))
UP_DOWN_QUITBUTTON = list(range(287, 484))


SPEED = 900
WIDTH = 16
HEIGHT = 20
EMPTY = 0
FULL = 1
CELL_SIZE = 30
SIZE = [CELL_SIZE * WIDTH, CELL_SIZE * HEIGHT]


#FIGURES
SQUARE = [[[1, 1],
 [1, 1]]]

STICK = [[[1, 1, 1, 1]], [[0, 1],
                          [0, 1],
                          [0, 1],
                          [0, 1]]]
L = [[[1, 0, 0],[1, 1, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 1, 1],[0, 0, 1]], [[0, 1],[0, 1],[1, 1]]]

ZED_L = [[[1, 1, 0],
         [0, 1, 1]], [[0, 1],
                   [1, 1],
                   [1, 0]]]

ZED_R = [[[0, 1, 1],
         [1, 1, 0]], [[1, 0],
                      [1, 1],
                      [0, 1]]]

F = [[[0, 1, 0],
      [1, 1, 1]], [[1, 0],
                   [1, 1],
                   [1, 0]], [[1, 1, 1],[0, 1, 0]],[[0, 1],
                                                   [1, 1],
                                                   [0, 1]]]

FORMS = [F, STICK, ZED_L, ZED_R, SQUARE]