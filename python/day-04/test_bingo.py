import pytest
from bingo import BingoCard


def test_parse_lines_empty():
    input_lines = []

    card = BingoCard()
    board = card.parse_lines(input_lines)

    assert not board


def test_parse_lines_contains_all_values():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]
    expected_values = [
        [20, 21, 22, 23, 24,],
        [15, 16, 17, 18, 19,],
        [45, 44, 43, 42, 41,],
    ]

    card = BingoCard()
    board = card.parse_lines(input_lines)

    assert board == expected_values


def test_parse_lines_error_on_nonnumeric():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 A B C"]

    card = BingoCard()
    with pytest.raises(ValueError):
        card.parse_lines(input_lines)


def test_parse_lines_ignores_whitespace():
    input_lines = [
        "20 21 22 23 24    ",
        "15   16 17   18 19",
        "    45 44    43 42 41\n\n"]
    expected_values = [
        [20, 21, 22, 23, 24,],
        [15, 16, 17, 18, 19,],
        [45, 44, 43, 42, 41,],
    ]

    card = BingoCard()
    board = card.parse_lines(input_lines)

    assert board == expected_values


def test_load_board_creates_index():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]
    expected_values = [
        [20, 21, 22, 23, 24,],
        [15, 16, 17, 18, 19,],
        [45, 44, 43, 42, 41,],
    ]

    card = BingoCard()
    card.load_board(input_lines)

    for rownum, row in enumerate(card.board):
        for colnum, number in enumerate(row):
            assert number in card.index
            assert card.index[number] == (rownum, colnum)


def test_init_load_board():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]
    expected_values = [
        [20, 21, 22, 23, 24,],
        [15, 16, 17, 18, 19,],
        [45, 44, 43, 42, 41,],
    ]

    card = BingoCard(input_lines)

    for rownum, row in enumerate(card.board):
        for colnum, number in enumerate(row):
            assert number in card.index
            assert card.index[number] == (rownum, colnum)


def test_apply_draw_adds_mark_on_card():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]

    card = BingoCard(input_lines)
    card.apply_draw(42)

    assert 42 in card.marked
    assert card.bingo is None


def test_apply_draw_no_mark_if_not_on_card():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]

    card = BingoCard(input_lines)
    card.apply_draw(77)

    assert 77 not in card.marked
    assert card.bingo is None


def test_has_no_bingo():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]
    draws = [15, 44, 17, 23, 100]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert not card.has_bingo()


def test_has_no_bingo_too_few_draws():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]
    draws = [15, 44]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert not card.has_bingo()


def test_has_bingo_for_row():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41"]
    draws = [15, 16, 17, 18, 19]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert card.has_bingo()
    assert card.bingo == draws


def test_has_bingo_for_col():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41",
    ]
    draws = [23, 18, 42]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert card.has_bingo()
    assert card.bingo == draws


def test_has_bingo_subset_of_marked():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41",
    ]
    draws = [20, 21, 23, 18, 17, 42]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert card.has_bingo()
    assert set(card.bingo).issubset(set(card.marked))


def test_has_bingo_first_bingo_only():
    input_lines = [
        "20 21 22 23 24",
        "15 16 17 18 19",
        "45 44 43 42 41",
    ]
    first_draws = [85, 47, 21, 16, 44]
    second_draws = [20, 22, 23, 24]

    card = BingoCard(input_lines)
    for draw in first_draws:
        card.apply_draw(draw)
    assert card.has_bingo()
    assert card.bingo == [21, 16, 44]

    for draw in second_draws:
        card.apply_draw(draw)
    assert card.has_bingo()
    assert card.bingo == [21, 16, 44]


def test_score_card_no_bingo():
    input_lines = [
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7",
    ]
    draws = [7,4,9,5]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert not card.has_bingo()
    assert card.score_bingo() == 0


def test_score_card_with_bingo():
    input_lines = [
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7",
    ]
    draws = [7,4,9,5,11,17,23,2,0,14,21,24]

    card = BingoCard(input_lines)
    for draw in draws:
        card.apply_draw(draw)

    assert card.has_bingo()
    assert card.score_bingo() == 4512
