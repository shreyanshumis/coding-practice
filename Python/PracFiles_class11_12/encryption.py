def encrypt(sttr,enkey):
    return enkey.join(sttr)
def decrypt(sttr,enkey):
    return sttr.split(enkey)

mstr = input("Enter The Main String:")
estr = input("Enter the Encryption key:")
enstr = encrypt(mstr,estr)
destr = "".join(mstr)
print("Encrypted string = ", enstr)
print("Decrypted string = ", destr)