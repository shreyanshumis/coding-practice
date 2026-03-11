print("Enter a word to check if it is palindrome or not \n It should either be in upper case in it's entirity or in lower case")
st=input()
st2=st[::-1]
if(st==st2):
    print('It is a palindrome')
else:
    print('It is not a Palindrome')
