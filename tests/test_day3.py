import pytest

from days import day3

TEST_FILE = "tests/data/day3_test.txt"
TEST_FILE_SIZE = (4, 2)


@pytest.mark.parametrize(
    "line, expected",
    [
        ["###", [True, True, True]],
        ["...", [False, False, False]],
        [".#.", [False, True, False]],
    ]
)
def test_parse_line(line, expected):
    assert day3.Grid.parse_line(line) == expected


def test_load_file():
    grid = day3.Grid()
    grid.load_file(TEST_FILE)
    assert grid.size() == TEST_FILE_SIZE


def test_move():
    grid = day3.Grid()
    grid.load_file(TEST_FILE)
    assert grid.size() == TEST_FILE_SIZE
    assert grid.pos() == (0, 0)
    grid.move(2, 1)
    assert grid.pos() == (2, 1)
    # Wrap around x-axis
    grid.move(TEST_FILE_SIZE[0] - 2, 0) == (0, 1)
    # Fall off end of y-axis
    with pytest.raises(IndexError):
        grid.move(0, TEST_FILE_SIZE[1] - 1)
