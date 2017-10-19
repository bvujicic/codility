"""
Test 1: BinaryGap
"""


def binary_gap(N):
    binary_string = format(N, 'b')
    zero_gaps = binary_string.strip('0').split('1')

    length_of_max_gap = len(max(zero_gaps))

    return length_of_max_gap if length_of_max_gap else 0