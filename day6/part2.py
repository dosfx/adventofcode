
# Time:      7  15   30
# Distance:  9  40  200

time = 71530
distance = 940200

# Time:        47     84     74     67
# Distance:   207   1394   1209   1014

time = 47847467
distance = 207139412091014

t = 0
while (time - t) * t <= distance:
    t += 1

print(time - (t * 2) + 1)