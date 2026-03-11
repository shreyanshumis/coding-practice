h = float(input("Enter Hours:"))
rate = float(input("Enter rate(per hour):"))
if h <= 40.0:
    grosspay = h*rate
elif h > 40.0:
    z = h - 40.0
    grosspay = (40.0*rate)+(z*(rate*1.5))
else:
	print("wrong input")
print(grosspay)