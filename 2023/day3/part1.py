import re

total = 0
with open("input.txt") as file:
    lines = file.readlines()
re_sym = re.compile(r"[^.\d]")
re_num = re.compile(r"([^.\d]?)(\d+)")
lines = [l.strip() for l in lines]
line_count = len(lines)
line_len = len(lines[0])
for i in range(line_count):
    for match in re.finditer(re_num, lines[i]):
        num = int(match.group(2))
        if len(match.group(1)) > 0:
            total += num
            continue
        start = max(0, match.start(2) - 1)
        end = min(line_len, match.end(2) + 1)
        if re.search(re_sym, lines[i][end - 1]) is not None:
            total += num
            continue
        if i > 0 and re.search(re_sym, lines[i - 1][start:end]) is not None:
            total += num
            continue
        if i < (line_count - 1) and re.search(re_sym, lines[i + 1][start:end]) is not None:
            total += num
            continue
print(total)