import pygame
import random
import my_settings as settings


class Field:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.table = [[1] + [0] * self.width + [1]
                      for i in range(self.height)] + [[1] * (self.width + 2)]
        self.screen = screen

    def delete_row(self):
        for i in range(self.height):
            if 0 not in self.table[i]:
                self.table = [[1] + [0] * self.width + [1]] + self.table[:i] + self.table[i + 1:]

    def draw(self):
        self.screen.fill(settings.BACKGROUND_COLOR)
        for y in range(self.height):
            for x in range(1, self.width + 1):
                if self.table[y][x] != settings.EMPTY:
                    pygame.draw.rect(self.screen, self.table[y][x], [(x - 1) * settings.CELL_SIZE, y * settings.CELL_SIZE, settings.CELL_SIZE, settings.CELL_SIZE])

    def end_game(self):
        for i in self.table[0][1:-1]:
            if i != 0:
                return True
        return False


class Figure:
    def __init__(self, field, screen, form):
        self.x = field.width // 2 - 1
        self.y = 0
        self.form = form
        self.turn = 0
        self.field = field
        self.screen = screen
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.draw(self.color)

    def draw(self, color):
        for y in range(len(self.form[self.turn])):
            for x in range(len(self.form[self.turn][y])):
                if self.form[self.turn][y][x] == settings.FULL:
                    pygame.draw.rect(self.screen, color, [(self.x + x) * settings.CELL_SIZE, (self.y + y) * settings.CELL_SIZE, settings.CELL_SIZE, settings.CELL_SIZE])

    def can_move_general(self, check_y, check_x, testing_form):
        for y in range(len(self.form[testing_form])):
            for x in range(len(self.form[testing_form][y])):
                if self.form[testing_form][y][x] == settings.FULL:
                    if self.field.table[self.y + y + check_y][self.x + x + check_x] != settings.EMPTY:
                        return False
        return True

    def can_move_down(self, field):
        return self.can_move_general(1, 1, self.turn)

    def move_down(self, screen, field):
        self.draw(settings.BACKGROUND_COLOR)
        self.y += 1
        self.draw(self.color)

    def can_move_left(self, field):
        return self.can_move_general(0, 0, self.turn)

    def move_left(self, screen, field):
        self.draw(settings.BACKGROUND_COLOR)
        self.x -= 1
        self.draw(self.color)

    def can_move_right(self, field):
        return self.can_move_general(0, 2, self.turn)

    def move_right(self, screen, field):
        self.draw(settings.BACKGROUND_COLOR)
        self.x += 1
        self.draw(self.color)

    def to_map(self, screen, field):
        for y in range(len(self.form[self.turn])):
            for x in range(len(self.form[self.turn][y])):
                if self.form[self.turn][y][x] == settings.FULL:
                    self.field.table[self.y + y][self.x + x + 1] = self.color
        self.field.delete_row()
        self.field.draw()

    def can_rotate(self, screen, field):
        return self.can_move_general(0, 1, (self.turn + 1) % len(self.form))

    def rotate(self, screen, field):
        self.draw(settings.BACKGROUND_COLOR)
        self.turn = (self.turn + 1) % (len(self.form))
        self.draw(self.color)


def game(size):
    pygame.init()
    size = size
    screen = pygame.display.set_mode(size)
    field = Field(settings.WIDTH, settings.HEIGHT, screen)
    figure = Figure(field, screen, random.choice(settings.FORMS))
    pygame.time.set_timer(pygame.KEYDOWN, settings.SPEED)
    pygame.display.set_caption("Tetris")
    screen.fill(settings.BACKGROUND_COLOR)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill(settings.WHITE)
                done = True
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if figure.can_move_left(field):
                            figure.move_left(screen, field)
                    elif event.key == pygame.K_RIGHT:
                        if figure.can_move_right(field):
                            figure.move_right(screen, field)
                    elif event.key == pygame.K_UP:
                        if figure.can_rotate(screen, field):
                            figure.rotate(screen, field)
                    else:
                        if figure.can_move_down(field):
                            figure.move_down(screen, field)
                        else:
                            figure.to_map(screen, field)
                            if field.end_game():
                                done = True
                            figure = Figure(field, screen, random.choice(settings.FORMS))
        pygame.display.flip()
    pygame.quit()
