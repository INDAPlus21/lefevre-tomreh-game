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

        red_color: list = [255, 0, 0]
        blue_color: list = [0, 0, 255]

        for row_index, row in enumerate(self.game.array):
            for val_index, val in enumerate(row):
                match val[0]:
                    case 1:
                        pygame.draw.rect(self.screen, red_color, self.rects[val_index][row_index])
                    case 2:
                        pygame.draw.rect(self.screen, blue_color, self.rects[val_index][row_index])

        pygame.display.flip()

    def pre_gen_rects(self) -> list[list]:
        size_const: int = min(self.screen_width // self.game.width, self.screen_height // self.game.height)

        rect_list = []

        for x_val in range((self.screen_width - self.game.width * size_const) // 2, self.screen_width, size_const):
            sub_list = []
            for y_val in range((self.screen_height - self.game.height * size_const) // 2, self.screen_height, size_const):
                sub_list.append(pygame.rect.Rect(x_val, y_val, size_const, size_const))
            
            rect_list.append(sub_list)

        return rect_list


