def signof(a: int, b: int) -> int:
    if a == b: return 0
    return int(abs(a - b) / (a - b))

def check(levels: list[int]) -> bool:
    last = levels[0]
    sign = signof(levels[1], last)
    for cur in levels[1:]:
        diff = cur - last
        if diff == 0:
            return False
        if abs(diff) > 3:
            return False
        if sign != signof(cur, last):
            return False
        last = cur
    return True


with open("input.txt") as file:
    safe = 0
    for line in file:
        levels = [int(num) for num in line.split()]
        if check(levels):
            safe += 1
            continue
        for i in range(len(levels)):
            if check(levels[0:i] + levels[i + 1:]):
                safe +=1
                break
    print(safe)