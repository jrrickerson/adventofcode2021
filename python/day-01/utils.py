def sliding_windows(measurement_list, window=3):
    sums = []
    if len(measurement_list) < window:
        return sums
    for i in range(0, len(measurement_list)):
        window_list = measurement_list[i:i+window]
        if len(window_list) < window:
            break
        window_sum = sum(window_list)
        sums.append(window_sum)
    return sums


def load_depth_list(file_obj):
    return [int(line.strip()) for line in file_obj if line.strip()]


def count_increases(value_list):
    if not value_list:
        return 0

    previous = None
    count = 0
    for item in value_list:
        if previous is not None and previous < item:
            count += 1
        previous = item
    return count



