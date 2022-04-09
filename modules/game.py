import pygame
import random

from modules.renderer import Renderer
from modules.agent import Agent
from modules.player import Player
from modules.food import Food


class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[(0,0)] * grid_size[0] for i in range(grid_size[1])]
        
    def start(self, agents, foods):
        pygame.init()

        renderer = Renderer(400, 400, self.grid_size)

        players = agents


        # create a pygame clock
        clock = pygame.time.Clock()
        FPS = 10

        running = True
        while running:
            # limit frame speed to 20 FPS
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    for player in players:
                        player.Output(event)
                    if event.key == pygame.K_ESCAPE:
                        running = False

            for player in players:
                player.update()

            # check if player is outside grid
            killed_players = []
            for player in players:
                if player.pos[0] < 0 or player.pos[0] >= self.grid_size[0] or player.pos[1] < 0 or player.pos[1] >= self.grid_size[1]:
                    # kill player
                    killed_players.append(player)
                    print(f"Agent {player.id} has been killed")

            # remove killed players from players
            for player in killed_players:
                players.remove(player)
            # check if player hits food
            for player in players:
                for food in foods:
                    if player.pos[0] == food.pos[0] and player.pos[1] == food.pos[1] and player.id == food.id:
                        player.score += 1
                        foods.remove(food)
                        print(f"Agent {player.id} has eaten food")
                        # create new food with random pos in the grid
                        new_food = Food((random.randint(0, self.grid_size[0]-1), random.randint(0, self.grid_size[1]-1)), player.id)
                        foods.append(new_food)
                        print(f"Agent {player.id} has eaten food {food.id}. Current score: {player.score}, New food at {new_food.id}")
                        # TODO: Add body parts 

            # draw the agents
            renderer.draw(self.grid, players, foods)
            
        pygame.quit()
            
    def draw_grid(self):
        for i in range(self.grid_size[1]):
            msg = ""
            for j in range(self.grid_size[0]):
                msg += str(self.grid[j][i]) + " "
            print(msg)