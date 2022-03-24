from game import Game
from player import Player
from basicBot import BasicBot


print("Successfully started application.")
game = Game((20, 20))

game.start(Player(0), Player(1))