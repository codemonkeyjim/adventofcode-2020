#!/usr/bin/env python

import pathlib
import re

DATA_FILE = 'data/day4.txt'


class Passport:
    REQUIRED_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    VALID_FIELDS = ('cid',) + REQUIRED_FIELDS

    def __init__(self, text: str) -> None:
        kv_pairs = re.split(r'\s+', text)
        self.entries = {}
        for pair in kv_pairs:
            k, v = pair.split(':', maxsplit=1)
            if k in self.VALID_FIELDS:
                self.entries[k] = v
