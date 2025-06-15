def add_ed(verb):
    if len(verb) < 3:
        return "Verb should be at least 3 characters long."
    
    if verb[-2:] == 'ed':
        return verb
    
    return verb + 'ed'

# Example usage
given_verb = input("Enter a verb: ")
result = add_ed(given_verb)
print("Result:", result)

