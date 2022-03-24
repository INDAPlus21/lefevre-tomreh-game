from modules.renderer import Renderer
import pygame

if __name__ == '__main__':
    pygame.init()
    renderer = Renderer(400, 400)

    test_grid = [[0] * 10 for i in range(10)]
    test_grid[0][0] = 1
    test_grid[9][9] = 1
    test_grid[5][3] = 1
    test_grid[3][5] = 1
    test_grid[4][4] = 1
    test_grid[5][5] = 1
    test_grid[5][4] = 1
    test_grid[4][5] = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break;

        renderer.draw(test_grid)

pygame.quit()
