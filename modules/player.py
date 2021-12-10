import pygame
from modules.agent import Agent

class Player(Agent):
    def __init__(self, id: int):
        self.id = id
    def Output(self, event: pygame.event):
        keyUp, keyDown, keyLeft, keyRight = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
        if id == 1:
            keyUp, keyDown, keyLeft, keyRight = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT
        
        if event.type == pygame.KEYDOWN:
            if event.key == keyUp:
                print('yield yeets UP')
                return self._up
            elif event.key == keyDown:
                print('yield yeets DOWN')
                return self._down
            elif event.key == keyLeft:
                print('yield yeets LEFT')
                return self._left
            elif event.key == keyRight:
                print('yield yeets RIGHT')
                return self._right
            else:
                return (0, 0)
        else:
            return (0, 0)