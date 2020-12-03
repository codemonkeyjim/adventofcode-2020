#!/usr/bin/env python

from ast import Index
import pathlib
from typing import Tuple

DATA_FILE = 'data/day3.txt'

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

    def move(self, delta_x, delta_y) -> None:
        if self.y + delta_y >= self.size()[1]:
            raise IndexError("Exceeded end of grid")
        self.x = (self.x + delta_x) % self.size()[0]
        self.y = self.y + delta_y

    def pos(self) -> Coords:
        return (self.x, self.y)

    def is_tree(self) -> bool:
        return self.rows[self.y][self.x]


if __name__ == "__main__":
    grid = Grid()
    grid.load_file(DATA_FILE)
    trees = 0
    while True:
        trees = trees + grid.is_tree()
        try:
            grid.move(3, 1)
        except IndexError:
            break
    print(trees)
