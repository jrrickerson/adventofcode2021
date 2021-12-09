import solve
import utils


def test_parse_lanternfish():
    line = "3,4,3,1,2"

    result = utils.parse_lanternfish(line)

    assert result == [3, 4, 3, 1, 2]


def test_parse_lanternfish_single_fish():
    line = "3"

    result = utils.parse_lanternfish(line)

    assert result == [3]


def test_parse_lanternfish_empty():
    line = ""

    result = utils.parse_lanternfish(line)

    assert result == []


def test_next_generation_decrements_timers():
    fish = [3, 4, 3, 1, 2]

    next_gen = utils.next_generation(fish)

    for i, f in enumerate(fish):
        assert next_gen[i] == f - 1


def test_next_generation_resets_expired_timers():
    fish = [2, 3, 2, 0, 1]

    next_gen = utils.next_generation(fish)

    for i, f in enumerate(fish):
        if f == 0:
            assert next_gen[i] == utils.LANTERNFISH_RESET
        else:
            assert next_gen[i] == f - 1


def test_next_generation_appends_new():
    fish = [2, 3, 2, 0, 1]

    next_gen = utils.next_generation(fish)

    assert len(next_gen) == len(fish) + 1
    assert next_gen[-1] == utils.LANTERNFISH_NEW


def test_find_generation_default():
    fish = [3, 4, 3, 1, 2]

    next_gen = utils.find_generation(fish)

    assert next_gen == [2, 3, 2, 0, 1]


def test_find_generation_specific_generation():
    fish = [3, 4, 3, 1, 2]

    next_gen = utils.find_generation(fish, forward=10)

    assert next_gen == [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8]


def test_part1_sample_input():
    input_data = ["3,4,3,1,2"]

    result = solve.part_1(input_data)

    assert result == 5934
