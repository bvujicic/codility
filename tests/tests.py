from hypothesis import given
import hypothesis.strategies as st

from Lesson1.binary_gap import solution


@given(st.integers())
def test_binary_gap(N):

    print(solution(N))