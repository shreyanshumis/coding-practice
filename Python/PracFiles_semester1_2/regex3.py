import re

string = "Where there's a will, there's a way"
pattern = "[a-m]"
result = re.findall(pattern, string)

print(result)