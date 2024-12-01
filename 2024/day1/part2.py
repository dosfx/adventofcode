left: list[int] = []
right: dict[int, int] = {}

with open("input.txt") as file:
    for line in file:
        l, r = [int(num) for num in line.split()]
        left.append(l)
        if not r in right:
            right[r] = 0
        right[r] += 1

total = 0
for l in left:
    if l in right:
        total += l * right[l]

print(total)