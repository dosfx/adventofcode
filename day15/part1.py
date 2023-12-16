with open("input.txt") as file:
    input = file.readline().strip()

def hash(input: str) -> int:
    ret = 0
    for c in input:
        ret += ord(c)
        ret *= 17
        ret = ret % 256
    return ret

total = 0
for step in input.split(","):
    total += hash(step)
print(total)