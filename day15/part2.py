from dataclasses import dataclass
from typing import List

@dataclass
class Lens:
    label: str
    focal: int

    def __repr__(self) -> str:
        return f"[{self.label} {self.focal}]"


def hash(input: str) -> int:
    ret = 0
    for c in input:
        ret += ord(c)
        ret *= 17
        ret = ret % 256
    return ret

def insert(box: List[Lens], lens: Lens) -> None:
    for i in range(len(box)):
        if box[i].label == lens.label:
            box[i] = lens
            break
    else:
        box.append(lens)

def remove(box: List[Lens], label: str) -> None:
    for i in range(len(box)):
        if box[i].label == label:
            box.remove(box[i])
            break

with open("input.txt") as file:
    input = file.readline().strip()
boxes = {}
for step in input.split(","):
    if step[-1:] == "-":
        label = step[:-1]
        focal = None
    else:
        [label, focal] = step.split("=")
        focal = int(focal)
    index = hash(label)
    if index not in boxes:
        boxes[index] = []
    box = boxes[index]
    if focal is not None:
        insert(box, Lens(label, focal))
    else:
        remove(box, label)

total = 0
for index,box in boxes.items():
    for i,lens in enumerate(box):
        total += (index + 1) * (i + 1) * lens.focal
print(total)