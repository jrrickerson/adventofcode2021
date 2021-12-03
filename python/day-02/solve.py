from vector import Vector2
from utils import command_to_vector2, command_to_pos_aim_vectors


def get_commands(input_file):
    commands = [line.strip() for line in open(input_file) if line.strip()]
    return commands


def part_1(commands):
    """Convert all the text input commands to 2-dimensional vectors, with
    the postive/negative values determined by the command name, and sum the
    vectors to get the final position."""
    start_vector = Vector2(0, 0)
    vectors = [command_to_vector2(command) for command in commands]
    end_vector = sum(vectors, start=start_vector)

    return end_vector.x * end_vector.y


def part_2(commands):
    """Convert all text input commands to tuples of 2-dimensional vectors
    to apply to the current position and aim vectors.  Scale the aim
    by the magnitude of the position vector and add to the postion vector
    to increase or decrease depth.
    NOTE:  The "down" and "up" commands translate to position vectors with
    a magnitude of 0, so they will not affect the current position."""
    position = Vector2(0, 0)
    aim = Vector2(0, 0)
    deltas = [command_to_pos_aim_vectors(command) for command in commands]
    for pos_delta, aim_delta in deltas:
        aim += aim_delta
        position += pos_delta + aim.scale(pos_delta.magnitude)

    return position.x * position.y


def main(input_filename):
    commands = [line.strip() for line in open(input_filename) if line.strip()]
    part_1_result = part_1(commands)
    part_2_result = part_2(commands)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":
    print("Solving Puzzle for Day 2:", "https://adventofcode.com/2021/day/2")
    print(main("../puzzles/day-02.input"))
