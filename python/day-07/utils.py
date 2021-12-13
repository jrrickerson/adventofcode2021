import statistics


def parse_horizontal_positions(line):
    return [int(p) for p in line.strip().split(",") if p]


def sum_distance_to(positions, x):
    distances = [abs(pos - x) for pos in positions]
    return sum(distances)


def nth_triangular(x):
    """10 -> 1 + 2 + 3....8 + 9 + 10"""
    return sum(range(int(x) + 1))


def nth_triangular_distances(positions, x):
    distances = [nth_triangular(abs(pos - x)) for pos in positions]
    return distances


def distance_to_median(positions):
    median = statistics.median(positions)

    return sum_distance_to(positions, median)


def distance_to_mean(positions):
    mean = statistics.mean(positions)
    int_mean = round(mean)

    return sum_distance_to(positions, int_mean)


def weighted_mean(numbers, weights):
    return sum([w * n for w, n in zip(weights, numbers)]) / sum(weights)
