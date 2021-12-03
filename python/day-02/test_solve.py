import solve


def test_command_to_vector2_down():
    command = "down 1"

    v = solve.command_to_vector2(command)

    assert isinstance(v, solve.Vector2)
    assert v.x == 0
    assert v.y == 1


def test_command_to_vector2_up():
    command = "up 1"

    v = solve.command_to_vector2(command)

    assert isinstance(v, solve.Vector2)
    assert v.x == 0
    assert v.y == -1


def test_command_to_vector2_forward():
    command = "forward 1"

    v = solve.command_to_vector2(command)

    assert isinstance(v, solve.Vector2)
    assert v.x == 1
    assert v.y == 0


def test_command_to_vector2_reverse():
    command = "reverse 1"

    v = solve.command_to_vector2(command)

    assert isinstance(v, solve.Vector2)
    assert v.x == -1
    assert v.y == 0


def test_command_to_vector2_scales_with_parameter():
    command = "down 5"

    v = solve.command_to_vector2(command)

    assert isinstance(v, solve.Vector2)
    assert v.x == 0
    assert v.y == 5


def test_Vector2_init_defaults():
    v = solve.Vector2()

    assert v.x == 0
    assert v.y == 0


def test_Vector2_init_args():
    x = 7
    y = 54

    v = solve.Vector2(x, y)

    assert v.x == x
    assert v.y == y


def test_Vector2_addition():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 3, 4

    v1 = solve.Vector2(v1_x, v1_y)
    v2 = solve.Vector2(v2_x, v2_y)

    v3 = v1 + v2

    assert v3.x == v1_x + v2_x
    assert v3.y == v1_y + v2_y
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y
    assert v2.x == v2_x
    assert v2.y == v2_y


def test_Vector2_subtraction():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 3, 4

    v1 = solve.Vector2(v1_x, v1_y)
    v2 = solve.Vector2(v2_x, v2_y)

    v3 = v1 - v2

    assert v3.x == v1_x - v2_x
    assert v3.y == v1_y - v2_y
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y
    assert v2.x == v2_x
    assert v2.y == v2_y


def test_Vector2_scale_positive():
    v1_x, v1_y = 1, 2
    scalar = 13

    v1 = solve.Vector2(v1_x, v1_y)
    v3 = v1.scale(scalar)

    assert v3.x == v1_x * scalar
    assert v3.y == v1_y * scalar
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y


def test_Vector2_scale_negative():
    v1_x, v1_y = 1, 2
    scalar = -7

    v1 = solve.Vector2(v1_x, v1_y)
    v3 = v1.scale(scalar)

    assert v3.x == v1_x * scalar
    assert v3.y == v1_y * scalar
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y


def test_part1_sample_input():
    sample_commands = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    result = solve.part_1(sample_commands)

    assert result == 150


def test_Vector2_magnitude_y_axis():
    expected = 5
    vec = solve.Vector2(0, 5)

    assert vec.magnitude == expected


def test_Vector2_magnitude_x_axis():
    expected = 7
    vec = solve.Vector2(7, 0)

    assert vec.magnitude == expected


def test_Vector2_magnitude_zero():
    expected = 0
    vec = solve.Vector2(0, 0)

    assert vec.magnitude == expected


def test_command_to_pos_aim_vectors_down():
    """Down command:  No change in position, positive change in aim"""
    command = "down 1"

    vec_pos, vec_aim = solve.command_to_pos_aim_vectors(command)

    assert isinstance(vec_pos, solve.Vector2)
    assert isinstance(vec_aim, solve.Vector2)
    assert vec_pos.x == 0
    assert vec_pos.y == 0
    assert vec_aim.x == 0
    assert vec_aim.y == 1


def test_command_to_pos_aim_vectors_up():
    """Up command:  No change in position, negative change in aim"""
    command = "up 1"

    vec_pos, vec_aim = solve.command_to_pos_aim_vectors(command)

    assert isinstance(vec_pos, solve.Vector2)
    assert isinstance(vec_aim, solve.Vector2)
    assert vec_pos.x == 0
    assert vec_pos.y == 0
    assert vec_aim.x == 0
    assert vec_aim.y == -1


def test_command_to_pos_aim_vectors_forward():
    """Forward command:  Positive change in position, no change in aim"""
    command = "forward 1"

    vec_pos, vec_aim = solve.command_to_pos_aim_vectors(command)

    assert isinstance(vec_pos, solve.Vector2)
    assert isinstance(vec_aim, solve.Vector2)
    assert vec_pos.x == 1
    assert vec_pos.y == 0
    assert vec_aim.x == 0
    assert vec_aim.y == 0


def test_command_to_pos_aim_vectors_reverse():
    """Forward command:  Negative change in position, no change in aim"""
    command = "reverse 1"

    vec_pos, vec_aim = solve.command_to_pos_aim_vectors(command)

    assert isinstance(vec_pos, solve.Vector2)
    assert isinstance(vec_aim, solve.Vector2)
    assert vec_pos.x == -1
    assert vec_pos.y == 0
    assert vec_aim.x == 0
    assert vec_aim.y == 0


def test_part2_sample_input():
    sample_commands = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    result = solve.part_2(sample_commands)
    assert result == 900

