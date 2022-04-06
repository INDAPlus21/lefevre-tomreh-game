import pygame

from modules.game import Game
from modules.player import Player
from modules.basicBot import BasicBot

if __name__ == '__main__':
    print("Successfully started application.")
    pygame.init()
    
    game = Game((20, 20))

    game.start(Player(0), Player(1))
