#!/usr/bin/env python

import pathlib
import re
from typing import Any, Callable

DATA_FILE = 'data/day4.txt'


class Passport:
    REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    VALID_FIELDS = {'cid'}.union(REQUIRED_FIELDS)
    VALIDATORS: dict[str, Callable[[Any], bool]] = {
        'byr': lambda val: 1920 <= int(val) <= 2002,
        'iyr': lambda val: 2010 <= int(val) <= 2020,
        'eyr': lambda val: 2020 <= int(val) <= 2030,
        'hgt': lambda val: (val.endswith("cm") and (150 <= int(val[:-2]) <= 193)) or (val.endswith("in") and (59 <= int(val[:-2]) <= 76)),
        'hcl': lambda val: re.match(r'#[0-9a-f]{6}', val) is not None,
        'ecl': lambda val: val in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda val: re.match(r'\d{9}', val) is not None
    }

    def __init__(self, text: str) -> None:
        kv_pairs = re.split(r'\s+', text)
        self.entries = {}
        for pair in kv_pairs:
            k, v = pair.split(':', maxsplit=1)
            if k in self.VALID_FIELDS:
                self.entries[k] = v

    def has_required_fields(self) -> bool:
        return set(self.entries.keys()).issuperset(self.REQUIRED_FIELDS)

    def is_field_valid(self, field) -> bool:
        validator = self.VALIDATORS.get(field, lambda _: True)
        return validator(self.entries[field])


def load_file(fn: str = DATA_FILE) -> list[str]:
    with pathlib.Path(fn).open() as in_file:
        whole_file = in_file.read()
    return re.split(r'\n\n', whole_file)


if __name__ == "__main__":
    passports = [Passport(record) for record in load_file()]
    print(len([passport for passport in passports if passport.has_required_fields()]))
