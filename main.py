import pygame

from modules.game import Game

if __name__ == '__main__':
    print("Successfully started application.")
    pygame.init()
    
    game = Game(10, 10)

    game.run()
    
    pygame.quit()
