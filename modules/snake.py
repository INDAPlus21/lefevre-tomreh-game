from modules.vec import Vec2
from modules.controls import Controlscheme
import queue
from random import randint


class Snake:
    def __init__(self, id) -> None:
        self.scheme = Controlscheme(id)
        self.pos = Vec2(randint(0, 5), randint(0, 5))
        self.len = 0
        self.dir = Vec2(0, 1)
        if id < 0:
            print("Invalid id, must be positive")
            raise ValueError
        self.id = id + 2
        self.buffer = queue.Queue(2)
        self.event_flag = False

    def event_handle(self, event) -> None:
        if not self.event_flag:
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
            if not self.buffer.full():
                self.buffer.put_nowait(event)
            else:
                self.buffer.get_nowait()
                self.buffer.put_nowait(event)

        self.event_flag = True

    def bufferless_event(self, event):
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
        if not self.buffer.empty() and self.event_flag:
            self.bufferless_event(self.buffer.get_nowait())

        self.pos += self.dir
        if self.pos.x < 0 or self.pos.y < 0:
            return False

        if self.pos.x >= x or self.pos.y >= y:
            return False

        self.evented_done = False
        return True

    def add_len(self) -> None:
        self.len += 1
