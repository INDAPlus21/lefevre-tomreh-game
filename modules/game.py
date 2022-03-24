import pygame
import sys

from modules.renderer import Renderer
from modules.agent import Agent

class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[(0,0)] * grid_size[0] for i in range(grid_size[1])]
    def start(self, agent1, agent2):
        pygame.init()

        clock = pygame.time.Clock()
        renderer = Renderer(400, 400)
        self.draw_grid()

        running = True
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    agent1.Output(event)
                    agent2.Output(event)

            renderer.draw()
    def draw_grid(self):
        for i in range(self.grid_size[1]):
            msg = ""
            for j in range(self.grid_size[0]):
                msg += str(self.grid[j][i]) + " "
            print(msg)