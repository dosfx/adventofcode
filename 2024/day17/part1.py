with open("input.txt") as file:
    reg_a = int(file.readline().split()[2])
    reg_b = int(file.readline().split()[2])
    reg_c = int(file.readline().split()[2])
    file.readline()
    program = [int(c) for c in file.readline().split()[1].split(",")]


def combo(operand: int) -> int:
    if operand <= 3:
        return operand
    if operand == 4:
        return reg_a
    if operand == 5:
        return reg_b
    if operand == 6:
        return reg_c
    raise Exception(f"{operand} is invalid")


ins = 0
output: list[int] = []
while ins < len(program):
    operand = program[ins + 1]
    match program[ins]:
        case 0:
            # adv
            reg_a = reg_a // (2 ** combo(operand))
        case 1:
            # bxl
            reg_b = reg_b ^ operand
        case 2:
            # bst
            reg_b = combo(operand) % 8
        case 3:
            # jnz
            if reg_a != 0:
                ins = operand
                continue
        case 4:
            # bxc
            reg_b = reg_c ^ reg_b
        case 5:
            # out
            output.append(combo(operand) % 8)
        case 6:
            # bdv
            reg_b = reg_a // (2 ** combo(operand))
        case 7:
            # cdv
            reg_c = reg_a // (2 ** combo(operand))
    ins += 2

print(reg_a, reg_b, reg_c)
print(",".join([str(num) for num in output]))
