from pygame import display
from pygame import draw
from pygame.rect import Rect
import modules.stylesheet as style
from modules.UI import UI


class Renderer:
    def __init__(self, w_width, w_height, grid_size) -> None:
        self.w_width = w_width
        self.w_height = w_height

        # Cells
        self.rects = self.gen_rects(grid_size)

        # Auto size grid for different sizes
        x, y = grid_size
        cell_size = min(w_width, w_height) // max(x, y)
        dynamic_border_x = (w_width - (x * cell_size))/2
        dynamic_border_y = (w_height - (y * cell_size))/2

        # Create window
        self.window = display.set_mode((w_width + style.BORDER_THICKNESS * 2,
                                        w_height + style.BORDER_THICKNESS * 2))

        display.set_caption("PvSnake")

        # Create subsurface for drawing on
        self.draw_zone = self.window.subsurface((
            dynamic_border_x + style.BORDER_THICKNESS,
            dynamic_border_y + style.BORDER_THICKNESS,
            w_width - (dynamic_border_x * 2),
            w_height - (dynamic_border_y * 2)))

        self.window.fill(style.BORDER)
        self.ui = UI(self.draw_zone)

    def draw_game(self, grid):
        # Background color
        self.draw_zone.fill(style.BACKGROUND)

        x, y = 0, 0

        for row in grid:
            x = 0
            for cell in row:
                match cell[0]:
                    case 0:
                        pass
                    case 1:
                        draw.rect(self.draw_zone, style.FOOD, self.rects[y][x])
                    case _:
                        draw.rect(self.draw_zone,
                                  style.SNAKES[cell[0] - 2], self.rects[y][x])
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
                row.append(Rect(val_x + offset_x, val_y +
                           offset_y, size_x, size_y))
            rows.append(row)

        return rows

    def draw_menu(self, events):
        return self.ui.menu.run(self.draw_zone, events)

    def draw_end(self, events, loser):
        return self.ui.end.run(self.draw_zone, events, loser)
