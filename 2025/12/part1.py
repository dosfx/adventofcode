from typing import Iterable

from aoc_lib import StrGrid


class Shape:
    def __init__(self, data: Iterable[bool]) -> None:
        self.data = tuple(data)
        self.area = sum(1 if d else 0 for d in self.data)
        self.x = 0
        self.y = 0

    def place(self, x: int, y: int, grid: StrGrid, c: str = "#") -> bool:
        for iy in range(3):
            for ix in range(3):
                if self.filled(ix, iy) and grid.at(x + ix, y + iy) != ".":
                    return False
        self.x = x
        self.y = y
        for iy in range(3):
            for ix in range(3):
                if self.filled(ix, iy):
                    grid.set(x + ix, y + iy, c)
        return True

    def remove(self, grid: StrGrid) -> None:
        for iy in range(3):
            for ix in range(3):
                if self.filled(ix, iy):
                    grid.set(self.x + ix, self.y + iy, ".")

    def filled(self, x: int, y: int) -> bool:
        return self.data[(y * 3) + x]

    @property
    def copy(self) -> "Shape":
        return Shape(self.data)

    @property
    def vertical(self) -> "Shape":
        return Shape(
            self.data[6:9] +
            self.data[3:6] +
            self.data[0:3]
        )

    @property
    def horizontal(self) -> "Shape":
        return Shape((
            self.data[2], self.data[1], self.data[0],
            self.data[5], self.data[4], self.data[3],
            self.data[8], self.data[7], self.data[6],
        ))

    @property
    def clock(self) -> "Shape":
        return Shape((
            self.data[6], self.data[3], self.data[0],
            self.data[7], self.data[4], self.data[1],
            self.data[8], self.data[5], self.data[2],
        ))

    @property
    def transforms(self) -> Iterable["Shape"]:
        return set([
            self,
            self.vertical,
            self.horizontal,
            self.clock,
            self.clock.vertical,
            self.clock.horizontal,
            self.clock.clock,
            self.clock.clock.clock,
        ])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.data == other.data

    def __hash__(self) -> int:
        return hash(self.data)

    def __str__(self) -> str:
        return "\n".join(
            "".join("#" if self.filled(x, y) else "." for x in range(3))
            for y in range(3)
        )

    @staticmethod
    def parse(lines: list[str]) -> "Shape":
        return Shape((c == "#" for c in "".join(
            (line.strip() for line in lines))
        ))


with open("input.txt") as f:
    shapes: list[Shape] = []
    for _ in range(6):
        f.readline()
        shapes.append(Shape.parse([f.readline() for _ in range(3)]))
        f.readline()
    lines = f.readlines()

for shape in shapes:
    t = shape.transforms
    for y in range(3):
        for s in t:
            for x in range(3):
                print("#" if s.filled(x, y) else ".", end="")
            print(" ", end="")
        print()
    print()
print("---")


def search(grid: StrGrid, remaining: list[Shape], depth: int) -> bool:
    seen: set[Shape] = set()
    for i, shape in enumerate(remaining):
        if shape in seen:
            continue
        seen.add(shape)
        for transform in shape.transforms:
            for y in range(grid.height - 2):
                for x in range(grid.width - 2):
                    if transform.place(x, y, grid):  # , chr(depth + 0x41)):
                        if len(remaining) == 1:
                            return True
                        # print(f"\033[{grid.height + 2}A")
                        # print(grid)
                        # print("-----")
                        if search(grid, remaining[:i] + remaining[i + 1:], depth + 1):
                            return True
                        transform.remove(grid)
    return False


count = 0
for line in lines:
    split = line.split(":")
    w, h = [int(n) for n in split[0].split("x")]
    req_shapes: list[Shape] = []
    for i, n in enumerate(split[1].split()):
        for _ in range(int(n)):
            req_shapes.append(shapes[i].copy)
    grid = StrGrid.from_size(w, h, ".")
    if sum(s.area for s in req_shapes) > w * h:
        print(False, "trivial")
        continue

    count += 1
    # solver not needed, but still happy I made it!
    # print(search(grid, req_shapes, 0))
    # print(grid)
    # print("---")
print(count)
