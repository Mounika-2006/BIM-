mat=int(input("enter your maths marks"))
sci=int(input("enter your science marks"))
eng=int(input("enter your english marks"))
if(mat>=75 and sci>=75 and eng>=75):
    print("distinction")
elif(mat>=35 and sci>=35 and eng>=35):
    print("pass")
else:
    print
    ("fail")