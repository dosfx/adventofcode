import re
from typing import Generator, Generic, Iterable, TypeVar

from aoc_lib._point2 import Point2

T = TypeVar("T", int, str)


class BaseGrid(Generic[T]):
    def __init__(self, data: Iterable[Iterable[T]]) -> None:
        self._data: tuple[tuple[T, ...], ...] = tuple([
            tuple([cell for cell in row])
            for row in data
        ])
        self._width = len(self._data[0])
        self._height = len(self._data)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BaseGrid) and self._data == other._data

    def __str__(self) -> str:
        return "\n".join(["".join([str(cell) for cell in row]) for row in self._data])

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def at(self, x: int, y: int) -> T:
        return self._data[y][x]

    def atp(self, p: Point2) -> T:
        return self.at(p.x, p.y)

    def at_none(self, x: int, y: int) -> T | None:
        if not self.contains(x, y):
            return None
        return self.at(x, y)

    def contains(self, x: int, y: int) -> bool:
        return 0 <= x and x < self.width and 0 <= y and y < self.height

    def containsp(self, p: Point2) -> bool:
        return self.contains(p.x, p.y)

    def rows(self) -> Generator[tuple[int, tuple[T, ...]], None, None]:
        for y, row in enumerate(self._data):
            yield (y, row)

    def cells(self) -> Generator[tuple[int, int, T], None, None]:
        for y, row in self.rows():
            for x, cell in enumerate(row):
                yield (x, y, cell)


class StrGrid(BaseGrid[str]):
    def find(self, pattern: str) -> Generator[tuple[int, int, str], None, None]:
        re_pattern = re.compile(pattern)
        for x, y, cell in self.cells():
            if re.match(re_pattern, cell):
                yield (x, y, cell)

    @staticmethod
    def from_lines(lines: Iterable[str], sep: str | None = None) -> "StrGrid":
        if sep is None:
            return StrGrid(lines)
        return StrGrid([
            [cell for cell in line.split(sep)]
            for line in lines
        ])

    @staticmethod
    def from_file(path: str, sep: str | None = None) -> "StrGrid":
        with open(path) as file:
            return StrGrid.from_lines([line.strip() for line in file.readlines()], sep)


class IntGrid(BaseGrid[int]):
    def find(self, num: int) -> Generator[tuple[int, int, int], None, None]:
        for x, y, cell in self.cells():
            if cell == num:
                yield (x, y, cell)

    @staticmethod
    def from_str(grid: StrGrid) -> "IntGrid":
        return IntGrid([
            [int(num) for num in row]
            for _, row in grid.rows()
        ])

    @staticmethod
    def from_lines(lines: Iterable[str], sep: str | None = None) -> "IntGrid":
        grid = StrGrid.from_lines(lines, sep)
        return IntGrid.from_str(grid)

    @staticmethod
    def from_file(path: str, sep: str | None = None) -> "IntGrid":
        grid = StrGrid.from_file(path, sep)
        return IntGrid.from_str(grid)