from typing import cast


with open("input.txt") as file:
    format = file.readline()

id = 0
blank = False
layout: list[int | None] = []
for c in format:
    if blank:
        append = None
    else:
        append = id
        id += 1
    for _ in range(int(c)):
        layout.append(append)
    blank = not blank

start = 0
end = len(layout) - 1
while start < end:
    if layout[start] is None:
        layout[start] = layout[end]
        layout[end] = None
        while layout[end] is None:
            end -= 1
    start += 1

total = 0
i = 0
while layout[i] is not None:
    total += i * cast(int, layout[i])
    i += 1
print(total)