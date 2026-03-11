import string
def ispangram(sentence, alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset<=set(sentence.lower())
print(ispangram(input("Sentence: ")))