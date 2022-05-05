import pygame

from modules.game import Game

if __name__ == '__main__':
    print("Successfully started application.")
    pygame.init()

    game = Game(20, 20, 400, 400)

    game.run()

    pygame.quit()
