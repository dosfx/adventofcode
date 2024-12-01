from dataclasses import dataclass
from sympy import symbols, solve
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
    for i, line in enumerate(file.readlines()):
        split = line.strip().split("@")
        stones.append(Hailstone(i, *[int(num.strip()) for num in split[0].split(",")], *[
                      int(num.strip()) for num in split[1].split(",")]))

# for stone in stones:
#     print(stone)

x = symbols('x')
y = symbols('y')
z = symbols('z')
vx = symbols('vx')
vy = symbols('vy')
vz = symbols('vz')

s0 = stones[0]
s1 = stones[1]
s2 = stones[2]

x0, y0, z0 = s0.x, s0.y, s0.z
x1, y1, z1 = s1.x, s1.y, s1.z
x2, y2, z2 = s2.x, s2.y, s2.z

vx0, vy0, vz0 = s0.vx, s0.vy, s0.vz
vx1, vy1, vz1 = s1.vx, s1.vy, s1.vz
vx2, vy2, vz2 = s2.vx, s2.vy, s2.vz

sols = solve(
    [(x-x0)*(vy-vy0)-(y-y0)*(vx-vx0), (y-y0)*(vz-vz0)-(z-z0)*(vy-vy0),
        (x-x1)*(vy-vy1)-(y-y1)*(vx-vx1), (y-y1)*(vz-vz1)-(z-z1)*(vy-vy1),
        (x-x2)*(vy-vy2)-(y-y2)*(vx-vx2), (y-y2)*(vz-vz2)-(z-z2)*(vy-vy2)],
    [x, y, z, vx, vy, vz], dict=True)

# select solution with integer speed components
for s in sols:
    if s[vx] == int(s[vx]) and s[vy] == int(s[vy]) and s[vz] == int(s[vz]):
        print(s)
        break
print(s[x] + s[y] + s[z])
