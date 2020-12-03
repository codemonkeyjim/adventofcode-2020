#!/usr/bin/env python

from functools import reduce
import operator
import pathlib
from typing import Tuple

DATA_FILE = 'data/day3.txt'

ALL_SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

Row = list[bool]
Coords = Tuple[int, int]


class Grid:
    def __init__(self) -> None:
        self.rows: list[Row] = list(list())
        self.x = 0
        self.y = 0

    def load_file(self, fn: str = DATA_FILE) -> None:
        with pathlib.Path(fn).open() as in_file:
            self.rows = [self.parse_line(line) for line in in_file]

    def size(self) -> Coords:
        return (len(self.rows[0]), len(self.rows))

    @staticmethod
    def parse_line(line: str) -> Row:
        return [char == "#" for char in line.strip()]

    def move(self, delta: Coords) -> None:
        if self.y + delta[1] >= self.size()[1]:
            raise IndexError("Exceeded end of grid")
        self.x = (self.x + delta[0]) % self.size()[0]
        self.y = self.y + delta[1]

    def pos(self) -> Coords:
        return (self.x, self.y)

    def is_tree(self) -> bool:
        return self.rows[self.y][self.x]

    def check_slope(self, delta: Coords) -> int:
        trees = 0
        while True:
            trees = trees + self.is_tree()
            try:
                self.move(delta)
            except IndexError:
                self.x = 0
                self.y = 0
                break
        return trees

    def check_slopes(self, slopes: list[Coords]) -> int:
        trees = [self.check_slope(slope) for slope in slopes]
        return reduce(operator.mul, trees, 1)


if __name__ == "__main__":
    grid = Grid()
    grid.load_file(DATA_FILE)
    print(f"Part 1: {grid.check_slope((3,1))}")
    print(f"Part 2: {grid.check_slopes(ALL_SLOPES)}")
