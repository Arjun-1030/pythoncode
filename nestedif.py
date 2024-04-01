user=input("enter your name:")
if user=="admin":
    print("You are successfully login in admin dashboard")
    attendence=input("enter attendence:")
    if attendence=="full":
        print("staff attendence is full")
    elif attendence=="half":
        print("staff attendence is half")
    elif attendence=="morning":
        print("staff attendence is morning")
    else:
        print("staff is absent")
else:
    print("You are not admin")