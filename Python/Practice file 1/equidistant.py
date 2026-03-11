def ser(a,b) :
    d = int ((b-a)/3)
    print("Series = ",a,a+d,a+2*d,b)

first = int(input("Enter first Term = "))
last = int(input("Enter last Term = "))

ser(first , last )