with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

energized = set()
seen = set()
height = len(grid)
width = len(grid[0])

def beam(x: int, y: int, dx: int, dy: int) -> None:
    if (x, y, dx, dy) in seen:
        return
    seen.add((x, y, dx, dy))
    while 0 <= x and x < width and 0 <= y and y < height:
        energized.add((x, y))
        c = grid[y][x]
        if c == "|" and dx != 0:
            beam(x, y - 1, 0, -1)
            beam(x, y + 1, 0, 1)
            return
        elif c == "-" and dy != 0:
            beam(x - 1, y, -1, 0)
            beam(x + 1, y, 1, 0)
            return
        elif c == "\\":
            if dx == 1:
                dx = 0
                dy = 1
            elif dx == -1:
                dx = 0
                dy = -1
            elif dy == 1:
                dx = 1
                dy = 0
            else:
                dx = -1
                dy = 0
        elif c == "/":
            if dx == 1:
                dx = 0
                dy = -1
            elif dx == -1:
                dx = 0
                dy = 1
            elif dy == 1:
                dx = -1
                dy = 0
            else:
                dx = 1
                dy = 0
        x += dx
        y += dy

beam(0, 0, 1, 0)
print(len(energized))