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
    total = 0
    for secret in map(int, file):
        for _ in range(2000):
            secret = evolve(secret)
        total += secret
    print(total)
