from modules.vec import Vec2
from modules.snake import Snake
import pygame
import queue
from random import randint
from modules.renderer import Renderer

DOWN  = Vec2(0, 1)
UP    = Vec2(0, -1)
LEFT  = Vec2(-1, 0)
RIGHT = Vec2(1, 0)

class Game:
    def __init__(self, x, y) -> None:
        self.dimension = Vec2(x, y)
        self.grid = [[[0, 0] for i in range(x)] for j in range(y)]
        self.snakes = [Snake(0)]
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.running = True
        self.food_flag = True
    
    def __repr__(self) -> str:
        out = ""
        for row in self.grid:
            out += "|"            
            for cell in row:
                out += f"{cell[0]},{cell[1]}|"
            out += "\n"
            
        return out
            
    def run(self, w, h) -> None:
        self.put_snakes(self.snakes)
        # print(self)
        renderer = Renderer(w, h, (self.dimension.x, self.dimension.y))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key > 5000:
                        self.snakes[0].event_handle(event)
                    else:
                        self.snakes[1].event_handle(event)
            
            for snake in self.snakes:
                if not snake.update(self.dimension.x, self.dimension.y):
                    self.game_over("Hit wall")
            
            self.check_col(self.snakes)
            self.put_snakes(self.snakes)
            self.clean_grid(self.snakes)
            self.spawn_food()
            renderer.draw(self.grid)
            self.clock.tick(self.FPS)
        
    def put_snakes(self, snakes) -> None:
        for snake in snakes:
            self.grid[snake.pos.y][snake.pos.x] = [snake.id, 0]
        
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
        
    def check_col(self, snakes) -> None:
        for snake in snakes:
            col_val = self.grid[snake.pos.y][snake.pos.x][0]
            match col_val:
                case 0:
                    pass
                case 1:
                    snake.add_len()
                case snake.id:
                    self.game_over("Self hit!")
                case _:
                    self.game_over(f"Hit snake nr.{col_val - 2}")
    
    def game_over(self, why) -> None:
        print("Game over!")
        print("You: " + why)
        self.running = False
        
    
    def spawn_food(self) -> None:
        if not self.food_flag:
            return
        rand_x = randint(0, self.dimension.x - 1)
        rand_y = randint(0, self.dimension.y - 1)
                
        while self.grid[rand_y][rand_x][0] != 0:
            rand_x = randint(0, self.dimension.x - 1)
            rand_y = randint(0, self.dimension.y - 1)
        
        self.grid[rand_y][rand_x][0] = 1

