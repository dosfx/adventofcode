from heapq import heappop, heappush

left: list[int] = []
right: list[int] = []

with open("input.txt") as file:
    for line in file:
        lstr, rstr = line.split()
        heappush(left, int(lstr))
        heappush(right, int(rstr))

total = 0
while len(left) > 0:
    lnum = heappop(left)
    rnum = heappop(right)
    total += abs(lnum - rnum)

print(total)