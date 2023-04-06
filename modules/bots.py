from modules.vec import Vec2

def getFoodPos(grid):
    x, y = 0, 0
    for row in grid:
        x = 0
        for cell in row:
            if (cell[0] == 1):
                return Vec2(x, y)
            x += 1
        y += 1
    return Vec2(len(grid[0]),0)
            

class BasicBot():
    def getMove(self, snake, grid):
        # Calculate position of food
        pos_food = getFoodPos(grid)
        print(pos_food)

        # Check if snake is on the same x-coordinate as food
        if (snake.pos.x != pos_food.x):
            dist = pos_food.x - snake.pos.x
            # If already there, keep going in same direction
            if(dist == 0):
                return snake.dir
            
            # Calculate absolute direction
            move_x = int(dist/abs(dist))

            return Vec2(move_x, 0)
        # Check if snake is on the same y-coordinate as food
        else:
            dist = pos_food.y - snake.pos.y
            # If already there, keep going in same direction
            if(dist == 0):
                return snake.dir
            
            # Calculate absolute direction
            move_y = int(dist/abs(dist))

            return Vec2(0, move_y)