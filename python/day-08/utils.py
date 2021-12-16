# Number of segments used for each seven-segment digit
# 0: 6,
# 1: 2,
# 2: 5,
# 3: 5,
# 4: 4,
# 5: 5,
# 6: 6,
# 7: 3,
# 8: 7,
# 9: 6,
# Which digits are possible with the number of segments "on"
SEGMENT_COUNT_DIGITS = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}


def parse_signal_data(line):
    if not line:
        return [], []

    signal_text, output_text = line.strip().split(" | ")
    signals = signal_text.split()
    outputs = output_text.split()

    return signals, outputs


def translate_by_count(output_value):
    candidate_digits = SEGMENT_COUNT_DIGITS.get(len(output_value), [])
    return candidate_digits
