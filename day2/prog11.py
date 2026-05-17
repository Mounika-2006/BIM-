id_card=input("enter your id card status : ")
finger=input("enter your finger print status : ")
access_level=int(input("enter your access level : "))
if id_card=="yes" and finger=="yes" and access_level>5:
    print("Access granted")
else:
    print("Access denied")