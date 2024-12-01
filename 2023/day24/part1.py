from dataclasses import dataclass
from typing import Tuple

@dataclass
class Hailstone:
    id: int
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int

    def at(self, a: float) -> Tuple[float, float, float]:
        return (self.x + (a * self.vx), self.y + (a * self.vy), self.z + (a * self.vz))

    def __repr__(self) -> str:
        return f"{self.id}: ({self.x},{self.y},{self.z})({self.vx},{self.vy},{self.vz})"

with open("input.txt") as file:
    stones = []
    for i,line in enumerate(file.readlines()):
        split = line.strip().split("@")
        stones.append(Hailstone(i, *[int(num.strip()) for num in split[0].split(",")], *[int(num.strip()) for num in split[1].split(",")]))

# for stone in stones:
#     print(stone)

area_min = 200000000000000
area_max = 400000000000000

total = 0
for i in range(len(stones)):
    for j in range(i + 1, len(stones)):
        # print()
        s0 = stones[i]
        s1 = stones[j]
        # print("Hailstone", s0)
        # print("Hailstone", s1)
        divisor = (s0.vy * s1.vx) - (s0.vx * s1.vy)
        if divisor == 0:
            # print("parallel")
            continue
        a = ((s1.vy * (s0.x - s1.x)) - (s1.vx * (s0.y - s1.y))) / divisor
        cross = s0.at(a)
        b = (cross[0] - s1.x) / s1.vx
        if b < 0 and a < 0:
            # print("past both")
            continue
        if a < 0:
            # print("past 0")
            continue
        if b < 0:
            # print("past 1")
            continue
        if area_min <= cross[0] and cross[0] <= area_max and area_min <= cross[1] and cross[1] <= area_max:
            # print("inside", cross)
            total += 1
            continue
        # print("outside", cross)
print(total)