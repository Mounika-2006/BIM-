helmet=int(input("enter your helmet status"))
license=int(input("enter your licence status"))
speed=int(input("enter your speed"))
if(helmet=="yes" and license=="yes" and speed<80):
    print("no fine")
elif(helmet=="yes" and license=="yes" and speed>80):
    print("heavy finr")
else:
    print("normal fine")