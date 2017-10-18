"""
Test 1: OddOccurrencesInArray, 100%
Test 2: CyclicRotation, 100%
"""


def odd_occurences_in_array(A):
    result = 0
    for element in A:
        result ^= element

    return result


def cyclic_rotation(A, K):
    if not A:
        return A

    for idx in range(K):
        b = A.pop(len(A) - 1)
        A.insert(0, b)

    return A