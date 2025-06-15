def remove_newlines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    lines = [line.rstrip('\n') for line in lines]

    with open(output_file, 'w') as file:
        file.write('\n'.join(lines))

input_file = "testresume.txt"
output_file = "output.txt"

remove_newlines(input_file, output_file)
