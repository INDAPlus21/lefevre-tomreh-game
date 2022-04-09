import pygame

from modules.agent import Agent

class Player(Agent):
    right = True
    left = False
    up = False
    down = False
    def __init__(self, id: int):
        self.id = id
        self.pos = [1,1]
        self.score = 0
        self.dir = 'right'
        self.added_body = False
        self.key_up, self.key_down, self.key_left, self.key_right = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
        if id == 1:
            self.key_up, self.key_down, self.key_left, self.key_right = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT

    def Output(self, event: pygame.event):
        if event.key == self.key_up:
            if self.dir == 'down':
                return
            self.clear_dirs()
            self.up = True
            self.dir = 'up'

        elif event.key == self.key_down:
            if self.dir == 'up':
                return
            self.clear_dirs()
            self.down = True
            self.dir = 'down'

        elif event.key == self.key_left:
            if self.dir == 'right':
                return
            self.clear_dirs()
            self.left = True
            self.dir = 'left'

        elif event.key == self.key_right:
            if self.dir == 'left':
                return
            self.clear_dirs()
            self.right = True
            self.dir = 'right'

    def clear_dirs(self):
        # set all directions to False
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def update(self):
        if self.right:
            self.pos[0] += 1
        elif self.left:
            self.pos[0] -= 1
        elif self.up:
            self.pos[1] -= 1
        elif self.down:
            self.pos[1] += 1


            



        

    



