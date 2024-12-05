import re

with open("input.txt") as file:
    search = "".join(file.readlines())
total = 0
linelen = search.find("\n")
fill = "." * (linelen - 1)
total += len(re.findall(f"(?=M.S{fill}A{fill}M.S)", search, re.RegexFlag.DOTALL))
total += len(re.findall(f"(?=M.M{fill}A{fill}S.S)", search, re.RegexFlag.DOTALL))
total += len(re.findall(f"(?=S.S{fill}A{fill}M.M)", search, re.RegexFlag.DOTALL))
total += len(re.findall(f"(?=S.M{fill}A{fill}S.M)", search, re.RegexFlag.DOTALL))
print(total)