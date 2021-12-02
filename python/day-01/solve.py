from utils import load_depth_list, count_increases, sliding_windows


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
