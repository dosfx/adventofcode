
def jolts(bank: str, digits: int) -> str:
    if digits == 1:
        return max(bank)
    digit = max(bank[:-(digits - 1)])
    return digit + jolts(bank[bank.find(digit) + 1:], digits - 1)

total = 0
with open("input.txt") as f:
    for bank in f.readlines():
        bank = bank.strip()
        total += int(jolts(bank, 12))

print(total)
