from modules.renderer import Renderer
import pygame

if __name__ == '__main__':
    pygame.init()
    renderer = Renderer(400, 400)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        renderer.draw()