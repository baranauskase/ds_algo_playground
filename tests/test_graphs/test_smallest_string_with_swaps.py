from curses.ascii import SO
import pytest
from graphs.smallest_string_with_swaps import Solution

@pytest.mark.parametrize('s, pairs, expect', [
    (
        'dcab',
        [[0,3],[1,2]],
        'bacd'
        # Explaination: 
        # Swap s[0] and s[3], s = "bcad"
        # Swap s[1] and s[2], s = "bacd"
    ),
    (
        'dcab',
        [[0,3],[1,2],[0,2]],
        'abcd'
        # Explaination: 
        # Swap s[0] and s[3], s = "bcad"
        # Swap s[0] and s[2], s = "acbd"
        # Swap s[1] and s[2], s = "abcd"
    ),
    (
        'cba',
        [[0,1],[1,2]],
        'abc'
        # Explaination: 
        # Swap s[0] and s[1], s = "bca"
        # Swap s[1] and s[2], s = "bac"
        # Swap s[0] and s[1], s = "abc"
    )
])
def test_smallest_string_with_swaps(s, pairs, expect):
    assert expect == Solution().smallest_string_with_swaps(s, pairs)
