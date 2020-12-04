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


@pytest.mark.parametrize(
    "line,valid",
    [
        ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", True],
        ["iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",  False],
        ["hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm", True]
    ]
)
def test_passport_is_valid(line, valid):
    passport = day4.Passport(line)
    assert passport.is_valid() == valid
