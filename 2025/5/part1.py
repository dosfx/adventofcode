fresh = []
with open("input.txt") as f:
    while len(line := f.readline().strip()) > 0:
        start, end = [int(n) for n in line.split("-")]
        fresh.append((start, end))

    count = 0
    while len(line := f.readline()) > 0:
        num = int(line)
        for start, end in fresh:
            if start <= num and num <= end:
                count += 1
                break
print(count)
