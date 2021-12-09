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
