import pygame

from agent import Agent

class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
    def start(self, agent1, agent2):
        pygame.init()

        clock = pygame.time.Clock()

        while(True):
            for event in pygame.event.get():
                print('an event')
                if event.type == pygame.KEYDOWN:
                    print(agent1.Output(event))
                    print(agent2.Output(event))