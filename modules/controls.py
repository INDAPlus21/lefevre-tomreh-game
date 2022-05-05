import pygame


class Controlscheme:
    def __init__(self, id) -> None:
        match id:
            case 0:
                self.up = pygame.K_UP
                self.down = pygame.K_DOWN
                self.left = pygame.K_LEFT
                self.right = pygame.K_RIGHT
            case 1:
                self.up = pygame.K_w
                self.down = pygame.K_s
                self.left = pygame.K_a
                self.right = pygame.K_d
            case _:
                self.up = 0
                self.down = 1
                self.left = 2
                self.right = 3

    def __iter__(self):
        return [self.up, self.down, self.left, self.right]
