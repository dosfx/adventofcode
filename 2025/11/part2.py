import functools


with open("input.txt") as f:
    nodes: dict[str, list[str]] = {}
    for line in f.readlines():
        split = line.split(":")
        nodes[split[0]] = split[1].split()


inv_nodes: dict[str, list[str]] = {}
for node, children in nodes.items():
    for child in children:
        inv_nodes.setdefault(child, []).append(node)


@functools.cache
def paths(target: str, start: str) -> list[tuple[str, ...]]:
    if target == start:
        return [(start,)]
    if target == "svr":
        return []
    ret = []
    for source in inv_nodes[target]:
        for path in paths(source, start):
            ret.append(path + (target,))
    return ret


svr_fft = len(paths("fft", "svr"))
fft_dac = len(paths("dac", "fft"))
dac_out = len(paths("out", "dac"))
print(svr_fft * fft_dac * dac_out)
