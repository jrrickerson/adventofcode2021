import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    """Count outputs that MUST be 1, 4, 7, 8, by length of the output"""
    digit_count = 0
    for line in input_data:
        signals, outputs = utils.parse_signal_data(line)
        for output_value in outputs:
            digits = utils.translate_by_count(output_value)
            if any([i in digits for i in (1, 4, 7, 8)]):
                digit_count += 1

    return digit_count


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
        "Solving Puzzle for Day 8:",
        "https://adventofcode.com/2021/day/8")
    print(main("../puzzles/day-08.input"))
