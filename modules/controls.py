import pygame


class Controlscheme:
    def __init__(self, id) -> None:
        """
        Sets default keybinds for players

        Args:
            id: The id of the snake.
        """
        match id:
            # Player 1
            case 0:
                self.up = pygame.K_UP
                self.down = pygame.K_DOWN
                self.left = pygame.K_LEFT
                self.right = pygame.K_RIGHT
            # Player 2
            case 1:
                self.up = pygame.K_w
                self.down = pygame.K_s
                self.left = pygame.K_a
                self.right = pygame.K_d
            # Player x
            case _:
                self.up = 0
                self.down = 1
                self.left = 2
                self.right = 3

    def __iter__(self):
        """
        Returns an iterator that contains the values of the controlscheme object
        """
        return [self.up, self.down, self.left, self.right]
