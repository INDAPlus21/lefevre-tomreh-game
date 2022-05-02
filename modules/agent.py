from modules.vec import Vec2
from modules.consts import *
class Agent:    
    def __init__(self, start_pos = Vec2(0, 0), start_dir = DOWN):
        self.pos = start_pos
        self.dir = start_dir
        self.len = 1
        
    
    def Output(self, state):
        pass