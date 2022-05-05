from modules.vec import Vec2
from modules.snake import Snake
import pygame
from random import randint
from modules.renderer import Renderer

DOWN = Vec2(0, 1)
UP = Vec2(0, -1)
LEFT = Vec2(-1, 0)
RIGHT = Vec2(1, 0)


class Game:
    def __init__(self, x, y, w, h) -> None:
        self.dimension = Vec2(x, y)
        self.grid = [[[0, 0] for i in range(x)] for j in range(y)]
        self.snakes = [Snake(0), Snake(1)]
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.running = True
        self.food_flag = True
        self.scene_select = 0
        self.renderer = Renderer(w, h, (self.dimension.x, self.dimension.y))
        self.snakes_used = 1

    def __repr__(self) -> str:
        out = ""
        for row in self.grid:
            out += "|"
            for cell in row:
                out += f"{cell[0]},{cell[1]}|"
            out += "\n"

        return out

    def run(self) -> None:
        while self.running:
            events = pygame.event.get()
            match self.scene_select:
                case 0:
                    self.scene_select = self.renderer.draw_menu(events)
                case 1:
                    self.snakes_used = 1
                    self.scene_select = self.game(events, self.scene_select)
                    self.renderer.draw_game(self.grid)
                case 2:
                    self.snakes_used = 2
                    self.scene_select = self.game(events, self.scene_select)
                    self.renderer.draw_game(self.grid)
                case 3:
                    self.scene_select = self.renderer.draw_end(
                        events, self.loser)

    def add_snake(self):
        self.snakes.append(Snake(self.id))
        self.id += 1

    def game(self, events, state):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # KEKW optimaztion
                if event.key > 5000:
                    self.snakes[0].event_handle(event)
                else:
                    self.snakes[1].event_handle(event)

        # Nice naming
        flag = True
        for snake in self.snakes[0:self.snakes_used]:
            if not snake.update(self.dimension.x, self.dimension.y):
                self.game_over(snake.id - 2)
                state = 3
                flag = False

        if flag:
            self.clean_grid(self.snakes)
            if self.put_snakes(self.snakes[0:self.snakes_used]):
                self.spawn_food()
                self.renderer.draw_game(self.grid)
                self.clock.tick(self.FPS)
            else:
                state = 3

        return state

    def get_inverse_snake(self, snakeid):
        if self.snakes_used == 1:
            return snakeid
        else:
            return self.snakes[snakeid - 1].id

    def put_snakes(self, snakes) -> None:
        for snake in snakes:
            slot = self.grid[snake.pos.y][snake.pos.x]
            match slot[0]:
                case 0:
                    self.grid[snake.pos.y][snake.pos.x] = [snake.id, 0]
                case 1:
                    snake.add_len()
                    self.grid[snake.pos.y][snake.pos.x] = [snake.id, 0]
                case _:
                    if slot[1] != 0:
                        self.game_over(self.get_inverse_snake(slot[0] - 2))
                        return False
                    else:
                        self.game_over(2)
                        return False
        return True

    def clean_grid(self, snakes):
        self.food_flag = True
        for row in self.grid:
            for cell in row:
                id_val = cell[0]
                index_val = cell[1]
                if id_val < 2:
                    if id_val == 1:
                        self.food_flag = False
                else:
                    if index_val >= snakes[id_val - 2].len:
                        cell[0] = 0
                        cell[1] = 0
                    else:
                        cell[1] += 1

    def game_over(self, loser) -> None:
        self.reset(loser)

    def reset(self, loser):
        self.grid = [[[0, 0] for _ in range(
            self.dimension.x)] for _ in range(self.dimension.y)]
        self.snakes = [Snake(0), Snake(1)]
        self.loser = loser

    def spawn_food(self) -> None:
        if not self.food_flag:
            return
        rand_x = randint(0, self.dimension.x - 1)
        rand_y = randint(0, self.dimension.y - 1)

        while self.grid[rand_y][rand_x][0] != 0:
            rand_x = randint(0, self.dimension.x - 1)
            rand_y = randint(0, self.dimension.y - 1)

        self.grid[rand_y][rand_x][0] = 1
