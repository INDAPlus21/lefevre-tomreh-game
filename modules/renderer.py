from pygame import display, Rect, draw
from modules import stylesheet

class Renderer:
    def __init__(self, w_width, w_height, grid_size):
        self.w_width = w_width
        self.w_height = w_height
        
        self.rects = self.gen_rects(grid_size)

        # Create window
        self.window = display.set_mode((w_width + stylesheet.BORDER_THICKNESS * 2
                                        ,w_height + stylesheet.BORDER_THICKNESS * 2))
    
        display.set_caption("PvSnake")

        self.draw_zone = self.window.subsurface((stylesheet.BORDER_THICKNESS, stylesheet.BORDER_THICKNESS
                                                ,w_width, w_height))

        self.window.fill(stylesheet.BACKGROUND)

    def draw(self, grid):
        # Background color
        self.draw_zone.fill(stylesheet.BACKGROUND)

        x, y = 0, 0

        for row in grid:
            x = 0
            for cell in row:
                match cell[0]:
                    case 1:
                        draw.rect(self.draw_zone, stylesheet.FOOD, self.rects[y][x])
                    case 2:
                        draw.rect(self.draw_zone, stylesheet.SNAKE1, self.rects[y][x])
                    case 3:
                        draw.rect(self.draw_zone, stylesheet.SNAKE2, self.rects[y][x])                    
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