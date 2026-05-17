'''Check laptop purchase recommendation
Hint:
Ask the user to enter:
budget
RAM
storage
Use:
AND operator
IF
ELIF
ELSE
Compare:
budget > 100000
ram >= 16
storage >= 512
If all conditions satisfy:
Print "Gaming Laptop"
Else if medium conditions satisfy:
Print "Office Laptop"
Else:
Print "Basic Laptop"'''

bud=int(input("enter your budget : "))
ram=int(input("enter how much RAM storage do you need : "))
stor=int(input("enter how much storage do you need : "))
if(bud>100000 and ram>=16 and stor>=512):
    print("Gaming laptop")
elif(bud>50000 and ram>=8 and stor>=256):
    print("office laptop")
else:
    print("basic laptop")