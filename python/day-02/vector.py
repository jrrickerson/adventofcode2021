class Vector2:
    """Two-dimensional vector for doing basic calculations
       because vector math is fun, right?"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def scale(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)


VECTOR_COMMAND_MAP = {
    "down": Vector2(0, 1),
    "up": Vector2(0, -1),
    "forward": Vector2(1, 0),
    "reverse": Vector2(-1, 0),
}


