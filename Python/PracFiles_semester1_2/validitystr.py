import re
def check_string(input_string):
    pattern = r'^[a-zA-Z0-9]+$'
    match = re.match(pattern, input_string)
    if match:
        print("The string contains only a-z, A-Z, 0-9.")
    else:
        print("The string contains other characters.")
check_string("Hello123")
check_string("Hello!123")
check_string("1234567890")
check_string("abcXYZ")
check_string("abcXYZ@")

