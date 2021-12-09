import statistics


def parse_horizontal_positions(line):
    return [int(p) for p in line.strip().split(",") if p]


def sum_distance_to(positions, x):
    distances = [abs(pos - x) for pos in positions]
    return sum(distances)


def distance_to_median(positions):
    median = statistics.median(positions)

    return sum_distance_to(positions, median)


def distance_to_mean(positions):
    mean = statistics.mean(positions)
    int_mean = round(mean)

    return sum_distance_to(positions, int_mean)
