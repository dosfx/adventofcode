from collections import deque
import functools
from aoc_lib import Vector2

pad_num = {
    "7": Vector2(0, 0),
    "8": Vector2(1, 0),
    "9": Vector2(2, 0),
    "4": Vector2(0, 1),
    "5": Vector2(1, 1),
    "6": Vector2(2, 1),
    "1": Vector2(0, 2),
    "2": Vector2(1, 2),
    "3": Vector2(2, 2),
    "0": Vector2(1, 3),
    "A": Vector2(2, 3),
}


pad_dir = {
    "^": Vector2(1, 0),
    "A": Vector2(2, 0),
    "<": Vector2(0, 1),
    "v": Vector2(1, 1),
    ">": Vector2(2, 1),
}


@functools.cache
def move(start: Vector2, end: Vector2, avoid: Vector2) -> tuple[str, ...]:
    diff = end - start
    seq = ""
    if diff.x > 0:
        seq += ">" * diff.x
    if diff.x < 0:
        seq += "<" * abs(diff.x)
    if diff.y > 0:
        seq += "v" * diff.y
    if diff.y < 0:
        seq += "^" * abs(diff.y)
    ret = tuple[str]()
    if diff.x != 0 and diff.y != 0:
        if Vector2(start.x + diff.x, start.y) != avoid:
            ret += (seq + "A",)
        if Vector2(start.x, start.y + diff.y) != avoid:
            ret += (seq[::-1] + "A",)
        return ret
    return (seq + "A",)


@functools.cache
def move_num(cur: str, target: str) -> tuple[str, ...]:
    return move(pad_num[cur], pad_num[target], Vector2(0, 3))


def gen_num(in_seq: str) -> list[str]:
    last = "A"
    seqs = deque([""])
    for c in in_seq:
        chunks = move_num(last, c)
        for _ in range(len(seqs)):
            cur = seqs.popleft()
            for chunk in chunks:
                seqs.append(cur + chunk)
        last = c
    return list(seqs)


@functools.cache
def move_dir(cur: str, target: str) -> tuple[str, ...]:
    return move(pad_dir[cur], pad_dir[target], Vector2(0, 0))


@functools.cache
def solve(seq: str, depth: int) -> int:
    if depth == 0:
        return len(seq)
    last = "A"
    total = 0
    for c in seq:
        total += min(map(lambda cur: solve(cur, depth - 1), move_dir(last, c)))
        last = c
    return total


with open("input.txt") as file:
    total = 0
    for line in map(str.strip, file):
        best = min(map(lambda seq: solve(seq, 25), gen_num(line)))
        total += best * int(line.replace("A", ""))
    print(total)
