temp=int(input("enter the temperature"))
lower=int(input("enter the lower limit value"))
upper=int(input("enter the upper limit value"))
if (temp > lower) and (temp < upper):
    print("safe")
else:
    print("danger")