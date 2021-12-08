class Game:
    def __init__(self, size_x: int, size_y: int) -> None:
        self.width = size_x
        self.height = size_y
        self.array = [[0] * size_x] * size_y

    def __repr__(self) -> str:
        out_string = ""

        for row in self.array:
            out_string += (str(row) + '\n')

        return out_string