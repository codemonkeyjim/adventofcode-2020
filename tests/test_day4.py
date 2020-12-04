import pytest

from days import day4


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
def test_passport_has_required_fields(line, valid):
    passport = day4.Passport(line)
    assert passport.has_required_fields() == valid


@pytest.mark.parametrize(
    "field,value,valid",
    [
        ["byr", "1920", True],
        ["byr", "1919", False],
        ["byr", "2002", True],
        ["byr", "2003", False],
        ["iyr", "2010", True],
        ["iyr", "2009", False],
        ["iyr", "2020", True],
        ["iyr", "2021", False],
        ["eyr", "2020", True],
        ["eyr", "2019", False],
        ["eyr", "2030", True],
        ["eyr", "2031", False],
        ["hgt", "150cm", True],
        ["hgt", "149cm", False],
        ["hgt", "193cm", True],
        ["hgt", "194cm", False],
        ["hgt", "59in", True],
        ["hgt", "58in", False],
        ["hgt", "76in", True],
        ["hgt", "77in", False],
        ["hcl", "#123abc", True],
        ["hcl", "#123abcd", False],
        ["hcl", "#123abz", False],
        ["hcl", "123abc", False],
        ["ecl", "brn", True],
        ["ecl", "wat", False],
        ["pid", "000000001", True],
        ["pid", "0123456789", False],
    ]
)
def test_passsport_field_validators(field, value, valid):
    passport = day4.Passport(f"{field}:{value}")
    assert passport.is_field_valid(field) == valid


@pytest.mark.parametrize(
    "line,valid",
    [
        ["eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926", False],
        ["iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946", False],
        ["hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277", False],
        ["hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007", False],
        ["pid:087499704 hgt:74 in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f", True],
        ["eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm", True],
        ["hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022", True],
        ["iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719", True]
    ]
)
def test_passport_is_valid(line, valid):
    assert day4.Passport(line).is_valid() == valid
