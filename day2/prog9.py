purchase=int(input("enter the amount : "))
cupon=input("enter the cupon if available : ")
membership=input("enter the membership if you have : ")
if(purchase>10000 and cupon=="yes" and membership=="yes"):
    print("maximum discount")
elif(purchase>5000 and cupon=="yes" and membership=="yes"):
    print("medium dicount")
else:
    print("no discount")