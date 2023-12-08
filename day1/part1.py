import re

total = 0
with open('input.txt') as file:
    for line in file:
        print(line, end='')
        line = re.sub(r'^[^\d]*', '', line)
        line = re.sub(r'[^\d]*$', '', line)
        total += int(line[0] + line[-1])

print()
print(total)