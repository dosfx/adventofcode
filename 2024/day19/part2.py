import functools


@functools.cache
def ways(towel: str) -> int:
    if len(towel) == 0:
        return 1
    ret = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            ret += ways(towel[len(pattern):])
    return ret


with open("input.txt") as file:
    patterns = tuple(map(str.strip, file.readline().split(", ")))
    file.readline()
    count = 0
    for line in map(str.strip, file.readlines()):
        count += ways(line)
    print(count)