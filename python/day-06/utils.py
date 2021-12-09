from collections import Counter

LANTERNFISH_RESET = 6
LANTERNFISH_NEW = 8


def parse_lanternfish(line):
    return [int(f) for f in line.strip().split(",") if f]


def next_generation(lanternfish):
    """Given a list of fish timers, create the next generation of fish
    timers"""
    next_gen = [f - 1 if f else LANTERNFISH_RESET for f in lanternfish]
    # New fish for every fish that was just reset
    new_fish = [LANTERNFISH_NEW] * lanternfish.count(0)
    next_gen += new_fish
    return next_gen


def find_generation(start_generation, forward=1):
    """Generate consecutive generations of fish timers for 'forward'
    number of generations, and return the resulting generation"""
    gen = start_generation
    for i in range(forward):
        gen = next_generation(gen)
    return gen


def next_generation_counts(counts):
    """Assuming a dictionary of fish timer values to fish counts,
    calculate the counts for the next generation."""
    next_gen = Counter()
    for timer_value in sorted(counts.keys()):
        if timer_value:
            next_gen[timer_value - 1] += counts[timer_value]
        else:
            next_gen[LANTERNFISH_RESET] += counts[timer_value]
    next_gen[LANTERNFISH_NEW] += counts[0]

    return next_gen


def find_generation_counts(start_generation, forward=1):
    """Given a list of fish timers, create a counter for the initial
    generation and update it for each subsequent generation for "forward"
    number of generations, returning the counts from the final generation"""
    gen_counts = Counter(start_generation)
    for i in range(forward):
        gen_counts = next_generation_counts(gen_counts)
    return gen_counts
