from typing import List

def vert_equal(pattern: List[str], a: int, b: int) -> bool:
    for y in range(len(pattern)):
        if pattern[y][a] != pattern[y][b]:
            return False
    return True

def solve(pattern: List[str]) -> int:
    for x in range(1, len(pattern[0])):
        if vert_equal(pattern, x - 1, x):
            for check in range(x + 1, len(pattern[0])):
                other = x - (check - x) - 1
                if other >= 0 and not vert_equal(pattern, other , check):
                    break
            else:
                return x
    for y in range(1, len(pattern)):
        if pattern[y - 1] == pattern[y]:
            for check in range(y + 1, len(pattern)):
                other = y - (check - y) - 1
                if other >= 0 and pattern[other] != pattern[check]:
                    break
            else:
                return y * 100
    return 0

with open("input.txt") as file:
    pattern = []
    total = 0
    for line in file.readlines():
        line = line.strip()
        if line == "":
            total += solve(pattern)
            pattern.clear()
        else:
            pattern.append(line)
    total += solve(pattern)

print(total)
