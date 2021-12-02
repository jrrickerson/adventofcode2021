from vector import Vector2
from utils import command_to_vector2


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
