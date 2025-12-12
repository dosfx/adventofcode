from heapq import heappop, heappush
import itertools
from aoc_lib._vector3 import Vector3

with open("input.txt") as f:
    points = [Vector3(*[int(n) for n in line.split(",")])
              for line in f.readlines()]


distances: list[tuple[int, Vector3, Vector3]] = []
for p1, p2 in itertools.combinations(points, 2):
    heappush(distances, (p1.dist2(p2), p1, p2))


circuits: list[set[Vector3]] = []


def findp(p: Vector3) -> set[Vector3] | None:
    for circuit in circuits:
        if p in circuit:
            return circuit
    return None


for _ in range(1000):
    _, p1, p2 = heappop(distances)
    p1_circuit = findp(p1)
    p2_circuit = findp(p2)
    if p1_circuit is None:
        if p2_circuit is None:
            circuits.append({p1, p2})
        else:
            p2_circuit.add(p1)
    else:
        if p1_circuit is p2_circuit:
            continue
        if p2_circuit is None:
            p1_circuit.add(p2)
        else:
            circuits.remove(p2_circuit)
            for p in p2_circuit:
                p1_circuit.add(p)

lengths: list[int] = []
for circuit in circuits:
    heappush(lengths, -len(circuit))

total = 1
for _ in range(3):
    total *= -heappop(lengths)
print(total)