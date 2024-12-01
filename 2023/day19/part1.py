import re
from typing import Dict

re_flow = re.compile(r"([a-z]+){([^}]+)}")
re_part = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
re_rule = re.compile(r"(?:(a|m|s|x)(<|>)(\d+):)?([a-zA-Z]+)")

class Part:
    def __init__(self, text: str):
        match = re.match(re_part, text)
        self.cats = {
            "x": int(match.group(1)),
            "m": int(match.group(2)),
            "a": int(match.group(3)),
            "s": int(match.group(4)),
        }

class Rule:
    def __init__(self, text: str):
        match = re.match(re_rule, text)
        (self.cat, self.op, self.other, self.result) = match.groups()
        if self.other is not None:
            self.other = int(self.other)

    def __repr__(self) -> str:
        return (f"{self.cat}{self.op}{self.other}:" if self.cat is not None else "") + self.result

    def match(self, input: Part) -> bool:
        if self.cat is not None:
            cat = input.cats[self.cat]
            return cat < self.other if self.op == "<" else cat > self.other
        return True

class Flow:
    def __init__(self, line):
        match = re.match(re_flow, line)
        self.id = match.group(1)
        self.rules = [Rule(text) for text in match.group(2).split(",")]

    def send(self, input: Part) -> str:
        for rule in self.rules:
            if rule.match(input):
                return rule.result


flows: Dict[str, Flow] = {}
with open("input.txt") as file:
    while (line := file.readline().strip()) != "":
        flow = Flow(line)
        flows[flow.id] = flow
    total = 0
    while (line := file.readline().strip()) != "":
        part = Part(line)
        flow = flows["in"]
        for _ in range(1000):
            print(flow.id, end=" > ")
            result = flow.send(part)
            if result == "A":
                print(result)
                total += sum(part.cats.values())
                break
            elif result == "R":
                print(result)
                break
            else:
                flow = flows[result]
        else:
            print("over loop")
            exit(0)
print(total)