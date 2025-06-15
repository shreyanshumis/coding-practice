def count_words_starting_with_the(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        count = 0
        for word in words:
            # Convert the word to lowercase to make the comparison case-insensitive
            word = word.lower()
            # Check if the word starts with 'the'
            if word.startswith('the'):
                count += 1
        return count

# Call the function with the filename 'ABC.txt'
filename = 'ABC.txt'
count = count_words_starting_with_the(filename)
print(f"Number of words starting with 'the' in '{filename}': {count}")
