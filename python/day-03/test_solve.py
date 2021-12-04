import solve
import utils


def test_binary_digits_to_places_zero():
    bin_string = "00000"
    expected = []

    places = utils.binary_digits_to_places(bin_string)

    assert places == expected


def test_binary_digits_to_places_single_bit():
    bin_string = "00001"
    expected = [1]

    places = utils.binary_digits_to_places(bin_string)

    assert places == expected


def test_binary_digits_to_places_multiple_bits():
    bin_string = "01011"
    expected = [1, 2, 8]

    places = utils.binary_digits_to_places(bin_string)

    assert places == expected


def test_binary_digits_to_places_all_bits():
    bin_string = "11111"
    expected = [1, 2, 4, 8, 16]

    places = utils.binary_digits_to_places(bin_string)

    assert places == expected


def test_count_bits_by_place_empty():
    places_list = []
    expected = {}

    counts = utils.count_bits_by_place(places_list)

    assert counts == expected


def test_count_bits_by_place():
    places_list = [1, 2, 4, 8, 2, 8, 4, 16]
    expected = {
        1: 1,
        2: 2,
        4: 2,
        8: 2,
        16: 1
    }

    counts = utils.count_bits_by_place(places_list)

    assert counts == expected


def test_count_bits_by_same_place():
    places_list = [2, 2, 2, 2, 2, 2, 2, 2]
    expected = {
        2: 8,
    }

    counts = utils.count_bits_by_place(places_list)

    assert counts == expected


def test_bitwise_not_zero():
    val = 0
    expected = 1

    result = utils.bitwise_not(val)

    assert result == expected


def test_bitwise_not_all_ones():
    val = 255
    expected = 0

    result = utils.bitwise_not(val)

    assert result == expected


def test_bitwise_not_force_bit_size():
    val = 7
    expected = 248

    result = utils.bitwise_not(val, bitsize=8)

    assert result == expected


def test_part1_sample_input():
    binary_strings = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    result = solve.part_1(binary_strings)

    assert result == 198


def most_common_empty_iterable():
    values = []
    expected = None

    result = utils.most_common(values)

    assert result == expected


def most_common_single_value():
    values = [
        1, 0, 1, 1, 0, 1, 1, 0]
    expected = [1]

    result = utils.most_common(values)

    assert result == expected


def test_most_common_bits():
    bit_lists = [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    expected = [1, 0, 1, 1, 0]

    result = utils.most_common_bits(bit_lists)

    assert result == expected


def test_filter_by_places_no_filter():
    places = [1, 2, 4, 8]
    places_lists = [
        [1],
        [2, 8],
        [1, 4],
        [8]
    ]
    filter_places = []
    expected = [1]

    results = utils.filter_by_places(places_lists, places, filter_places)

    assert results == expected


def test_filter_by_places_single_place_filter():
    places = [1, 2, 4, 8]
    places_lists = [
        [1, 2],
        [2, 8],
        [1, 4],
        [8]
    ]
    filter_places = [8]
    expected = [8]

    results = utils.filter_by_places(places_lists, places, filter_places)

    assert results == expected


def test_filter_by_places_multi_place_filter():
    places = [1, 2, 4, 8]
    places_lists = [
        [1, 2],
        [2, 8],
        [1, 4],
        [8]
    ]
    filter_places = [2, 4]
    expected = [1, 4]

    results = utils.filter_by_places(places_lists, places, filter_places)

    assert results == expected


def test_part2_sample_input():
    binary_strings = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    result = solve.part_2(binary_strings)

    assert result == 230
