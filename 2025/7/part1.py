from aoc_lib import StrGrid


grid = StrGrid.from_file("input.txt")
rows = grid.rows()
_, top = next(rows)
grid.set(top.index("S"), 0, "|")
splits = 0
for y, row in rows:
    for x, c in enumerate(row):
        if grid.at(x, y - 1) == "|":
            if c == ".":
                grid.set(x, y, "|")
            elif c == "^":
                splits += 1
                grid.set(x - 1, y, "|")
                grid.set(x + 1, y, "|")
print(splits)
