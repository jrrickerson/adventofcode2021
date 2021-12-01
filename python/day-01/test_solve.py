import io
import solve


def test_count_increases_empty_list():
    depth_list = []

    increases = solve.count_increases(depth_list)

    assert 0 == increases


def test_count_increases_single_increase():
    depth_list = [0, 100]

    increases = solve.count_increases(depth_list)

    assert 1 == increases


def test_count_increases_single_decrease():
    depth_list = [100, 0]

    increases = solve.count_increases(depth_list)

    assert 0 == increases


def test_count_increases_single_value_zero_increases():
    depth_list = [100]

    increases = solve.count_increases(depth_list)

    assert 0 == increases


def test_count_increases_all_increases():
    depth_list = [100, 101, 102, 103, 104, 105]

    increases = solve.count_increases(depth_list)

    assert len(depth_list) - 1 == increases


def test_count_increases_all_decreases():
    depth_list = reversed([100, 101, 102, 103, 104, 105])

    increases = solve.count_increases(depth_list)

    assert 0 == increases


def test_part_1_sample_input():
    depth_list = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]

    increases = solve.count_increases(depth_list)

    assert 7 == increases


def test_load_depth_list_empty_file():
    file_obj = io.StringIO("")

    depth_list = solve.load_depth_list(file_obj)

    assert depth_list == []


def test_load_depth_list_single_line():
    file_obj = io.StringIO("100")

    depth_list = solve.load_depth_list(file_obj)

    assert depth_list == [100]


def test_load_depth_list_multi_line():
    file_obj = io.StringIO("""100
    200
    300
    400
    500""")

    depth_list = solve.load_depth_list(file_obj)

    assert depth_list == [100, 200, 300, 400, 500]


def test_load_depth_list_ignore_empty_lines():
    file_obj = io.StringIO("""100
    200

    300
    400

    500""")

    depth_list = solve.load_depth_list(file_obj)

    assert depth_list == [100, 200, 300, 400, 500]


def test_sliding_windows_empty_list():
    measurements = []

    sums = solve.sliding_windows(measurements)

    assert sums == []


def test_sliding_windows_not_enough_measurements():
    measurements = [100, 200]

    sums = solve.sliding_windows(measurements, window=3)

    assert sums == []


def test_sliding_windows_sum_of_measurements():
    measurements = [100, 200, 300]

    sums = solve.sliding_windows(measurements, window=3)

    assert sums == [600]


def test_sliding_windows_sum_per_window():
    measurements = [100, 200, 300, 10]

    sums = solve.sliding_windows(measurements, window=3)

    assert sums == [600, 510]


def test_sliding_windows_extra_measurements_ignored():
    measurements = [100, 200, 300, 10, 20]

    sums = solve.sliding_windows(measurements, window=3)

    assert sums == [600, 510, 330]


def test_part_2_sample_input():
    depth_list = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]
    sums = solve.sliding_windows(depth_list, window=3)
    print(sums)
    increases = solve.count_increases(sums)

    assert 5 == increases
