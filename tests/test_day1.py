import pytest

from days.day1 import solve


@pytest.mark.parametrize(
    "nums, solution",
    [
        [[1721, 979, 366, 299, 675, 1456], 514579]
    ]
)
def test_solve(nums, solution):
    assert solve(nums) == solution
