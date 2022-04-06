from pygame import display, Rect, draw
from modules import stylesheet

class Renderer:
    def __init__(self, w_width, w_height):
        self.w_width = w_width
        self.w_height = w_height
        
        self.rects = self.gen_rects(10)

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
                if cell == 1:
                    draw.rect(self.draw_zone, stylesheet.CELL1, self.rects[y][x])
                x += 1
            y += 1


        # Swap buffers, done last
        display.flip()

        
    def gen_rects(self, size):
        cell_size = self.w_width // size

        rows = []
        for val_y in range(0, self.w_width, cell_size):
            row = []
            for val_x in range(0, self.w_width, cell_size):
                row.append(Rect(val_x, val_y, cell_size, cell_size))
            rows.append(row)

        return rows