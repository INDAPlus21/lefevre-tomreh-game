import pygame
from modules.renderer import Renderer

from modules.game import Game
from modules.player import Player
from modules.basicBot import BasicBot

if __name__ == '__main__':
    print("Successfully started application.")

    pygame.init()
    renderer = Renderer(400, 400)
    game = Game((20, 20))

    game.start(Player(0), Player(1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        renderer.draw()
