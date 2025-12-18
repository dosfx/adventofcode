import z3


def search(line: str) -> int:
    split = line.strip().split(" ")
    jolts = [int(n) for n in split[-1][1:-1].split(",")]
    buttons = [[int(n) for n in b[1:-1].split(",")] for b in split[1:-1]]
    vars = [z3.Int(f"v{i}") for i in range(len(buttons))]
    opt = z3.Optimize()
    for i, jolt in enumerate(jolts):
        opt.add(
            z3.Sum((vars[j] for j, button in enumerate(
                buttons) if i in button)) == jolt
        )
    opt.add([v >= 0 for v in vars])
    opt.minimize(z3.Sum(*vars))
    opt.check()
    m = opt.model()
    answer = sum([m[v].as_long() for v in vars])
    return answer


with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        total += search(line)
    print(total)
