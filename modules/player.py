import pygame

from modules.agent import Agent

class Player(Agent):
    def __init__(self, id: int):
        self.id = id
        self.key_up, self.key_down, self.key_left, self.key_right = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
        if id == 1:
            self.key_up, self.key_down, self.key_left, self.key_right = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT
    def Output(self, event: pygame.event):
        if event.key == self.key_up:
            print('yield yeets UP')
            return self._up
        elif event.key == self.key_down:
            print('yield yeets DOWN')
            return self._down
        elif event.key == self.key_left:
            print('yield yeets LEFT')
            return self._left
        elif event.key == self.key_right:
            print('yield yeets RIGHT')
            return self._right
        else:
            return (0, 0)