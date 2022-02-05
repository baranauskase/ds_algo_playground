import pytest
from graphs.valid_tree import Solution

@pytest.mark.parametrize('n, edges, expect', [
    (
        5,
        [[0,1],[0,2],[0,3],[1,4]],
        True
    ),
    (
        5,
        [[0,1],[1,2],[2,3],[1,3],[1,4]],
        False
    ),
    (
        4,
        [[0,1],[2,3]],
        False
    )
])
def test_valid_tree(n, edges, expect):
    assert expect == Solution().valid_tree(n, edges)