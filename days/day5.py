#!/usr/bin/env python

import pathlib
from typing import Tuple

DATA_FILE = 'data/day5.txt'

NUM_ROWS = 128
NUM_COLS = 8


def seat_id(line: str) -> int:
    # Binary partitioning == binary encoding!
    bits = line.replace("B", "1").replace(
        "F", "0").replace("R", "1").replace("L", "0")
    return int(bits, 2)


def load_file(fn: str = DATA_FILE) -> set[int]:
    with pathlib.Path(fn).open() as in_file:
        return {seat_id(line) for line in in_file}


if __name__ == "__main__":
    all_seats = set(range((NUM_ROWS + 1) * NUM_COLS - 1))
    occupied_seats = load_file()
    print(f"Part 1: {max(occupied_seats)}")
    open_seats = all_seats - occupied_seats
    candidate_seats = [open_seat for open_seat in open_seats if open_seat -
                       1 in occupied_seats and open_seat+1 in occupied_seats]
    print(f"Part 2: {candidate_seats}")
