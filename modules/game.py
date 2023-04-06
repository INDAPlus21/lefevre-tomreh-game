from modules.vec import Vec2
from modules.snake import Snake
import pygame
from random import randint
from modules.renderer import Renderer
from modules.scenes import Scene

DOWN = Vec2(0, 1)
UP = Vec2(0, -1)
LEFT = Vec2(-1, 0)
RIGHT = Vec2(1, 0)

"""
Game Grid

The grid consists of two-element lists for each coordinate
The first element in this list represents the type of game object where:
    0: Nothing
    1: Food
    >1: Snakes (typically 2 and 3, but supports more)
The second element in this list represents which part of the game object:
    For example, the head of a snake is represented by 0 and the remaining tail is 1,2...
"""

class Game:
    def __init__(self, x, y, w, h) -> None:
        """
        Initializes an instance of the class.

        Args:
            x: An integer representing the x dimension of the grid.
            y: An integer representing the y dimension of the grid.
            w: An integer representing the width of the game window.
            h: An integer representing the height of the game window.
        """
        self.dimension = Vec2(x, y)
        self.grid = [[[0, 0] for i in range(x)] for j in range(y)]
        self.snakes = [Snake(0), Snake(1)]
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.running = True
        self.food_flag = True
        self.scene_select = Scene(0)
        self.renderer = Renderer(w, h, (self.dimension.x, self.dimension.y))
        self.snakes_used = 1


    def __repr__(self) -> str:
        """
        Returns a string representation of the object, showing the contents of the grid
        """
        out = ""
        for row in self.grid:
            out += "|"
            for cell in row:
                out += f"{cell[0]},{cell[1]}|"
            out += "\n"

        return out


    def run(self) -> None:
        """
        The main game loop, runs the current scene
        """
        while self.running:
            # Get any events that have occured
            events = pygame.event.get()

            match self.scene_select:
                case Scene.MAINMENU:
                    self.scene_select = self.renderer.draw_menu(events)
                case Scene.SINGLEPLAYER:
                    self.snakes_used = 1
                    self.scene_select = self.game(events, self.scene_select)
                    self.renderer.draw_game(self.grid)
                case Scene.MULTIPLAYER:
                    self.snakes_used = 2
                    self.scene_select = self.game(events, self.scene_select)
                    self.renderer.draw_game(self.grid)
                case Scene.GAMEOVER:
                    self.scene_select = self.renderer.draw_end(
                        events, self.loser)


    def add_snake(self):
        """
        Adds a snake to the list of snakes
        """
        self.snakes.append(Snake(self.id))
        self.id += 1


    def game(self, events, state):
        """
        Game loop
        
        Args:
            events: A list of events
            state: The current scene state
            
        Returns:
            bool: Next game state
        """
        # Handle events
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # KEKW optimaztion
                if event.key > 5000:
                    self.snakes[0].event_handle(event)
                else:
                    self.snakes[1].event_handle(event)

        # Update snake positions
        gameRunningFlag = True
        for snake in self.snakes[0:self.snakes_used]:
            if not snake.update(self.dimension.x, self.dimension.y):
                self.game_over(snake.id - 2)
                state = Scene.GAMEOVER
                gameRunningFlag = False

        # Prepare for next frame
        if gameRunningFlag:
            # Cleaning grid from old snake positions and check if more food needs to be spawned
            self.clean_grid(self.snakes)
            # Check the next positions for the snakes
            if self.put_snakes(self.snakes[0:self.snakes_used]):
                # Spawn food
                self.spawn_food()
                self.renderer.draw_game(self.grid)
                self.clock.tick(self.FPS)
            else:
                state = Scene.GAMEOVER

        return state


    def get_inverse_snake(self, snakeid):
        """
        Returns the id of the other snake in the game.
        
        Args:
            snakeid: id of known snake
        """
        if self.snakes_used == 1:
            return snakeid
        else:
            return self.snakes[snakeid - 1].id


    def put_snakes(self, snakes) -> None:
        """
        Checks the next position for each snake, performing the relevant logic
        
        Args:
            snakes: A list of snakes.
        """
        for snake in snakes:
            slot = self.grid[snake.pos.y][snake.pos.x]
            match slot[0]: 
                # If the space is empty
                case 0: 
                    self.grid[snake.pos.y][snake.pos.x] = [snake.id, 0]
                # If the space is a fruit
                case 1:
                    snake.add_len()
                    self.grid[snake.pos.y][snake.pos.x] = [snake.id, 0]
                # If the space is a snake, causing a collision
                case _:
                    # Head to body collsion, other snake wins game
                    if slot[1] != 0:
                        self.game_over(self.get_inverse_snake(slot[0] - 2))
                        return False
                    # Head to head collision, draw
                    else:
                        self.game_over(2)
                        return False
        return True
    

    def clean_grid(self, snakes):
        """
        Checks and clears the current state of the grid.
        
        Args:
            snakes: A list of snakes.
        """
        self.food_flag = True
        # Iterate over each cell in the grid
        for row in self.grid:
            for cell in row:
                # Extract the id and index values from the cell
                id_val = cell[0]
                index_val = cell[1]

                # Check if the cell contains food
                if id_val < 2:
                    # If it does, set the food flag to False
                    if id_val == 1:
                        self.food_flag = False
                else:
                    # If it doesn't, check if the snake at index id_val - 2 has reached the cell
                    if index_val >= snakes[id_val - 2].len:
                        # If it has, reset the cell to an empty state
                        cell[0] = 0
                        cell[1] = 0
                    else:
                        # If it hasn't, move the snake one step forward
                        cell[1] += 1


    def game_over(self, loser) -> None:
        """
        Reset grid upon game over.
        
        Args:
            loser: the losing snake.
        """
        self.reset(loser)


    def reset(self, loser):
        """
        Reset game environment.
        
        Args:
            loser: the losing snake of the previous game.
        """
        # Reset grid to [0,0] on each position
        self.grid = [[[0, 0] for _ in range(
            self.dimension.x)] for _ in range(self.dimension.y)]
        # Reset snakes
        self.snakes = [Snake(0), Snake(1)]
        self.loser = loser


    def spawn_food(self) -> None:
        """
        Spawn food on a random empty location on the grid if no food is on the grid
        """
        if not self.food_flag:
            return
        rand_x = randint(0, self.dimension.x - 1)
        rand_y = randint(0, self.dimension.y - 1)

        while self.grid[rand_y][rand_x][0] != 0:
            rand_x = randint(0, self.dimension.x - 1)
            rand_y = randint(0, self.dimension.y - 1)

        self.grid[rand_y][rand_x][0] = 1
