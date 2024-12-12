from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


@dataclass(frozen=True)
class Point2:
    x: int
    y: int

    def __add__(self, other: "Point2") -> "Point2":
        return Point2(self.x + other.x, self.y + other.y)

    def __neg__(self) -> "Point2":
        return Point2(-self.x, -self.y)

    def __sub__(self, other: "Point2") -> "Point2":
        return Point2(self.x - other.x, self.y - other.y)

    def __mul__(self, scale: int) -> "Point2":
        return Point2(self.x * scale, self.y * scale)

    def shift(self, direction: Direction) -> "Point2":
        match direction:
            case Direction.Up:
                return self.up()
            case Direction.Right:
                return self.right()
            case Direction.Down:
                return self.down()
            case Direction.Left:
                return self.left()

    def up(self) -> "Point2":
        return Point2(self.x, self.y - 1)

    def right(self) -> "Point2":
        return Point2(self.x + 1, self.y)

    def down(self) -> "Point2":
        return Point2(self.x, self.y + 1)

    def left(self) -> "Point2":
        return Point2(self.x - 1, self.y)
