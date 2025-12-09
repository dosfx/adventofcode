from heapq import heappop, heappush


Range = tuple[int, int]

with open("input.txt") as f:
    fresh_ranges: list[Range] = []
    while len(line := f.readline().strip()) > 0:
        start, end = [int(n) for n in line.split("-")]
        heappush(fresh_ranges, (start, end))

total = 0
start = 0
end = -1
while len(fresh_ranges) > 0:
    cur_start, cur_end = heappop(fresh_ranges)
    if end < cur_start:
        total += end - start + 1
        start = cur_start
        end = cur_end
    else:
        end = max(end, cur_end)
total += end - start + 1
print(total)
