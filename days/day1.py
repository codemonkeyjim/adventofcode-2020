#!/usr/bin/env python

import pathlib
from typing import List, Optional

DATA_FILE = 'data/day1.txt'
TARGET = 2020


def load_file(fn: str = DATA_FILE) -> List[int]:
    with pathlib.Path(fn).open() as in_file:
        return [int(line.strip()) for line in in_file]


def solve(nums: List[int], target: int = TARGET) -> Optional[int]:
    low_nums = [num for num in nums if num < target]
    for i in range(0, len(low_nums)):
        for j in range(i+1, len(low_nums)):
            if low_nums[i] + low_nums[j] == target:
                return low_nums[i] * low_nums[j]
    return None


if __name__ == "__main__":
    print(solve(load_file()))
