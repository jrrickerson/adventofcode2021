import utils


def get_input_data(filename):
    return [line for line in open(filename)]


def part_1(input_data):
    fish = utils.parse_lanternfish(input_data[0])

    final_gen = utils.find_generation_counts(fish, 80)

    return sum(final_gen.values())


def part_2(input_data):
    fish = utils.parse_lanternfish(input_data[0])

    final_gen = utils.find_generation_counts(fish, 256)

    return sum(final_gen.values())


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
        "Solving Puzzle for Day 6:",
        "https://adventofcode.com/2021/day/6")
    print(main("../puzzles/day-06.input"))
