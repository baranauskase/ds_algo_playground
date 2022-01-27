from unittest import expectedFailure
import pytest
from graphs.number_of_provinces import Solution

@pytest.mark.parametrize('case, expect', [
    ([[1,1,0],[1,1,0],[0,0,1]], 2),
    ([[1,0,0],[0,1,0],[0,0,1]], 3),
    ([[1,1,0,0],[1,1,0,1],[0,0,1,0],[0,1,0,1]], 2)
])
def test_find_circle_num(case, expect):
    sol = Solution()
    assert sol.finde_circle_num(case) == expect