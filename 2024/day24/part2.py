from dataclasses import dataclass


@dataclass
class Gate:
    left: str
    op: str
    right: str
    result: str


with open("input.txt") as file:
    wires = dict[str, bool]()
    while len(line := file.readline().strip()) > 0:
        name, val = line.split(": ")
        wires[name] = val == "1"
    gates_in = dict[str, list[Gate]]()
    gates_out = dict[str, Gate]()
    while len(line := file.readline().strip()) > 0:
        parts = line.split(" ")
        gate = Gate(parts[0], parts[1], parts[2], parts[4])
        gates_in[gate.left] = gates_in.get(gate.left, []) + [gate]
        gates_in[gate.right] = gates_in.get(gate.right, []) + [gate]
        assert gate.result not in gates_out
        gates_out[gate.result] = gate

swaps = set[str]()
for i in range(1, 45):
    gate = gates_out[f"z{i:02}"]
    if gate.op != "XOR":
        swaps.add(gate.result)
print(swaps)
for i in range(1, 45):
    num = f"{i:02}"
    gates = gates_in["x" + num]
    and0 = gates[0] if gates[0].op == "AND" else gates[1]
    xor0 = gates[0] if gates[0].op == "XOR" else gates[1]
    gates = gates_in[xor0.result]
    if len(gates) != 2:
        swaps.add(xor0.result)
    else:
        and1 = gates[0] if gates[0].op == "AND" else gates[1]
        xor1 = gates[0] if gates[0].op == "XOR" else gates[1]
        if xor1.result != ("z" + num):
            swaps.add(xor1.result)

    if and0.result not in gates_in:
        swaps.add(and0.result)
        continue
    gates = gates_in[and0.result]
    if len(gates) != 1:
        swaps.add(and0.result)
print(",".join(sorted(swaps)))
