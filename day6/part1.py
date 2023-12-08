
# Time:      7  15   30
# Distance:  9  40  200

time = [7, 15, 30]
distance = [9, 40, 200]

# Time:        47     84     74     67
# Distance:   207   1394   1209   1014

time = [47, 84, 74, 67]
distance = [207, 1394, 1209, 1014]

total = 1

for i in range(len(time)):
    count = 0
    for t in range(time[i] + 1):
        travel = (time[i] - t) * t
        if travel > distance[i]:
            count += 1
    total *= count

print(total)