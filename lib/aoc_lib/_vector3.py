from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Vector3:
    x: int
    y: int
    z: int

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self) -> "Vector3":
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scale: int) -> "Vector3":
        return Vector3(self.x * scale, self.y * scale, self.z * scale)

    def dist(self, other: "Vector3") -> float:
        return sqrt(self.dist2(other))

    def dist2(self, other: "Vector3") -> int:
        return self.__sub__(other).len2()

    def len(self) -> float:
        return sqrt(self.len2())

    def len2(self) -> int:
        return (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

    def mod(self, mod: int) -> "Vector3":
        return self.mod2(mod, mod, mod)

    def mod2(self, mx: int, my: int, mz: int) -> "Vector3":
        return Vector3(self.x % mx, self.y % my, self.z % mz)
