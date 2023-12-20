DELTA = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}

with open("input.txt") as file:
    coords = [(0, 0)]
    x = y = 0
    xsum = ysum = 0
    for line in file.readlines():
        [direction, num] = line.split(" ")[0:2]
        num = int(num)
        (dx, dy) = DELTA[direction]
        x += num * dx
        y += num * dy
        xsum += abs(num * dx)
        ysum += abs(num * dy)
        coords.append((x, y))

xy = 0
yx = 0
for i in range(len(coords) - 1):
    xy += coords[i][0] * coords[i + 1][1]
    yx += coords[i][1] * coords[i + 1][0]

print(((xy - yx) / 2) + (xsum / 2) + (ysum / 2) + 1)