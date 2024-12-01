from dataclasses import dataclass
from queue import Queue
import re
from typing import Dict, List, Optional, Tuple

re_mod = re.compile(r"([%&]?)([a-z]+) -> ([a-z ,]+)")

class Module:
    def __init__(self, name: str, outputs: Tuple[str]):
        self.name = name
        self.outputs: Tuple[str] = outputs

    def input_signal(self, input: bool, src: str) -> Optional[bool]:
        return input

    def __repr__(self) -> str:
        return f"{self.name} -> {', '.join(self.outputs)}"

    @staticmethod
    def parse(line: str) -> "Module":
        match = re.match(re_mod, line)
        name = match.group(2)
        outputs = tuple([o.strip() for o in match.group(3).split(",")])
        if match.group(1) == "%":
            return FlipFlop(name, outputs)
        if match.group(1) == "&":
            return Conjunction(name, outputs)
        return Module(name, outputs)

class FlipFlop(Module):
    def __init__(self, name: str, outputs: Tuple[str]):
        super().__init__(name, outputs)
        self.mem: bool = False

    def __repr__(self) -> str:
        return "%" + super().__repr__()

    def input_signal(self, input: bool, src: str) -> Optional[bool]:
        if not input:
            self.mem = not self.mem
            return self.mem
        return None

class Conjunction(Module):
    def __init__(self, name: str, outputs: Tuple[str]):
        super().__init__(name, outputs)
        self.memory: Optional[Dict[str, bool]] = None

    def __repr__(self) -> str:
        return "&" + super().__repr__()

    def input_signal(self, input: bool, src: str) -> Optional[bool]:
        self.memory[src] = input
        return not all(self.memory.values())

    def set_inputs(self, inputs: List[str]) -> None:
        self.memory = {}
        for con in inputs:
            self.memory[con] = False

@dataclass
class Signal:
    source: str
    value: bool
    target: str

    def __repr__(self) -> str:
        return f"{self.source} -{'high' if self.value else 'low'}-> {self.target}"

with open("input.txt") as file:
    modules: Dict[str, Module] = {}
    for line in file.readlines():
        module = Module.parse(line)
        modules[module.name] = module

for mod in modules.values():
    if isinstance(mod, Conjunction):
        mod.set_inputs([in_mod.name for in_mod in modules.values() if mod.name in in_mod.outputs])

low_total = high_total = 0
for _ in range(1000):
    low = high = 0
    queue: Queue[Signal] = Queue()
    queue.put(Signal("button", False, "broadcaster"))
    while not queue.empty():
        signal = queue.get()
        if signal.value:
            high += 1
        else:
            low += 1
        if not signal.target in modules:
            continue
        mod = modules[signal.target]
        result = mod.input_signal(signal.value, signal.source)
        if result is not None:
            for out in mod.outputs:
                queue.put(Signal(mod.name, result, out))
    low_total += low
    high_total += high

print(low_total * high_total)