month = { "jan":31,"feb":28,"march":31,"april":30,"may":31,"june":30,"july":31,"aug":31,"sept":30,"oct":31,"nov":30,"dec":31}
mon = input("enter the mounth name in short form = ")
print("number of days in ",mon,"=",month [ mon ])
lst = list ( month . keys() )
lst.sort()
print( lst )
print( "month which have 31 days --- ")
for i in month :
    if month [ i ] == 31 :
        print( i )
print("month according to number of days ---")
print("feb")
for i in month :
    if month [ i ] == 30 :
        print(i)
for i in month :
    if month [ i ] == 31 :
        print( i )