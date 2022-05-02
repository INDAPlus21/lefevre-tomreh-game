import pygame

from modules.agent import Agent
from modules.vec import Vec2
from modules.consts import *

class Player:
    def __init__(self, id: int):
        self.id = id
        self.key_up, self.key_down, self.key_left, self.key_right = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
        if id == 1:
            self.key_up, self.key_down, self.key_left, self.key_right = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT
        self.pos = Vec2(0, 0)
        self.dir = DOWN
        self.len = 1
            
    def Output(self, event: pygame.event):
        if event.key == self.key_up:
            print('yield yeets UP')
            self.dir = UP
        elif event.key == self.key_down:
            print('yield yeets DOWN')
            self.dir = DOWN
        elif event.key == self.key_left:
            print('yield yeets LEFT')
            self.dir = LEFT
        elif event.key == self.key_right:
            print('yield yeets RIGHT')
            self.dir = RIGHT
            
        print(self.dir, "Output")