#  Check sports team selection
speed=int(input("enter your speed : "))
fitness=int(input("enter your fitness score : "))
dis=int(input("enter your discipline score"))
if(speed>80 and fitness>80 and dis>80):
    print("selected")
elif(speed>=50 and fitness>=50 and dis>=50):
    print("waiting List")
else:
    print("rejected")