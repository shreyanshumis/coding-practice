def retser (init,step):
    return init, init+step, init+2*step, init+3*step
ini = int(input("Enter initial value of the AP series : "))
ste = int(input("Enter step value of the AP series : "))
t1,t2,t3,t4=retser(ini,ste)
print(t1,t2,t3,t4)