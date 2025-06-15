import re

s = 'shrey.anshumishra'

#without using \
match = re.search(r'.',s)
print(match)

#using \
match = re.search(r'\.',s)
print(match)

