from pygame import display, Rect, draw
import json

class Renderer:
    def __init__(self, w_width, w_height):
        # Not really needed
        self.d = self.load_artistic()

        self.w_width = w_width
        self.w_height = w_height
        
        self.rects = self.gen_rects(10)

        # Create window
        self.window = display.set_mode((w_width + self.d["d"]["bt"] * 2
                                        ,w_height + self.d["d"]["bt"] * 2))
    
        display.set_caption("PvSnake")

        self.draw_zone = self.window.subsurface((self.d["d"]["bt"], self.d["d"]["bt"]
                                                ,w_width, w_height))

        self.window.fill(self.d["c"]["br"])

    def draw(self, grid):
        # Background color
        self.draw_zone.fill(self.d["c"]["bg"])

        x, y = 0, 0

        for row in grid:
            x = 0
            for cell in row:
                if cell == 1:
                    draw.rect(self.draw_zone, self.d["c"]["cc"], self.rects[y][x])
                x += 1
            y += 1


        # Swap buffers, done last
        display.flip()

    # Overcomplication kekw
    def load_artistic(self):
        with open("assets/artistic.json") as f:
            return json.load(f)

        
    def gen_rects(self, size):
        cell_size = self.w_width // size

        rows = []
        for val_y in range(0, self.w_width, cell_size):
            row = []
            for val_x in range(0, self.w_width, cell_size):
                row.append(Rect(val_x, val_y, cell_size, cell_size))
            rows.append(row)

        return rows