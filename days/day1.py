#!/usr/bin/env python

from functools import reduce
from itertools import combinations
import operator
import pathlib
from typing import List, Optional

DATA_FILE = 'data/day1.txt'
TARGET = 2020


def load_file(fn: str = DATA_FILE) -> List[int]:
    with pathlib.Path(fn).open() as in_file:
        return [int(line.strip()) for line in in_file]


def solve(nums: List[int], combo_len: int, target: int = TARGET) -> Optional[int]:
    matches = [combo for combo in combinations(
        nums, combo_len) if sum(combo) == target]
    if len(matches) == 1:
        return reduce(operator.mul, matches[0], 1)
    else:
        raise ValueError(
            f"Found {len(matches)} matches of length {combo_len} summing to {target}")


if __name__ == "__main__":
    print(solve(load_file(), 2))
    print(solve(load_file(), 3))
