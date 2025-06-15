import re

regex = r'^The'
strings = ['The grass is always greener on the other side', 'The clever cat', 'Actions speak louder than words.']

for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'not matched {string}')