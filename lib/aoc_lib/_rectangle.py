from dataclasses import dataclass
from typing import Generator

from aoc_lib._vector2 import Vector2


@dataclass(frozen=True)
class Rectangle:
    x: int
    y: int
    w: int
    h: int

    @property
    def area(self) -> int:
        return self.w * self.h

    @property
    def top(self) -> int:
        return self.y

    @property
    def bot(self) -> int:
        return self.y + self.h - 1

    @property
    def left(self) -> int:
        return self.x

    @property
    def right(self) -> int:
        return self.x + self.w - 1

    def contains(self, x: int, y: int) -> bool:
        return self.left <= x and x <= self.right and self.top <= y and y <= self.bot

    def containsp(self, p: Vector2) -> bool:
        return self.contains(p.x, p.y)

    @staticmethod
    def from_ints(x1: int, y1: int, x2: int, y2: int) -> "Rectangle":
        return Rectangle(min(x1, x2), min(y1, y2), abs(x1 - x2) + 1, abs(y1 - y2) + 1)

    @staticmethod
    def from_points(a: Vector2, b: Vector2) -> "Rectangle":
        return Rectangle.from_ints(a.x, a.y, b.x, b.y)
