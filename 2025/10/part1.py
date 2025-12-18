from collections import deque


Path = tuple[tuple[int, ...], ...]


def search(line: str) -> Path:
    split = line.split(" ")
    lights = split[0][1:-1]
    start = "".join(["." for _ in range(len(lights))])
    buttons = [tuple([int(n) for n in b[1:-1].split(",")])
               for b in split[1:-1]]
    queue: deque[tuple[str, Path]] = deque([(start, ())])
    seen: set[str] = set()
    while True:
        cur_lights, path = queue.popleft()
        for button in buttons:
            new_lights = cur_lights
            new_path = path + (button,)
            for i in button:
                new_lights = new_lights[:i] + ("#" if cur_lights[i]
                                               == "." else ".") + new_lights[i + 1:]
            if new_lights == lights:
                return new_path
            if new_lights in seen:
                continue
            seen.add(new_lights)
            queue.append((new_lights, new_path))


with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        total += len(search(line))
    print(total)
