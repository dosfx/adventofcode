with open("input.txt") as file:
    grid = [[c for c in line.strip()] for line in file.readlines()]

for i in range(len(grid)):
    for y in range(1, len(grid) - i):
        for x in range(len(grid[0])):
            if grid[y][x] == "O" and grid[y - 1][x] == ".":
                grid[y][x] = "."
                grid[y - 1][x] = "O"

total = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "O":
            total += len(grid) - y

print(total)