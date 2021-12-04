import itertools
import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(binary_strings):
    """Count most common bit places in a list of binary strings to
    find the gamma rate, and find the epsilon rate as the inverse of the
    bits"""
    bit_lists = [
        utils.bit_list(bin_string)
        for bin_string in binary_strings]

    # There are only two possibilities (1 and 0), so if the count for a place
    # exceeds half of the total list of entries, 1 is more common than 0
    most_common = utils.most_common_bits(bit_lists)
    least_common = [0 if i else 1 for i in most_common]

    gamma = sum([2**exp * b for exp, b in enumerate(most_common[::-1])])
    # Flip the bits to get the least common ones
    epsilon = sum([2**exp * b for exp, b in enumerate(least_common[::-1])])

    return gamma * epsilon


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
        "Solving Puzzle for Day 3:",
        "https://adventofcode.com/2021/day/3")
    print(main("../puzzles/day-03.input"))
