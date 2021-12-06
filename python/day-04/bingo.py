from collections import defaultdict


class BingoCard:
    def __init__(self, text_lines=None):
        self.marked = []
        self.board = []
        self.index = {}
        self.bingo = None
        if text_lines:
            self.load_board(text_lines)

    def parse_lines(self, text_lines):
        rows = []
        for line in text_lines:
            row = [int(item) for item in line.strip().split()]
            rows.append(row)
        return rows

    def load_board(self, text_lines):
        self.board = self.parse_lines(text_lines)
        # Index by value for quick lookup
        self.index = {
            number: (rownum, colnum)
            for rownum, row in enumerate(self.board)
            for colnum, number in enumerate(row)
        }

    def apply_draw(self, number):
        if number in self.index:
            self.marked.append(number)
        self.has_bingo()

    def _has_bingo_for_sequence(self, numbers):
        if all([number in self.marked for number in numbers]):
            return True
        return False

    def has_bingo(self):
        if self.bingo:
            return True
        if len(self.marked) < min(len(self.board), len(self.board[0])):
            return False

        # Check rows
        for row in self.board:
            if self._has_bingo_for_sequence(row):
                self.bingo = row.copy()
                return True
        # Check columns
        for i in range(len(self.board[0])):
            col = [row[i] for row in self.board]
            if self._has_bingo_for_sequence(col):
                self.bingo = col.copy()
                return True
        return False

    def score_bingo(self):
        if not self.has_bingo():
            return 0

        unmarked = [
            number for number in self.index.keys()
            if number not in self.marked]
        score = sum(unmarked) * self.marked[-1]
        return score
