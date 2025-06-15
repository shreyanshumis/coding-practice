import re
def match_string(input_string):
    pattern = r'n[b]+'
    match = re.search(pattern, input_string)
    if match:
        print("String matches the pattern.")
    else:
        print("String does not match the pattern.")
match_string("nbb")
match_string("nnbbb")
match_string("n")
match_string("nbbb")
match_string("nbbbbz")
