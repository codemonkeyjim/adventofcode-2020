import pytest

from days import day5


@pytest.mark.parametrize(
    "line, seat_id",
    [
        ["BFFFBBFRRR", 567],
        ["FFFBBBFRRR", 119],
        ["BBFFBBFRLL", 820]
    ]
)
def test_seat_id(line, seat_id):
    assert day5.seat_id(line) == seat_id
