import utils


def get_input_data(filename):
    return [line.strip() for line in open(filename)]


def part_1(input_data):
    draws = utils.get_draws_from_input(input_data[0])
    cards = utils.get_cards_from_input(input_data[1:])

    for draw in draws:
        for card in cards:
            card.apply_draw(draw)
            if card.has_bingo():
                return card.score_bingo()


def part_2(input_data):
    pass


def main(input_file):
    input_data = get_input_data(input_file)

    part_1_result = part_1(input_data)
    part_2_result = part_2(input_data)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":
    print(
        "Solving Puzzle for Day 4:",
        "https://adventofcode.com/2021/day/4")
    print(main("../puzzles/day-04.input"))
