import itertools
import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(binary_strings):
    """Count most common bit places in a list of binary strings to
    find the gamma rate, and find the epsilon rate as the 2's compliment"""
    half = len(binary_strings) // 2
    bit_length = len(binary_strings[0])
    places_lists = [
        utils.binary_digits_to_places(bin_string)
        for bin_string in binary_strings]
    all_lists = itertools.chain(*places_lists)
    bit_counts = utils.count_bits_by_place(all_lists)

    # There are only two possibilities (1 and 0), so if the count for a place
    # exceeds half of the total list of strings, 1 is more common than 0
    most_common = [
        place for place in bit_counts.keys() if bit_counts[place] > half]

    gamma = sum(most_common)
    print("Gamma", gamma, "=", bin(gamma))
    # Flip the bits to get the least common ones
    epsilon = utils.bitwise_not(gamma, bitsize=bit_length)

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
