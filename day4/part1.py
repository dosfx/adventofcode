total = 0
with open("input.txt") as file:
    for line in file:
        wins = line[10:40].split()
        nums = set(line[42:117].split())
        points = -1
        for win in wins:
            if win in nums:
                points += 1
        if points >= 0:
            total += pow(2, points)
print(total)