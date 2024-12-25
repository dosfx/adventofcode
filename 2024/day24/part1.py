from collections import deque
from dataclasses import dataclass


@dataclass
class Gate:
    left: str
    op: str
    right: str
    result: str

    def do(self, left: bool, right: bool) -> bool:
        if self.op == "AND":
            return left and right
        if self.op == "OR":
            return left or right
        if self.op == "XOR":
            return left ^ right
        raise Exception()


with open("input.txt") as file:
    wires = dict[str, bool]()
    while len(line := file.readline().strip()) > 0:
        name, val = line.split(": ")
        wires[name] = val == "1"
    gates = deque[Gate]()
    while len(line := file.readline().strip()) > 0:
        parts = line.split(" ")
        gates.append(Gate(parts[0], parts[1], parts[2], parts[4]))


while gates:
    cur = gates.popleft()
    if not cur.left in wires:
        gates.append(cur)
        continue
    if not cur.right in wires:
        gates.append(cur)
        continue
    wires[cur.result] = cur.do(wires[cur.left], wires[cur.right])

result = 0
for bit in sorted(filter(lambda k: k.startswith("z"), wires.keys()), reverse=True):
    result = (result << 1) | wires[bit]
print(result)
