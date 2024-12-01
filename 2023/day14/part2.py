with open("input.txt") as file:
    grid = [[c for c in line.strip()] for line in file.readlines()]


def north(grid):
    for i in range(len(grid)):
        for y in range(1, len(grid) - i):
            for x in range(len(grid[0])):
                if grid[y][x] == "O" and grid[y - 1][x] == ".":
                    grid[y][x] = "."
                    grid[y - 1][x] = "O"

def west(grid):
    for i in range(len(grid[0])):
        for x in range(1, len(grid[0]) - i):
            for y in range(len(grid)):
                if grid[y][x] == "O" and grid[y][x - 1] == ".":
                    grid[y][x] = "."
                    grid[y][x - 1] = "O"

def south(grid):
    for i in range(len(grid)):
        for y in range(len(grid) - 2, i - 1, -1):
            for x in range(len(grid[0])):
                if grid[y][x] == "O" and grid[y + 1][x] == ".":
                    grid[y][x] = "."
                    grid[y + 1][x] = "O"

def east(grid):
    for i in range(len(grid[0])):
        for x in range(len(grid[0]) - 2, i - 1, -1):
            for y in range(len(grid)):
                if grid[y][x] == "O" and grid[y][x + 1] == ".":
                    grid[y][x] = "."
                    grid[y][x + 1] = "O"

def cycle(grid):
    north(grid)
    west(grid)
    south(grid)
    east(grid)

def score(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                total += len(grid) - y
    return total

seen = []
while True:
    cycle(grid)
    check = "".join(["".join(row) for row in grid])
    for loop in range(len(seen)):
        if check == seen[loop]:
            break
    else:
        seen.append(check)
        continue
    break

count = len(seen)

length = count - loop
total = 1000000000 - count - 1
remainder = total % length
final_grid = [list(seen[remainder + loop][y:y + len(grid)]) for y in range(0, len(seen[0]), len(grid))]
print(score(final_grid))