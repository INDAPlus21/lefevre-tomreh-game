from pygame import display
from pygame import Surface
import json

class Renderer:
    def __init__(self, w_width, w_height):
        # Not really needed
        self.load_artistic()

        # Create window
        self.window = display.set_mode((w_width + self.art_d["d"]["bt"] * 2
                                        ,w_height + self.art_d["d"]["bt"] * 2))
        display.set_caption("PvSnake")

        self.draw_zone = self.window.subsurface((self.art_d["d"]["bt"], self.art_d["d"]["bt"]
                                                ,w_width, w_height))

        self.window.fill(self.art_d["c"]["br"])


    def draw(self):
        # Background color
        self.draw_zone.fill(self.art_d["c"]["bg"])

        # Swap buffers, done last
        display.flip()

    # Overcomplication kekw
    def load_artistic(self):
        with open("assets/artistic.json") as f:
            self.art_d = json.load(f)

        
