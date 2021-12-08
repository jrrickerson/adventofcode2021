from collections import Counter
import itertools
import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename) if line.strip()]


def part_1(input_data):
    segments = []
    # Parse and filter out any segments that are not
    # horizontal or vertical
    for line in input_data:
        segment = utils.parse_vector_pairs(line)
        # Skip zero-length segments
        if not utils.is_nonzero_segment(*segment):
            continue
        # Skip non-vertical and non-horizontal segments
        if not (utils.is_horizontal_segment(*segment) or
                utils.is_vertical_segment(*segment)):
            continue
        if segment in segments:
            print("Repeat segment!")
        segments.append(segment)

    # Find all unique pairs of segments and test for intersections
    # Keep an index of intersection points and counts
    intersection_points = Counter()
    for segment_pair in itertools.combinations(segments, 2):
        intersections = utils.intersections(*segment_pair)
        if len(intersections) > 1:
            print(f"Overlap: {len(intersections)} - {segment_pair}")
        for point in intersections:
            intersection_points[point] += 1
    #print(intersection_points.most_common(10))
    return len(intersection_points)


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
        "Solving Puzzle for Day 5:",
        "https://adventofcode.com/2021/day/5")
    print(main("../puzzles/day-05.input"))
