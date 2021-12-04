from collections import Counter


def binary_digits_to_places(binary_string):
    """Given a string representing a binary value, return a list of the
    decimal values of the places for which the bit is on.
    0011 -> [1, 2]"""
    reversed_bits = reversed(binary_string)
    place_values = [
        2**exp for exp, digit in enumerate(reversed_bits) if digit == "1"]
    return place_values


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
