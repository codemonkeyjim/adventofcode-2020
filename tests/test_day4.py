import pytest

from days import day4

TEST_FILE = "tests/data/day4_test.txt"


@pytest.mark.parametrize(
    "line,fields",
    [
        ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", [
            'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']],
        ["""iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929""", ['iyr', 'ecl', 'cid', 'eyr', 'pid', 'hcl', 'byr']]
    ]
)
def test_passport_init(line, fields):
    passport = day4.Passport(line)
    assert set(passport.entries.keys()) == set(fields)
