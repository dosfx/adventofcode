from dataclasses import dataclass
import re
from typing import Dict, List, Tuple

re_flow = re.compile(r"([a-z]+){([^}]+)}")
re_part = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
re_rule = re.compile(r"(?:(a|m|s|x)(<|>)(\d+):)?([a-zA-Z]+)")

class Part:
    def __init__(self, x: int, m: int, a: int, s: int):
        self.cats = {
            "x": x,
            "m": m,
            "a": a,
            "s": s,
        }

@dataclass
class Rule:
    cat: str
    op: str
    other: int
    result: str

    @staticmethod
    def parse(text: str):
        match = re.match(re_rule, text)
        cat, op, other, result = match.groups()
        if other is not None:
            other = int(other)
        return Rule(cat, op, other, result)

    def __repr__(self) -> str:
        return (f"{self.cat}{self.op}{self.other}:" if self.cat is not None else "") + self.result

    def invert(self) -> "Rule":
        if self.cat is None:
            return self
        if self.op == "<":
            return Rule(self.cat, ">", self.other - 1, self.result)
        return Rule(self.cat, "<", self.other + 1, self.result)

class Flow:
    def __init__(self, line):
        match = re.match(re_flow, line)
        self.id = match.group(1)
        self.rules = [Rule.parse(text) for text in match.group(2).split(",")]


flows: Dict[str, Flow] = {}
with open("input.txt") as file:
    while (line := file.readline().strip()) != "":
        flow = Flow(line)
        flows[flow.id] = flow

def match(rule: Rule, input: int) -> bool:
    return input < rule.other if rule.op == "<" else input > rule.other

def count(rules: Tuple[Rule]) -> int:
    lines = {
        "x": [],
        "m": [],
        "a": [],
        "s": [],
    }
    for rule in rules:
        if rule.cat is None:
            continue
        lines[rule.cat].append(rule)
    total = 1
    for line in lines.values():
        if len(line) == 0:
            cur = 4000
        else:
            cur = 0
            check_points = set()
            for rule in line:
                check_points.add(rule.other - 1)
                check_points.add(rule.other)
                check_points.add(rule.other + 1)
            start = 1
            for check in sorted(check_points):
                if all(match(rule, check) for rule in line):
                    if start is not None:
                        cur += check - start + 1
                    start = check
                else:
                    start = None
            if start is not None:
                cur += 4000 - start + 1
        total *= cur
    return total

total = 0
stack: List[Tuple[Flow, Tuple[Rule]]] = [(flows["in"], ())]
while len(stack) > 0:
    flow, path = stack.pop()
    for rule in flow.rules:
        if rule.result == "A":
            total += count(path + (rule,))
        elif rule.result != "R":
            stack.append((flows[rule.result], path + (rule,)))
        path += (rule.invert(),)
print(total)
