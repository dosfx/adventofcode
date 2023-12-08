import re

NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
LOOKUP = { NUMBERS[i]: i for i in range(10)}
num_group = f'({"|".join(NUMBERS)}|{"|".join([str(i) for i in range(10)])})'
firstRe = re.compile(r'^.*?' + num_group)
lastRe = re.compile(r'.*' + num_group + r'.*$')

total = 0
with open('input.txt') as file:
    for line in file:
        print(line, end='')
        first = re.search(firstRe, line).group(1)
        last = re.search(lastRe, line).group(1)
        first = (LOOKUP[first] if first in LOOKUP else int(first)) * 10
        last = LOOKUP[last] if last in LOOKUP else int(last)
        total += first + last

print()
print(total)