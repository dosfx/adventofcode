from collections import deque
import functools


def mix(secret: int, value: int) -> int:
    return secret ^ value


def prune(secret: int) -> int:
    return secret % 16777216


@functools.cache
def evolve(secret: int) -> int:
    result = secret * 64
    secret = mix(secret, result)
    secret = prune(secret)
    result = secret // 32
    secret = mix(secret, result)
    secret = prune(secret)
    result = secret * 2048
    secret = mix(secret, result)
    secret = prune(secret)
    return secret


with open("input.txt") as file:
    scores = dict[tuple[int, ...], int]()
    for secret in map(int, file):
        last = secret % 10
        diffs = deque[int]()
        for _ in range(3):
            secret = evolve(secret)
            cur = secret % 10
            diffs.append(cur - last)
            last = cur
        seen = set[tuple[int, ...]]()
        for _ in range(1997):
            secret = evolve(secret)
            cur = secret % 10
            diffs.append(cur - last)
            last4 = tuple(diffs)
            diffs.popleft()
            last = cur
            if last4 in seen:
                continue
            seen.add(last4)
            scores[last4] = scores.get(last4, 0) + cur
    print(max(scores.values()))
