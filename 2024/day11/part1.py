import functools


with open("input.txt") as file:
    stones = [int(num) for num in file.readline().split()]

@functools.cache
def step(num: int, remaining: int) -> int:
    if remaining == 0:
        return 1
    if num == 0:
        return step(1, remaining - 1)
    snum = str(num)
    if len(snum) % 2 == 0:
        half = len(snum) // 2
        return step(int(snum[:half]), remaining - 1) + step(int(snum[half:]), remaining - 1)
    return step(num * 2024, remaining - 1)

total = 0
for stone in stones:
    total += step(stone, 25)
print(total)