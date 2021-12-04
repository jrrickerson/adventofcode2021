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

    most_common = utils.most_common_bits(bit_lists)
    # Flip the bits to get the least common ones
    least_common = [0 if i else 1 for i in most_common]

    gamma = sum([2**exp * b for exp, b in enumerate(most_common[::-1])])
    epsilon = sum([2**exp * b for exp, b in enumerate(least_common[::-1])])

    return gamma * epsilon


def part_2(binary_strings):
    bit_lists = [
        utils.bit_list(bin_string)
        for bin_string in binary_strings]

    oxygen_values = bit_lists.copy()
    bit_pos = 0
    while len(oxygen_values) > 1:
        most_common = utils.most_common(
            [bit[bit_pos] for bit in oxygen_values])
        filter_val = 1 if len(most_common) > 1 else most_common[0]
        print(f"Bit {bit_pos} most common {filter_val}")
        oxygen_values = [
            bits for bits in oxygen_values if bits[bit_pos] == filter_val]
        print(oxygen_values)
        bit_pos += 1

    oxygen_generator_rating = sum(
        [2**exp * b for exp, b in enumerate(oxygen_values[0][::-1])])
    print("Oxygen:", oxygen_generator_rating)

    co2_values = bit_lists.copy()
    bit_pos = 0
    while len(co2_values) > 1:
        most_common = utils.most_common([bit[bit_pos] for bit in co2_values])
        filter_val = 1 if len(most_common) > 1 else most_common[0]
        # Flip the bit to get least common value
        filter_val = filter_val ^ 1
        print(f"Bit {bit_pos} most common {filter_val}")
        co2_values = [
            bits for bits in co2_values if bits[bit_pos] == filter_val]
        bit_pos += 1

    co2_scrubber_rating = sum(
        [2**exp * b for exp, b in enumerate(co2_values[0][::-1])])
    print("CO2:", co2_scrubber_rating)

    return oxygen_generator_rating * co2_scrubber_rating


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
