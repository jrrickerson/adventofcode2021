import math


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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def scale(self, scalar):
        """Scale the vector by a scalar value"""
        return Vector2(self.x * scalar, self.y * scalar)

    def cross(self, other):
        """Calculate the signed magnitude of the cross product of
        2D vectors, with the z coordinates assumed to be 0"""
        return (self.x * other.y) - (self.y * other.x)

    def cross_to(self, vec_A, vec_B):
        """Calculate the cross product of the 2D vectors from the
        current vector as the point of origin to vec_A and vec_B.
        This returns 0 if all three points are on the same line."""
        return (vec_A - self).cross(vec_B - self)

    @property
    def magnitude(self):
        return abs(math.sqrt(self.x ** 2 + self.y ** 2))
