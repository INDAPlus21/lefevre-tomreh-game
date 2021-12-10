import pygame
from modules.game import Game
from modules.renderer import Renderer
from modules.agent import Agent
from modules.player import Player
from modules.basicBot import BasicBot


if __name__ == "__main__":
    pygame.init()

    game = Game(8, 8)
    renderer = Renderer(game, 256, 256)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.draw()
    