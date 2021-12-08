import pygame

from modules.game import Game

class Renderer:
    def __init__(self, game: Game) -> None:
        self.game = game

        self.screen = pygame.display.set_mode((255, 255))
        pygame.display.set_caption('Snakes on INDA')

    def draw(self) -> None:
        self.screen.fill((255, 0, 255))
        pygame.display.flip()