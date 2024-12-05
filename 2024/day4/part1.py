import re

with open("input.txt") as file:
    search = "".join(file.readlines())
total = 0
total += len(re.findall(r"XMAS", search))
total += len(re.findall(r"SAMX", search))
linelen = search.find("\n")
fill = "." * linelen
total += len(re.findall(f"(?=X{fill}M{fill}A{fill}S)", search, re.RegexFlag.DOTALL))
total += len(re.findall(f"(?=S{fill}A{fill}M{fill}X)", search, re.RegexFlag.DOTALL))
fill = "." * (linelen - 1)
total += len(re.findall(f"(?=X{fill}M{fill}A{fill}S)", search, re.RegexFlag.DOTALL))
total += len(re.findall(f"(?=S{fill}A{fill}M{fill}X)", search, re.RegexFlag.DOTALL))
fill = "." * (linelen + 1)
total += len(re.findall(f"(?=X{fill}M{fill}A{fill}S)", search, re.RegexFlag.DOTALL))
total += len(re.findall(f"(?=S{fill}A{fill}M{fill}X)", search, re.RegexFlag.DOTALL))
print(total)