import re

s = 'Hello class BCA'

match = re.search('BCA', s)

print(match)

print('Starting Index: ', match.start())
print('Ending Index: ', match.end())