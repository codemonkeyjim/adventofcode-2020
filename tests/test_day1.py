import pytest

from days.day1 import solve


@pytest.mark.parametrize(
    "nums, num_vals, solution",
    [
        [[1721, 979, 366, 299, 675, 1456], 2, 514579],
        [[1721, 979, 366, 299, 675, 1456], 3, 241861950]
    ]
)
def test_solve(nums, num_vals, solution):
    assert solve(nums, num_vals) == solution
