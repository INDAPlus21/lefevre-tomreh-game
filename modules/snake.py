from modules.vec import Vec2
import pygame

class Snake:
    def __init__(self) -> None:
        self.pos = Vec2(0, 0)
        self.len = 1
        self.dir = Vec2(0, 1)
        
    def event_handle(self, event) -> None:
        match event.key:
            case pygame.K_DOWN:
                if self.dir != Vec2(0, -1):
                    self.dir = Vec2(0,  1)
            case pygame.K_UP:
                if self.dir != Vec2(0,  1):
                    self.dir = Vec2(0, -1)
            case pygame.K_RIGHT:
                if self.dir != Vec2(-1, 0):
                    self.dir = Vec2(1,  0)
            case pygame.K_LEFT:
                if self.dir != Vec2(1,  0):
                    self.dir = Vec2(-1,  0)
                                
    def update(self, x, y) -> bool:
        self.pos += self.dir
        if self.pos.x < 0 or self.pos.y < 0:
            return False
        
        if self.pos.x >= x or self.pos.y >= y:
            return False
        
        return True
    
    def add_len(self) -> None:
        self.len += 1
        