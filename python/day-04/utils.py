from bingo import BingoCard


def get_draws_from_input(line):
    return [int(draw) for draw in line.split(",")]


def get_cards_from_input(input_lines):
    card_lines = []
    cards = []
    for line in input_lines:
        if not line.strip():
            if card_lines:
                cards.append(BingoCard(card_lines))
                card_lines = []
            continue
        card_lines.append(line)
    if card_lines:
        cards.append(BingoCard(card_lines))
    return cards
