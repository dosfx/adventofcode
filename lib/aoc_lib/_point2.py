from dataclasses import dataclass


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
