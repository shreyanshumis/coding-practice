hrs = float(input("Enter Hours:")) #prompts the user for hrs
rate = float (input("Enter the rate per hour: ")) #'' but rate

def computepay(h, r):
    if hrs <= 40.0:
        p = hrs*rate
    elif hrs > 40.0:
        p = (40*rate)+((hrs-40)*(rate*1.5))
    else:
        print("Invalid input")
    return p

p = computepay(10, 20)
print("Pay", p)