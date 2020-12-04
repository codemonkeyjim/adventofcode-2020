#!/usr/bin/env python

import pathlib
import re

DATA_FILE = 'data/day4.txt'


class Passport:
    REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    VALID_FIELDS = {'cid'}.union(REQUIRED_FIELDS)

    def __init__(self, text: str) -> None:
        kv_pairs = re.split(r'\s+', text)
        self.entries = {}
        for pair in kv_pairs:
            k, v = pair.split(':', maxsplit=1)
            if k in self.VALID_FIELDS:
                self.entries[k] = v

    def is_valid(self) -> bool:
        return set(self.entries.keys()).issuperset(self.REQUIRED_FIELDS)


def load_file(fn: str = DATA_FILE) -> list[str]:
    with pathlib.Path(fn).open() as in_file:
        whole_file = in_file.read()
    return re.split(r'\n\n', whole_file)


if __name__ == "__main__":
    passports = [Passport(record) for record in load_file()]
    print(len([passport for passport in passports if passport.is_valid()]))
