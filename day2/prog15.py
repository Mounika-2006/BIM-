door_status=input("enter your door status : ")
cam_status=input("enter your camera status : ")
alm_status=input("enter your alram status : ")
if door_status=="YES" and cam_status=="YES"  and alm_status=="YES" :
    print("Home secure")
else:
    print("Security Warning")