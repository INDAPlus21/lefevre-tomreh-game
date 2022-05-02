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
        self.snake = Snake()
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.running = True
        self.food_flag = True
        self.input_buffer = queue.Queue(2)
        self.prev_input = pygame.K_DOWN
    
    def __repr__(self) -> str:
        out = ""
        for row in self.grid:
            out += "|"            
            for cell in row:
                out += f"{cell[0]},{cell[1]}|"
            out += "\n"
            
        return out
            
    def run(self, w, h) -> None:
        self.put_snake(self.snake)
        # print(self)
        renderer = Renderer(w, h, (self.dimension.x, self.dimension.y))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if not self.input_buffer.full() and event.key != self.prev_input:
                        self.input_buffer.put_nowait(event)
                    self.prev_input = event.key
            
            if not self.input_buffer.empty():
                curr_event = self.input_buffer.get()
                self.snake.event_handle(curr_event)
                    
            if not self.snake.update(self.dimension.x, self.dimension.y):
                self.game_over()
            else:
                self.check_col(self.snake)
                self.put_snake(self.snake)
                self.clean_grid(self.snake)
                self.spawn_food()
                renderer.draw(self.grid)
                self.clock.tick(self.FPS)
        
    def put_snake(self, snake: Snake) -> None:
        self.grid[snake.pos.y][snake.pos.x] = [1, 0]
        
    def clean_grid(self, snake):
        self.food_flag = True
        for row in self.grid:
            for cell in row:
                if cell[0] != 1:
                    if cell[0] == 2:
                        self.food_flag = False
                else:
                    if cell[1] >= snake.len:
                         cell[0] = 0
                         cell[1] = 0
                    else:
                        cell[1] += 1
        
    def check_col(self, snake: Snake) -> None:
        col_val = self.grid[snake.pos.y][snake.pos.x][0]
        match col_val:
            case 1:
                self.game_over()
            case 2:
                snake.add_len()
    
    def game_over(self):
        print("Game over!")
        self.running = False
        
    
    def spawn_food(self) -> None:
        if not self.food_flag:
            return
        rand_x = randint(0, self.dimension.x - 1)
        rand_y = randint(0, self.dimension.y - 1)
                
        while self.grid[rand_y][rand_x][0] != 0:
            rand_x = randint(0, self.dimension.x - 1)
            rand_y = randint(0, self.dimension.y - 1)
        
        self.grid[rand_y][rand_x][0] = 2

