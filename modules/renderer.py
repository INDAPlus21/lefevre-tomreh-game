import pygame

from modules.game import Game

class Renderer:
    def __init__(self, game: Game, size_x: int, size_y: int) -> None:
        self.game = game

        self.screen = pygame.display.set_mode((size_x, size_y))
        self.screen_width = size_x
        self.screen_height = size_y

        self.rects = self.pre_gen_rects()
        pygame.display.set_caption('Snakes on INDA')

    def draw(self) -> None:
        self.screen.fill((255, 0, 255))

        color: list = [0, 255, 255]

        for row_index, row in enumerate(self.game.array):
            for val_index, val in enumerate(row):
                if val != 0:
                    pygame.draw.rect(self.screen, color, self.rects[val_index][row_index])

        pygame.display.flip()

    def pre_gen_rects(self):
        x_const: int = self.screen_width // self.game.width
        y_const: int = self.screen_height // self.game.height

        rect_list = []

        for x_val in range(0, self.screen_width, x_const):
            sub_list = []
            for y_val in range(0, self.screen_height, y_const):
                sub_list.append(pygame.rect.Rect(x_val, y_val, x_const, y_const))
            
            rect_list.append(sub_list)

        return rect_list


