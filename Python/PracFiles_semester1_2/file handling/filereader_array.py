import numpy as np

def line_rdrr(file_path):
    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    lines_array = np.array(lines)
    return lines_array

file_path = "testresume.txt" 
lines_ndarray = line_rdrr(file_path)
print(lines_ndarray)
