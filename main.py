import pygame

from modules.game import Game
from modules.player import Player
from modules.basicBot import BasicBot
from modules.food import Food

if __name__ == '__main__':
    print("Successfully started application.")
    pygame.init()
    
    game = Game((20, 20))

    # Starting food
    foods = [Food((5, 5), 0), Food((5, 6), 1)]

    players = [Player(0), Player(1)]

    game.start(players, foods)
