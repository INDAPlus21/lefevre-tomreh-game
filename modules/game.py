import pygame

from modules.renderer import Renderer
from modules.agent import Agent
from modules.vec import Vec2
from pygame.time import Clock

class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[[0,0]] * grid_size[0] for i in range(grid_size[1])]
        self.FPS = 1
        self.clock = Clock()

    def update_grid(self, agent1, agent2):
        print(agent1.dir, "Dir update")
        agent1.pos + agent1.dir
        agent2.pos + agent2.dir
        
        print(agent1.pos, "Pos update")
        
        self.grid[agent1.pos.y][agent1.pos.x] = [1, 0]
        self.grid[agent2.pos.y][agent2.pos.x] = [2, 0]
        x, y = 0, 0
        for row in self.grid:
            for cell in row:
                if cell[0] == 0:
                    pass
                else:
                    cell[1] += 1
                    if cell[0] == 1:
                        if cell[1] >= agent1.len:
                            print(x, y)
                            self.grid[y][x] = [0, 0]
                    elif cell[0] == 2:
                        if cell[1] >= agent2.len:
                            print(x, y)
                            self.grid[y][x] = [0, 0]
                x += 1
            y += 1

    def start(self, agent1, agent2):
        pygame.init()

        renderer = Renderer(400, 400)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    agent1.Output(event)
                    agent2.Output(event)
            
            self.update_grid(agent1, agent2)
            renderer.draw(self.grid)
            self.draw_grid()
            self.clock.tick(self.FPS)
            
        pygame.quit()
            
    def draw_grid(self):
        for i in range(self.grid_size[1]):
            msg = ""
            for j in range(self.grid_size[0]):
                msg += str(self.grid[j][i]) + " "
            print(msg)