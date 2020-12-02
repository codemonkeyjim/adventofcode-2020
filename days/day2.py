#!/usr/bin/env python

import pathlib
import re
from re import match
from typing import Dict, List, Optional, TypedDict

DATA_FILE = 'data/day2.txt'


class PasswordPolicy(TypedDict):
    pattern: re.Pattern
    password: str


def parse_line(line: str) -> PasswordPolicy:
    pattern = re.compile(
        r'(?P<low>\d+)-(?P<high>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)')
    matches = pattern.match(line)
    policy: PasswordPolicy = {
        "pattern": re.compile("{letter}{{{low},{high}}}".format(**matches.groupdict())),
        "password": matches.group("password")
    }
    return policy


def is_password_compliant(policy: PasswordPolicy) -> bool:
    return bool(policy["pattern"].search(policy["password"]))


def load_file(fn: str = DATA_FILE) -> List[PasswordPolicy]:
    with pathlib.Path(fn).open() as in_file:
        return [parse_line(line.strip()) for line in in_file]


if __name__ == "__main__":
    good_passwords = filter(is_password_compliant, load_file())
    print(len(list(good_passwords)))
