#!/usr/bin/env python

from collections import Counter
import pathlib
import re
from typing import List, TypedDict

DATA_FILE = 'data/day2.txt'


class PasswordPolicy(TypedDict):
    lower: int
    upper: int
    letter: str
    password: str


def parse_line(line: str) -> PasswordPolicy:
    pattern = re.compile(
        r'(?P<lower>\d+)-(?P<upper>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)')
    matches = pattern.match(line)
    policy: PasswordPolicy = {
        "lower": int(matches.group("lower")),
        "upper": int(matches.group("upper")),
        "letter": matches.group("letter"),
        "password": matches.group("password")
    }
    return policy


def is_password_count_compliant(policy: PasswordPolicy) -> bool:
    counts = Counter(policy["password"])
    return policy["lower"] <= counts.get(policy["letter"], 0) <= policy["upper"]


def is_letter_at_position(letter: str, position: int, target: str) -> bool:
    return position < len(target) and target[position] == letter


def is_password_position_compliant(policy: PasswordPolicy) -> bool:
    matches = [policy[position] for position in ("lower", "upper") if is_letter_at_position(
        policy["letter"], policy[position] - 1, policy["password"])]
    return len(matches) == 1


def load_file(fn: str = DATA_FILE) -> List[PasswordPolicy]:
    with pathlib.Path(fn).open() as in_file:
        return [parse_line(line.strip()) for line in in_file]


if __name__ == "__main__":
    password_list = load_file()
    good_count_passwords = filter(is_password_count_compliant, password_list)
    print(len(list(good_count_passwords)))
    good_pos_passwords = filter(is_password_position_compliant, password_list)
    print(len(list(good_pos_passwords)))
