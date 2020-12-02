import pytest
import re

from days import day2


@pytest.mark.parametrize(
    "line, pattern, password",
    [
        ["1-4 m: mrfmmbjxr", "m{1,4}", "mrfmmbjxr"],
        ["5-16 b: bbbbhbbbbpbxbbbcb", "b{5,16}", "bbbbhbbbbpbxbbbcb"],
        ["13-16 q: qqqqqvzwqqqqqqqq", "q{13,16}", "qqqqqvzwqqqqqqqq"]
    ]
)
def test_parse_line(line, pattern, password):
    result = day2.parse_line(line)
    assert result == {"pattern": re.compile(pattern), "password": password}


@pytest.mark.parametrize(
    "pattern, password, expected",
    [
        ["a{1,3}", "abcde", True],
        ["b{1,3}", "cdefg", False],
        ["c{2,9}", "ccccccccc", True]
    ]
)
def test_is_password_compliant(pattern: str, password: str, expected: bool):
    policy: day2.PasswordPolicy = {
        "pattern": re.compile(pattern), "password": password}
    result = day2.is_password_compliant(policy)
    assert result == expected
