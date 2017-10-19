"""
Test 1: PermCheck
Test 2: FrogRiverOne
"""


def perm_check(A):

    if range(1, len(A) + 1) == sorted(A):
        return 1

    return 0


def frog_river_one(X, A):
    # the set we're building must equal at some point to this set, otherwise -1
    minimum_set = set(range(1, X + 1))

    current_set = set()
    for idx, element in enumerate(A):
        current_set.add(element)

        # at this step the frog can pass
        if current_set == minimum_set:
            return idx

    return -1


def missing_integer(A):
    A.sort()
    set_A = set(A)

    idx = 0
    for idx, element in enumerate(A, 1):
        if idx in set_A:
            continue
        else:
            return idx

    return idx + 1