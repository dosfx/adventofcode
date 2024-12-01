
with open("input.txt") as file:
    instructions = [0 if c == "L" else 1 for c in file.readline().strip()]
    file.readline()
    nodes = {}
    for line in file.readlines():
        nodes[line[0:3]] = (line[7:10], line[12:15])

steps = 0
i = 0
cur = nodes["AAA"]
while True:
    next = cur[instructions[i]]
    steps += 1
    if next == "ZZZ":
        break
    cur = nodes[next]
    i += 1
    if i >= len(instructions):
        i = 0

print(steps)