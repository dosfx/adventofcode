from io import TextIOWrapper
from typing import Dict, List

class Segment:
    def __init__(self, dest: int, src: int, length: int):
        self.dest = dest
        self.src = src
        self.length = length

    def contains(self, check: int) -> bool:
        return self.src <= check and check < self.src + self.length


class SegMap:
    def __init__(self):
        self.segments = []

    def map(self, input: int):
        for seg in self.segments:
            if seg.contains(input):
                return input - seg.src + seg.dest
        return input


def ints(line: str) -> List[int]:
    return [int(n) for n in line.split()]


def read_map(file: TextIOWrapper) -> SegMap:
    ret = SegMap()
    while len(line := file.readline().strip()) > 0:
        ret.segments.append(Segment(*ints(line)))
    return ret


with open("input.txt") as file:
    seeds = ints(file.readline()[7:])
    file.readline()
    file.readline()
    seed_to_soil = read_map(file)
    file.readline()
    soil_to_fert = read_map(file)
    file.readline()
    fert_to_water = read_map(file)
    file.readline()
    water_to_light = read_map(file)
    file.readline()
    light_to_temp = read_map(file)
    file.readline()
    temp_to_humidity = read_map(file)
    file.readline()
    humidity_to_location = read_map(file)

closest = 10000000000
for seed in seeds:
    closest = min(closest, humidity_to_location.map(temp_to_humidity.map(light_to_temp.map(water_to_light.map(fert_to_water.map(soil_to_fert.map(seed_to_soil.map(seed))))))))
print(closest)