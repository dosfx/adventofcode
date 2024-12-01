from typing import List, Optional

def vert_equal(pattern: List[List[str]], a: int, b: int) -> bool:
    for y in range(len(pattern)):
        if pattern[y][a] != pattern[y][b]:
            return False
    return True

def hori_equal(pattern: List[List[str]], a: int, b: int) -> bool:
    for x in range(len(pattern[0])):
        if pattern[a][x] != pattern[b][x]:
            return False
    return True

def solve(pattern: List[List[str]], ignore: int) -> Optional[int]:
    for x in range(1, len(pattern[0])):
        if vert_equal(pattern, x - 1, x):
            for check in range(x + 1, len(pattern[0])):
                other = x - (check - x) - 1
                if other >= 0 and not vert_equal(pattern, other , check):
                    break
            else:
                if x != ignore:
                    return x
    for y in range(1, len(pattern)):
        if hori_equal(pattern, y - 1, y):
            for check in range(y + 1, len(pattern)):
                other = y - (check - y) - 1
                if other >= 0 and not hori_equal(pattern, other, check):
                    break
            else:
                score = y * 100
                if score != ignore:
                    return score
    return None

def flip(pattern: List[List[str]], x: int, y: int) -> None:
    pattern[y][x] = "#" if pattern[y][x] == "." else "."

def fudge(pattern: List[List[str]]) -> int:
    ignore = solve(pattern, -1)
    for y in range(len(pattern)):
        for x in range(len(pattern[y])):
            flip(pattern, x, y)
            if (num := solve(pattern, ignore)) is not None:
                return num
            flip(pattern, x, y)
    print("BAD")

with open("input.txt") as file:
    pattern = []
    total = 0
    for line in file.readlines():
        line = [c for c in line.strip()]
        if len(line) == 0:
            total += fudge(pattern)
            pattern.clear()
        else:
            pattern.append(line)
    total += fudge(pattern)

print(total)
