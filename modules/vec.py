class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        
        return Vec2(x, y)
        
    def __repr__(self):
        return f"{self.x}, {self.y}"
    
    def __eq__(self, __o: object) -> bool:
        if self.x == __o.x and self.y == __o.y:
            return True
        else:
            return False