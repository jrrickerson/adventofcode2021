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
