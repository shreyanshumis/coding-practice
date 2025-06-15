def sort_tuples_by_last_element(tuples):
    sorted_tuples = sorted(tuples, key=lambda x: x[-1])
    return sorted_tuples

# Example usage
tuples = [(12, 15), (11, 12), (14, 14), (12, 13), (12, 11)]
sorted_tuples = sort_tuples_by_last_element(tuples)
print("Sorted tuples:", sorted_tuples)
