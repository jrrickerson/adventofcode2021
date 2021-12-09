import solve
import utils
import vector


def test_parse_vector_pairs_empty_line():
    line = ""

    v1, v2 = utils.parse_vector_pairs(line)

    assert v1 is None
    assert v2 is None


def test_parse_vector_pairs_ignore_whitespace():
    line = "   0,9   ->       5,9  "
    expected_v1 = vector.Vector2(0, 9)
    expected_v2 = vector.Vector2(5, 9)

    v1, v2 = utils.parse_vector_pairs(line)

    assert v1 == expected_v1
    assert v2 == expected_v2


def test_is_horizontal_segment_same_y():
    v1 = vector.Vector2(0, 9)
    v2 = vector.Vector2(5, 9)

    result = utils.is_horizontal_segment(v1, v2)

    assert result is True


def test_is_horizontal_segment_different_y():
    v1 = vector.Vector2(0, 9)
    v2 = vector.Vector2(5, 11)

    result = utils.is_horizontal_segment(v1, v2)

    assert result is False


def test_is_vertical_segment_same_x():
    v1 = vector.Vector2(2, 2)
    v2 = vector.Vector2(2, 1)

    result = utils.is_vertical_segment(v1, v2)

    assert result is True


def test_is_vertical_segment_different_x():
    v1 = vector.Vector2(0, 8)
    v2 = vector.Vector2(8, 0)

    result = utils.is_vertical_segment(v1, v2)

    assert result is False


def test_is_nonzero_segment_same_endpoints():
    v1 = vector.Vector2(0, 8)
    v2 = vector.Vector2(0, 8)

    result = utils.is_nonzero_segment(v1, v2)

    assert result is False


def test_is_nonzero_segment_different_endpoints():
    v1 = vector.Vector2(0, 8)
    v2 = vector.Vector2(8, 0)

    result = utils.is_nonzero_segment(v1, v2)

    assert result is True


def test_overlapping_horizontal_no_points():
    segment_a = (vector.Vector2(0, 9), vector.Vector2(5, 9))
    segment_b = (vector.Vector2(6, 9), vector.Vector2(8, 9))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 0


def test_overlapping_horizontal_multiple_points():
    # Overlap at x = (3, 4, 5)
    segment_a = (vector.Vector2(0, 9), vector.Vector2(5, 9))
    segment_b = (vector.Vector2(3, 9), vector.Vector2(8, 9))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 3
    assert all([(x, 9) in points for x in range(3, 6)])


def test_overlapping_horizontal_subsegment():
    # Overlap at x = (0, 1, 2)
    segment_a = (vector.Vector2(0, 9), vector.Vector2(5, 9))
    segment_b = (vector.Vector2(0, 9), vector.Vector2(2, 9))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 3
    assert all([(x, 9) in points for x in range(0, 3)])


def test_overlapping_horizontal_single_endpoint():
    segment_a = (vector.Vector2(0, 9), vector.Vector2(5, 9))
    segment_b = (vector.Vector2(5, 9), vector.Vector2(8, 9))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 1
    assert (5, 9) in points


def test_overlapping_vertical_no_points():
    segment_a = (vector.Vector2(9, 0), vector.Vector2(9, 5))
    segment_b = (vector.Vector2(9, 6), vector.Vector2(9, 8))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 0


def test_overlapping_vertical_multiple_points():
    # Overlap at y = (3, 4, 5)
    segment_a = (vector.Vector2(9, 0), vector.Vector2(9, 5))
    segment_b = (vector.Vector2(9, 3), vector.Vector2(9, 8))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 3
    assert all([(9, y) in points for y in range(3, 6)])


def test_overlapping_vertical_single_endpoint():
    segment_a = (vector.Vector2(9, 0), vector.Vector2(9, 5))
    segment_b = (vector.Vector2(9, 5), vector.Vector2(9, 8))

    points = utils.overlapping(segment_a, segment_b)

    assert len(points) == 1
    assert (9, 5) in points


def test_intersections_parallel_segments():
    segment_a = (vector.Vector2(0, 5), vector.Vector2(0, 9))
    segment_b = (vector.Vector2(3, 2), vector.Vector2(3, 12))

    points = utils.intersections(segment_a, segment_b)

    assert len(points) == 0


def test_intersections_perpendicular_segments():
    segment_a = (vector.Vector2(1, 5), vector.Vector2(1, 9))
    segment_b = (vector.Vector2(0, 6), vector.Vector2(4, 6))

    points = utils.intersections(segment_a, segment_b)

    assert len(points) == 1
    assert (1, 6) in points


def test_intersections_overlapping_segments():
    # Overlap at y = (3, 4, 5)
    segment_a = (vector.Vector2(9, 0), vector.Vector2(9, 5))
    segment_b = (vector.Vector2(9, 3), vector.Vector2(9, 8))

    points = utils.intersections(segment_a, segment_b)

    assert len(points) == 3
    assert all([(9, y) in points for y in range(3, 6)])


def test_intersections_diagonal_segments():
    segment_a = (vector.Vector2(1, 1), vector.Vector2(5, 5))
    segment_b = (vector.Vector2(5, 1), vector.Vector2(1, 5))

    points = utils.intersections(segment_a, segment_b)

    assert len(points) == 1
    assert (3, 3) in points


def test_intersections_overlapping_diagonal_segments():
    segment_a = (vector.Vector2(1, 1), vector.Vector2(4, 4))
    segment_b = (vector.Vector2(6, 6), vector.Vector2(3, 3))

    points = utils.intersections(segment_a, segment_b)

    assert len(points) == 2
    assert (3, 3) in points
    assert (4, 4) in points


def test_part1_sample_input():
    input_lines = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]

    result = solve.part_1(input_lines)

    assert result == 5


def test_slope_zero():
    v1 = vector.Vector2(0, 0)
    v2 = vector.Vector2(5, 0)

    slope = utils.slope(v1, v2)

    assert slope == 0


def test_slope_positive():
    v1 = vector.Vector2(0, 0)
    v2 = vector.Vector2(5, 5)

    slope = utils.slope(v1, v2)

    assert slope == 1


def test_slope_negative():
    v1 = vector.Vector2(9, 7)
    v2 = vector.Vector2(7, 9)

    slope = utils.slope(v1, v2)

    assert slope == -1


def test_is_diagonal_increasing_slope():
    v1 = vector.Vector2(0, 0)
    v2 = vector.Vector2(5, 5)

    result = utils.is_diagonal_segment(v1, v2)

    assert result is True


def test_is_diagonal_non_matching_coordinates():
    v1 = vector.Vector2(0, 1)
    v2 = vector.Vector2(5, 7)

    result = utils.is_diagonal_segment(v1, v2)

    assert result is False


def test_part2_sample_input():
    input_lines = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]

    result = solve.part_2(input_lines)

    assert result == 12
