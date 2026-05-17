rooms=int(input("enter the number of days"))
days=int(input("enter the number of days"))
budget=int(input("enter the budget"))
if(rooms>=2 and days>=3 and budget>50000):
    print("luxary booking")
elif(rooms>=1 and days>=1 and budget>=25000):
    print("standard booking")
else:
    print("budget bookin")