def conversion01(n):
    strnum = str(n)
    decinum = int (strnum,8)
    print("Numbers in Decimal = ", decinum)
    print("Numbers in Binary = ", bin(decinum))
    print("Numbers in Hexadecimal = ", hex (decinum))
num = int(input("Enter an octal number:"))
conversion01(num)