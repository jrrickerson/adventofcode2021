import solve
import utils


def test_get_draws_from_input():
    input_line = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1"

    draws = utils.get_draws_from_input(input_line)

    assert draws == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]


def test_get_cards_from_input_single_card():
    input_lines = [
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",
        " 1 12 20 15 19",
    ]

    cards = utils.get_cards_from_input(input_lines)

    assert len(cards) == 1
    for card in cards:
        assert len(card.board) == len(input_lines)


def test_get_cards_from_input_multiple_cards_with_empty_lines():
    input_lines = [
        "",
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",
        " 1 12 20 15 19",
        "",
        " 3 15  0  2 22",
        " 9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
        "",
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7",
    ]
    cards = utils.get_cards_from_input(input_lines)

    assert len(cards) == 3
    for card in cards:
        assert len(card.board) == 5


def test_part1_sample_input():
    bingo_data = """
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
         8  2 23  4 24
        21  9 14 16  7
         6 10  3 18  5
         1 12 20 15 19

         3 15  0  2 22
         9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
         2  0 12  3  7"""
    bingo_input_lines = bingo_data.strip().splitlines()

    result = solve.part_1(bingo_input_lines)

    assert result == 4512
