from collections import deque


with open("input.txt") as file:
    reg_a = int(file.readline().split()[2])
    reg_b = int(file.readline().split()[2])
    reg_c = int(file.readline().split()[2])
    file.readline()
    program = tuple([int(c) for c in file.readline().split()[1].split(",")])


def run(reg_a: int, reg_b: int, reg_c: int) -> tuple[int, ...]:
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
    return tuple(output)


check = deque([0])
for i in range(len(program)):
    expected = tuple(program[len(program)-i-1:])
    for _ in range(len(check)):
        v = check.popleft()
        for k in range(8):
            reg_a = (8 * v) + k
            output = run(reg_a, reg_b, reg_c)
            if output == expected:
                check.append(reg_a)

print(min(check))
