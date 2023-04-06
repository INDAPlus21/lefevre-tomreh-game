class Vec2:
    def __init__(self, x, y):
        """
        Initializes vector2 class
        
        Args:
            x: x-position.
            y: y-position.
        """
        self.x = x
        self.y = y
        
    def __add__(self, other):
        """
        Adds together two Vec2 classes.
        
        Args:
            other: another instance of Vec2.

        Returns:
            Vec2: instance with the values added together.
        """
        x = self.x + other.x
        y = self.y + other.y
        
        return Vec2(x, y)
        
    def __repr__(self):
        """
        Return a string representation of the object, format: x,y
        """
        return f"{self.x}, {self.y}"
    
    def __eq__(self, __o: object) -> bool:
        """
        Checks if two instances of Vec2 have equal values
        
        Args:
            __o: another instance of Vec2
        
        Returns:
            bool: result of equals operation
        """
        return self.x == __o.x and self.y == __o.y