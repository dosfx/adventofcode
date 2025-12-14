from dataclasses import dataclass
from math import sqrt
from typing import Generator

@dataclass(frozen=True)
class Vector2:
    x: int
    y: int

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self) -> "Vector2":
        return Vector2(-self.x, -self.y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scale: int) -> "Vector2":
        return Vector2(self.x * scale, self.y * scale)

    @property
    def vertical(self) -> bool:
        return self.x == 0 and self.y != 0

    @property
    def horizonal(self) -> bool:
        return self.x != 0 and self.y == 0

    @property
    def clock(self) -> "Vector2":
        return Vector2(-self.y, self.x)

    @property
    def counter(self) -> "Vector2":
        return Vector2(self.y, -self.x)

    def directions(self) -> Generator["Vector2", None, None]:
        for d in DIRECTIONS:
            yield self + d

    def dist(self, other: "Vector2") -> float:
        return sqrt(self.dist2(other))

    def dist2(self, other: "Vector2") -> int:
        return self.__sub__(other).len2()

    def len(self) -> float:
        return sqrt(self.len2())

    def len2(self) -> int:
        return (self.x * self.x) + (self.y * self.y)

    def mod(self, mod: int) -> "Vector2":
        return self.mod2(mod, mod)

    def mod2(self, mx: int, my: int) -> "Vector2":
        return Vector2(self.x % mx, self.y % my)

    def norm(self) -> "Vector2":
        length = self.len()
        return Vector2(int(self.x / length), int(self.y / length))

UNIT = Vector2(1, 1)
ZERO = Vector2(0, 0)

UP = Vector2(0, -1)
RIGHT = Vector2(1, 0)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)

DIRECTIONS = (UP, RIGHT, DOWN, LEFT)
