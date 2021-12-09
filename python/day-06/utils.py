LANTERNFISH_RESET = 6
LANTERNFISH_NEW = 8


def parse_lanternfish(line):
    return [int(f) for f in line.strip().split(",") if f]


def next_generation(lanternfish):
    next_gen = [f - 1 if f else LANTERNFISH_RESET for f in lanternfish]
    # New fish for every fish that was just reset
    new_fish = [LANTERNFISH_NEW] * lanternfish.count(0)
    next_gen += new_fish
    return next_gen


def find_generation(start_generation, forward=1):
    gen = start_generation
    for i in range(forward):
        gen = next_generation(gen)
    return gen
