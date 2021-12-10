import pygame
from modules import Agent

class Player(Agent):
    def __init__(self, id: int):
        self.id = id
    def Output(self, event: pygame.event):
        keyUp, keyDown, keyLeft, keyRight = 'w', 's', 'a', 'd'
        if id == 1:
            keyUp, keyDown, keyLeft, keyRight = 'up arrow', 'down arrow', 'left arrow', 'right arrow'
        
        try:
            if keyboard.is_pressed(keyUp):
                print('yield yeets UP')
                return UP
            elif keyboard.is_pressed(keyDown):
                print('yield yeets DOWN')
                return DOWN
            elif keyboard.is_pressed(keyLeft):
                print('yield yeets LEFT')
                return LEFT
            elif keyboard.is_pressed(keyRight):
                print('yield yeets RIGHT')
                return RIGHT
        except:
            return (0, 0)