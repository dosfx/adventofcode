total = 0
with open("input.txt") as f:
    for bank in f.readlines():
        bank = bank.strip()
        first = max(bank[:-1])
        second = max(bank[bank.find(first) + 1:])
        jolts = (int(first) * 10) + int(second)
        total += jolts
print(total)
