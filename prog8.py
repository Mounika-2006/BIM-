age=int(input("enter your age"))
license_availability=input("did you license")
if(age>=19) and (license_availability=="yes"):
    print("you are eligible for the driving")
else:
    print("you are not eligible for the driving")