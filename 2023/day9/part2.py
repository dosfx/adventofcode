def calc_diffs(nums: list) -> int:
    zero = True
    diffs = []
    for i in range(len(nums) - 1):
        diffs.append(d := nums[i + 1] - nums[i])
        if d != 0:
            zero = False
    sub = 0 if zero else calc_diffs(diffs)
    return diffs[0] - sub

total = 0
with open("input.txt") as file:
    for line in file.readlines():
        input = [int(s) for s in line.split()]
        total += input[0] - calc_diffs(input)

print(total)
