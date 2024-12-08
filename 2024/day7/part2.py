def eval(cur: int, remaining: tuple[int, ...], target: int) -> bool:
    if len(remaining) == 0:
        return cur == target
    if eval(cur * remaining[0], remaining[1:], target): return True
    if eval(int(str(cur) + str(remaining[0])), remaining[1:], target): return True
    return eval(cur + remaining[0], remaining[1:], target)

with open("input.txt") as file:
    total = 0
    for line in file.readlines():
        target, nums = line.split(":")
        first, *remaining = nums.split()
        if eval(int(first), tuple([int(num) for num in remaining]), int(target)):
            total += int(target)
    print(total)