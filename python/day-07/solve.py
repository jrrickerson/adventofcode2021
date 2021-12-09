import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    positions = utils.parse_horizontal_positions(input_data[0])
    spent_fuel = utils.distance_to_median(positions)

    return spent_fuel


def part_2(input_data):
    pass


def main(input_file):
    input_data = get_input_data(input_file)

    part_1_result = part_1(input_data)
    part_2_result = part_2(input_data)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":
    print(
        "Solving Puzzle for Day 7:",
        "https://adventofcode.com/2021/day/7")
    print(main("../puzzles/day-07.input"))
