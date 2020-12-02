import pytest
import re

from days import day2


@pytest.mark.parametrize(
    "line, lower, upper, letter, password",
    [
        ["1-4 m: mrfmmbjxr", 1, 4, "m", "mrfmmbjxr"],
        ["5-16 b: bbbbhbbbbpbxbbbcb", 5, 16, "b", "bbbbhbbbbpbxbbbcb"],
        ["13-16 q: qqqqqvzwqqqqqqqq", 13, 16, "q", "qqqqqvzwqqqqqqqq"]
    ]
)
def test_parse_line(line, lower, upper, letter, password):
    result = day2.parse_line(line)
    assert result == {"lower": lower, "upper": upper,
                      "letter": letter, "password": password}


@pytest.mark.parametrize(
    "lower, upper, letter, password, expected",
    [
        [1, 3, "a", "abcde", True],
        [1, 3, "b", "cdefg", False],
        [2, 9, "c", "ccccccccc", True],
        [1, 5, "p", "pppppp", False]
    ]
)
def test_is_password_count_compliant(lower: int, upper: int, letter: str, password: str, expected: bool):
    policy: day2.PasswordPolicy = {
        "lower": lower, "upper": upper, "letter": letter, "password": password}
    result = day2.is_password_count_compliant(policy)
    assert result == expected


@pytest.mark.parametrize(
    "position, letter, target, expected",
    [
        [0, "a", "abcde", True],
        [0, "b", "cdefg", False],
        [2, "c", "ccccccccc", True],
        [3, "p", "pp", False]
    ]
)
def test_is_letter_at_position(position: int, letter: str, target: str, expected: bool):
    assert day2.is_letter_at_position(letter, position, target) == expected


@pytest.mark.parametrize(
    "lower, upper, letter, password, expected",
    [
        [1, 3, "a", "abcde", True],
        [1, 3, "b", "cdefg", False],
        [2, 9, "c", "ccccccccc", False],
        [1, 3, "a", "bb", False]
    ]
)
def test_is_password_position_compliant(lower: int, upper: int, letter: str, password: str, expected: bool):
    policy: day2.PasswordPolicy = {
        "lower": lower, "upper": upper, "letter": letter, "password": password}
    result = day2.is_password_position_compliant(policy)
    assert result == expected
