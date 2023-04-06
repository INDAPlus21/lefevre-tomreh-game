from modules.vec import Vec2
from modules.controls import Controlscheme
import queue
from random import randint


class Snake:
    def __init__(self, id) -> None:
        """
        Initializes a Snake object.

        Args:
            id: The id of the snake.

        Raises:
            ValueError: If the given id is not a positive integer.
        """
        # Initialize instance variables
        self.scheme = Controlscheme(id)
        self.pos = Vec2(randint(0, 5), randint(0, 5))
        self.len = 0
        self.dir = Vec2(0, 1)
        self.isBot = False
        self.score = 0

        # Check if id is positive integer
        if id < 0:
            print("Invalid id, must be positive")
            raise ValueError

        self.id = id + 2
        self.buffer = queue.Queue(2)
        self.event_flag = False


    def event_handle(self, event) -> None:
        """
        Handles events that affect the game, such as keyboard inputs.

        Args:
            event: The event to be handled.
        """
        # If the event flag is False, check the type of the event
        if not self.event_flag:
            # Prohibit player input if snake is bot
            if (not self.isBot):
                # Match the key of the event with the corresponding case and update the direction of the snake accordingly
                match event.key:
                    case self.scheme.down:
                        if self.dir != Vec2(0, -1):
                            self.dir = Vec2(0,  1)
                    case self.scheme.up:
                        if self.dir != Vec2(0,  1):
                            self.dir = Vec2(0, -1)
                    case self.scheme.right:
                        if self.dir != Vec2(-1, 0):
                            self.dir = Vec2(1,  0)
                    case self.scheme.left:
                        if self.dir != Vec2(1,  0):
                            self.dir = Vec2(-1,  0)
        else:
            # If the event flag is True, put the event in the buffer if it is not full
            if not self.buffer.full():
                self.buffer.put_nowait(event)
            # If the buffer is full, remove the oldest event from the buffer and add the new event
            else:
                self.buffer.get_nowait()
                self.buffer.put_nowait(event)

        # Set the event flag to True
        self.event_flag = True


    def bufferless_event(self, event):
        """
        Handles events in case the buffer is empty.

        Args:
            event: The event to be handled.
        """
        
        # Prohibit player input if snake is a bot
        if(not self.isBot):
            # Match the key of the event with the corresponding case and update the direction of the snake accordingly
            match event.key:
                case self.scheme.down:
                    if self.dir != Vec2(0, -1):
                        self.dir = Vec2(0,  1)
                case self.scheme.up:
                    if self.dir != Vec2(0,  1):
                        self.dir = Vec2(0, -1)
                case self.scheme.right:
                    if self.dir != Vec2(-1, 0):
                        self.dir = Vec2(1,  0)
                case self.scheme.left:
                    if self.dir != Vec2(1,  0):
                        self.dir = Vec2(-1,  0)


    def update(self, x, y) -> bool:
        """
        Updates the state of the game after each frame.

        Args:
            x: The width of the game screen.
            y: The height of the game screen.

        Returns:
            A boolean value indicating if the update was successful.
        """
        # If the buffer is not empty and the event flag is True, handle the event
        if not self.buffer.empty() and self.event_flag:
            self.bufferless_event(self.buffer.get_nowait())

        # Update the position of the snake based on the current direction
        self.pos += self.dir

        # If the position of the snake is outside the boundaries of the game screen, return False
        if self.pos.x < 0 or self.pos.y < 0:
            return False
        if self.pos.x >= x or self.pos.y >= y:
            return False

        # Set the evented_done flag to False and return True
        self.evented_done = False
        return True


    def add_len(self) -> None:
        """
        Adds one length and score to the snake.
        """
        self.len += 1
        self.score += 1

        color = ["BLUE", "RED"]
        print(color[self.id - 2], "scored!")
