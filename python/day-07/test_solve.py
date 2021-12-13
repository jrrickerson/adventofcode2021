import statistics
import solve
import utils


def test_parse_horizontal_positions():
    line = "3,4,3,1,2"

    result = utils.parse_horizontal_positions(line)

    assert result == [3, 4, 3, 1, 2]


def test_parse_horizontal_positions_single_value():
    line = "3"

    result = utils.parse_horizontal_positions(line)

    assert result == [3]


def test_parse_horizontal_positions_empty():
    line = ""

    result = utils.parse_horizontal_positions(line)

    assert result == []


def test_distance_to_median():
    values = [1, 2, 7, 14, 21, 3, 10]
    expected = 39

    total = utils.distance_to_median(values)

    assert total == expected


def test_distance_to_mean():
    values = [1, 2, 7, 14, 21, 3, 10]
    expected = 40

    total = utils.distance_to_mean(values)

    assert total == expected


def test_part1_sample_input():
    input_data = [
        "16,1,2,0,4,2,7,1,2,14"
    ]

    result = solve.part_1(input_data)

    assert result == 37


def test_nth_triangular_zero():
    x = 0
    result = utils.nth_triangular(x)

    assert result == 0


def test_nth_triangular():
    x = 11
    result = utils.nth_triangular(x)

    assert result == 66


def test_nth_triangular_distances():
    numbers = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    value = 5
    result = utils.nth_triangular_distances(numbers, value)

    assert result == [66, 10, 6, 15, 1, 6, 3, 10, 6, 45]


def test_weighted_mean_equal_weights():
    numbers = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    weights = [1] * len(numbers)

    result = utils.weighted_mean(numbers, weights)

    assert result == statistics.mean(numbers)


def test_weighted_mean_skewed_weights():
    numbers = [5, 5, 5, 10]
    weights = [1, 1, 1, 3]
    expected = 7.5

    result = utils.weighted_mean(numbers, weights)

    assert result == expected


def test_part2_sample_input():
    input_data = [
        "16,1,2,0,4,2,7,1,2,14"
    ]

    result = solve.part_2(input_data)

    assert result == 168
