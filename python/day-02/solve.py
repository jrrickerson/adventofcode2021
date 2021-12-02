

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


def command_to_vector2(command):
    """Given a text command, create a 2-dimensional vector with the appropriate
    direction and magnitude"""
    try:
        direction, magnitude = command.strip().split()
    except Exception:
        print("Failed to parse:", command)
    vector = VECTOR_COMMAND_MAP[direction]
    vector = vector.scale(int(magnitude))
    return vector


def part_1(input_file):
    """Convert all the text input commands to 2-dimensional vectors, with
    the postive/negative values determined by the command name, and sum the
    vectors to get the final position."""
    start_vector = Vector2(0, 0)
    commands = [line.strip() for line in open(input_file) if line.strip()]
    vectors = [command_to_vector2(command) for command in commands]
    end_vector = sum(vectors, start=start_vector)

    return end_vector.x * end_vector.y


def part_2(input_file):
    pass


def main(input_filename):
    part_1_result = part_1(input_filename)
    part_2_result = part_2(input_filename)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":
    print("Solving Puzzle for Day 2:", "https://adventofcode.com/2021/day/2")
    print(main("../puzzles/day-02.input"))
