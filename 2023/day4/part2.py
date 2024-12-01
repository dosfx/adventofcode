with open("input.txt") as file:
    lines = file.readlines()

counts = [0 for _ in range(len(lines))]
for i in range(len(lines) - 1, -1, -1):
    nums = set(lines[i][42:117].split())
    points = 0
    count = 1
    for win in lines[i][10:40].split():
        if win in nums:
            points += 1
            count += counts[i + points]
    counts[i] = count

print(sum(counts))
