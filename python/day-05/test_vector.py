from vector import Vector2


def test_init_defaults():
    v = Vector2()

    assert v.x == 0
    assert v.y == 0


def test_init_args():
    x = 7
    y = 54

    v = Vector2(x, y)

    assert v.x == x
    assert v.y == y


def test_addition():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 3, 4

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)

    v3 = v1 + v2

    assert v3.x == v1_x + v2_x
    assert v3.y == v1_y + v2_y
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y
    assert v2.x == v2_x
    assert v2.y == v2_y


def test_subtraction():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 3, 4

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)

    v3 = v1 - v2

    assert v3.x == v1_x - v2_x
    assert v3.y == v1_y - v2_y
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y
    assert v2.x == v2_x
    assert v2.y == v2_y


def test_scale_positive():
    v1_x, v1_y = 1, 2
    scalar = 13

    v1 = Vector2(v1_x, v1_y)
    v3 = v1.scale(scalar)

    assert v3.x == v1_x * scalar
    assert v3.y == v1_y * scalar
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y


def test_scale_negative():
    v1_x, v1_y = 1, 2
    scalar = -7

    v1 = Vector2(v1_x, v1_y)
    v3 = v1.scale(scalar)

    assert v3.x == v1_x * scalar
    assert v3.y == v1_y * scalar
    # Ensure original vectors didn't change
    assert v1.x == v1_x
    assert v1.y == v1_y


def test_cross():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 3, 4

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)

    result = v1.cross(v2)

    assert result == v1.x * v2.y - v1.y * v2.x


def test_cross_to_same_line():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 2, 2
    # Same line as the previous two points
    v3_x, v3_y = 8, 2

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)
    v3 = Vector2(v3_x, v3_y)

    result = v1.cross_to(v2, v3)

    assert result == 0


def test_cross_to_different_line():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 2, 2
    # Different line as the previous two points
    v3_x, v3_y = 1, 1

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)
    v3 = Vector2(v3_x, v3_y)

    result = v1.cross_to(v2, v3)

    assert result != 0


def test_equals_same_coordinates():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 1, 2

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)

    result = v1 == v2

    assert result is True


def test_equals_different_coordinates():
    v1_x, v1_y = 1, 2
    v2_x, v2_y = 3, 4

    v1 = Vector2(v1_x, v1_y)
    v2 = Vector2(v2_x, v2_y)

    result = v1 == v2

    assert result is False
