import re
from typing import Generator, Iterable

from aoc_lib._point2 import Point2


class Grid:
    def __init__(self, data: Iterable[Iterable[str]]) -> None:
        self._data = tuple([
            tuple([cell for cell in row])
            for row in data
        ])
        self._width = len(self._data[0])
        self._height = len(self._data)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Grid) and self._data == other._data

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self._data])

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def at(self, x: int, y: int) -> str:
        return self._data[y][x]

    def atp(self, p: Point2) -> str:
        return self.at(p.x, p.y)

    def contains(self, x: int, y: int) -> bool:
        return 0 <= x and x < self.width and 0 <= y and y < self.height

    def containsp(self, p: Point2) -> bool:
        return self.contains(p.x, p.y)

    def find(self, pattern: str) -> Generator[tuple[int, int, str], None, None]:
        re_pattern = re.compile(pattern)
        for x, y, cell in self.cells():
            if re.match(re_pattern, cell):
                yield (x, y, cell)


    def rows(self) -> Generator[tuple[int, tuple[str, ...]], None, None]:
        for y, row in enumerate(self._data):
            yield (y, row)

    def cells(self) -> Generator[tuple[int, int, str], None, None]:
        for y, row in self.rows():
            for x, cell in enumerate(row):
                yield (x, y, cell)

    @staticmethod
    def from_lines(lines: Iterable[str], sep: str | None = None) -> "Grid":
        if sep is None:
            return Grid(lines)
        return Grid([
            [cell for cell in line.split(sep)]
            for line in lines
        ])

    @staticmethod
    def from_file(path: str, sep: str | None = None) -> "Grid":
        with open(path) as file:
            return Grid.from_lines([line.strip() for line in file.readlines()], sep)
