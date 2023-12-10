with open("input.txt") as file:
# with open("example3.txt") as file:
    instructions = [0 if c == "L" else 1 for c in file.readline().strip()]
    file.readline()
    nodes = {}
    for line in file.readlines():
        nodes[line[0:3]] = (line[7:10], line[12:15])

def count_steps(cur: str):
    steps = 0
    i = 0
    while True:
        next = cur[instructions[i]]
        steps += 1
        if next[2] == "Z":
            return steps
        cur = nodes[next]
        i += 1
        if i >= len(instructions):
            i = 0

multiples = []
for key in nodes.keys():
    if key[2] == "A":
        m = count_steps(nodes[key])
        multiples.append(m)
        print(m)

import math
print(math.lcm(*multiples))