from pygame import display
from pygame import draw
from pygame.rect import Rect
import modules.stylesheet as style

class Renderer:
    def __init__(self, w_width, w_height, grid_size):
        self.w_width = w_width
        self.w_height = w_height
        
        self.rects = self.gen_rects(grid_size)

        # Create window
        self.window = display.set_mode((w_width + style.BORDER_THICKNESS * 2
                                        ,w_height + style.BORDER_THICKNESS * 2))
    
        display.set_caption("PvSnake")

        self.draw_zone = self.window.subsurface((style.BORDER_THICKNESS, style.BORDER_THICKNESS
                                                ,w_width, w_height))

        self.window.fill(style.BACKGROUND)

    def draw(self, grid):
        # Background color
        self.draw_zone.fill(style.BACKGROUND)

        x, y = 0, 0

        for row in grid:
            x = 0
            for cell in row:
                match cell[0]:
                    case 1:
                        draw.rect(self.draw_zone, style.SNAKE1, self.rects[y][x])
                    case 2:
                        draw.rect(self.draw_zone, style.FOOD, self.rects[y][x])
                    case 3:
                        draw.rect(self.draw_zone, style.SNAKE2, self.rects[y][x])                    
                x += 1
            y += 1


        # Swap buffers, done last
        display.flip()

        
    def gen_rects(self, size):
        x, y = size
        size_x = self.w_width // x
        size_y = self.w_height // y
        
        offset_x = (self.w_width % size_x) / 2
        offset_y = (self.w_height % size_y) / 2

        rows = []
        for val_y in range(0, self.w_height, size_y):
            row = []
            for val_x in range(0, self.w_width, size_x):
                row.append(Rect(val_x + offset_x, val_y + offset_y, size_x, size_y))
            rows.append(row)

        return rows