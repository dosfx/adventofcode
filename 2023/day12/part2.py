from functools import cache
import re

with open("input.txt") as file:
    lines = file.readlines()

total = 0
for row,line in enumerate(lines[0:]):
    sub = 0
    [springs, check] = line.split()
    springs = "?".join([springs for _ in range(5)])
    check = ",".join([check for _ in range(5)])
    check = [int(c) for c in check.split(",")]
    length = len(springs)

    @cache
    def walker(springs: str, check: tuple) -> int:
        if len(check) == 0:
            if springs.count("#") == 0:
                return 1
            return 0
        if len(springs) == 0:
            return 0
        if springs[0] == ".":
            return walker(springs[1:], check)
        if springs[0] == "?":
            return walker("." + springs[1:], check) + walker("#" + springs[1:], check)
        if re.match(f"^[?#]{{{check[0]}}}", springs) is not None:
            if len(springs) == check[0]:
                return walker("", check[1:])
            elif springs[check[0]] == "." or springs[check[0]] == "?":
                return walker("." + springs[check[0] + 1:], check[1:])
        return 0
    total += walker(springs, tuple(check))
print(total)