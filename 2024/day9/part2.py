from dataclasses import dataclass

@dataclass(eq=False)
class Slot:
    length: int
    id: int | None


with open("input.txt") as file:
    format = file.readline()

id = 0
blank = False
layout: list[Slot] = []
for c in format:
    if blank:
        append = None
    else:
        append = id
        id += 1
    layout.append(Slot(int(c), append))
    blank = not blank

end = len(layout) - 1
while end > 0:
    if layout[end].id is not None:
        for start in range(end):
            if layout[start].id is None and layout[end].length <= layout[start].length:
                diff = layout[start].length - layout[end].length
                if diff > 0:
                    layout[start].length = layout[end].length
                    layout.insert(start + 1, Slot(diff, None))
                    end += 1
                layout[start].id = layout[end].id
                layout[end].id = None
                if end + 1 < len(layout) and layout[end + 1].id is None:
                    layout[end].length += layout[end + 1].length
                    layout.remove(layout[end + 1])
                if 0 <= end - 1 and layout[end - 1].id is None:
                    layout[end].length += layout[end - 1].length
                    layout.remove(layout[end - 1])
                    end -= 1
                break
    end -= 1

total = 0
i = 0
for slot in layout:
    if slot.id is None:
        i += slot.length
        continue
    for _ in range(slot.length):
        total += i * slot.id
        i += 1
print(total)