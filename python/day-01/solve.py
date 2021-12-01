

def sliding_windows(measurement_list, window=3):
    sums = []
    if len(measurement_list) < window:
        return sums
    for i in range(0, len(measurement_list)):
        window_list = measurement_list[i:i+window]
        if len(window_list) < window:
            break
        window_sum = sum(window_list)
        sums.append(window_sum)
    return sums


def load_depth_list(file_obj):
    return [int(line.strip()) for line in file_obj if line.strip()]


def count_increases(value_list):
    if not value_list:
        return 0

    previous = None
    count = 0
    for item in value_list:
        if previous is not None and previous < item:
            count += 1
        previous = item
    return count


def part_1(input_file):
    depth_list = load_depth_list(open(input_file))
    increases = count_increases(depth_list)
    return increases


def part_2(input_file):
    depth_list = load_depth_list(open(input_file))
    windows = sliding_windows(depth_list, window=3)
    increases = count_increases(windows)
    return increases


def main(filename):
    part_1_result = part_1(filename)
    part_2_result = part_2(filename)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":
    print("Solving Puzzle for Day 1:", "https://adventofcode.com/2021/day/1")
    print(main("../puzzles/day-01.input"))
