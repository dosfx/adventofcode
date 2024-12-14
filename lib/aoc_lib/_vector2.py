from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

    @property
    def vertical(self) -> bool:
        return self == Direction.Up or self == Direction.Down

    @property
    def horizonal(self) -> bool:
        return self == Direction.Right or self == Direction.Left

    def clock(self) -> "Direction":
        return Direction((self.value + 1) % 4)

    def counter(self) -> "Direction":
        return Direction((self.value + 3) % 4)


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

    def shift(self, direction: Direction) -> "Vector2":
        match direction:
            case Direction.Up:
                return self.up()
            case Direction.Right:
                return self.right()
            case Direction.Down:
                return self.down()
            case Direction.Left:
                return self.left()

    def up(self) -> "Vector2":
        return Vector2(self.x, self.y - 1)

    def right(self) -> "Vector2":
        return Vector2(self.x + 1, self.y)

    def down(self) -> "Vector2":
        return Vector2(self.x, self.y + 1)

    def left(self) -> "Vector2":
        return Vector2(self.x - 1, self.y)
