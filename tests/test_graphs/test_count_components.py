import pytest
from graphs.count_components import Solution


@pytest.mark.parametrize('n, edges, expect', [
    (
        5,
        [[0,1],[1,2],[3,4]],
        2
    ),
    (
        5,
        [[0,1],[1,2],[2,3],[3,4]],
        1
    )
])
def test_count_components(n, edges, expect):
    assert expect == Solution().count_components(n, edges)