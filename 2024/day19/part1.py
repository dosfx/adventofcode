import re


with open("input.txt") as file:
    patterns = map(str.strip, file.readline().split(", "))
    file.readline()
    print(len(re.findall(f"^({'|'.join(patterns)})+$", "".join(file.readlines()), re.MULTILINE)))