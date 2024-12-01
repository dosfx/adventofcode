from io import TextIOWrapper
from typing import List

class Segment:
    def __init__(self, dest: int, src: int, length: int):
        self.dest = dest
        self.src = src
        self.length = length

    def contains(self, check: int) -> bool:
        return self.src <= check and check < self.src + self.length

    def contains_dest(self, check: int) -> bool:
        return self.dest <= check and check < self.dest + self.length


class SegMap:
    def __init__(self):
        self.segments = []

    def map(self, src: int):
        for seg in self.segments:
            if seg.contains(src):
                return src - seg.src + seg.dest
        return src

    def reverse(self, dest: int):
        for seg in self.segments:
            if seg.contains_dest(dest):
                return dest - seg.dest + seg.src
        return dest


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



def check(start: int, step: int) -> int:
    closest = start
    while True:
        seed = seed_to_soil.reverse(soil_to_fert.reverse(fert_to_water.reverse(water_to_light.reverse(light_to_temp.reverse(temp_to_humidity.reverse(humidity_to_location.reverse(closest)))))))
        for i in range(0, len(seeds), 2):
            if seeds[i] <= seed and seed < (seeds[i] + seeds[i + 1]):
                return closest
        closest += step

closest = 0
for i in range(6, 0, -1):
    step = pow(10, i)
    closest = check(closest, step)
    print(closest)
    closest -= step

print(check(closest, 1))

