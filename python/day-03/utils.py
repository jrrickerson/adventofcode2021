from collections import Counter


def binary_digits_to_places(binary_string):
    """Given a string representing a binary value, return a list of the
    decimal values of the places for which the bit is on.
    0011 -> [1, 2]"""
    reversed_bits = reversed(binary_string)
    place_values = [
        2**exp for exp, digit in enumerate(reversed_bits) if digit == "1"]
    return place_values


def bit_list(binary_string):
    return [int(bit) for bit in binary_string]


def count_bits_by_place(places_list):
    """Given a list of places values, get a frequency count of each"""
    bit_counter = Counter(places_list)

    return bit_counter


def bitwise_not(int_val, bitsize=None):
    """Perform a bitwise not on an integer value, inverting each bit.
    The builtin ~ operator can perform this but works on signed integers.
    The optional "bitsize" parameter allows the complement to be forced
    to a specific number of bits, or defaults to the minimum needed to
    represent "int_val"
    7  -> 111
    ~7 -> 000

    11  -> 1011
    ~11 -> 0100
    """
    bitsize = bitsize or int.bit_length(int_val) or 1
    # All 1s up to the allocated bitsize
    mask = (1 << bitsize) - 1

    # XOR to mask down to the correct bit size
    return int_val ^ mask


def most_common(values):
    counts = Counter(values)
    return counts.most_common(1)[0][0]


def most_common_bits(bit_lists):
    """In binary, there are only two possibilities (1 and 0), so if the count
    for a place exceeds half of the total list of entries, 1 is more common
    than 0"""
    bit_length = len(bit_lists[0])
    most_common_values = []
    for bit_idx in range(bit_length):
        bit_values = [bit_list[bit_idx] for bit_list in bit_lists]
        most_common_values.append(most_common(bit_values))

    return most_common_values


def filter_by_places(places_lists, bit_places, filter_places):
    """ This is a bit ugly, but:
    - For each bit place in bit_places
        - Filter OUT any list in places_lists if that place does NOT appear in
          filter_places but does appear in the current list
        - Filter IN any list in places_lists if that place DOES appear in
          filter_places and it appears in the current list
    NOTE:  This is basically a bad form of bit masking based on my weird
    solution to part 1
    """
    # Most significant bit first
    bit_places = sorted(bit_places, reverse=True)
    filter_places = sorted(filter_places, reverse=True)

    results = places_lists.copy()
    for place in bit_places:
        if place in filter_places:
            results = [
                place_list for place_list in results if place in place_list]
        else:
            results = [
                place_list for place_list in results
                if place not in place_list]
        if len(results) == 1:
            break
    return results[0]
