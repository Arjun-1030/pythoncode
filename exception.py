#exception->an event that occurs to disrupt the normal flow of operation.
# try:
#     age=int(input())
#     print(age)
# except:
#     print("please provide numberic value")

# print('xavier college') 
# try:
#     a=int(input("enter a value:"))
#     b=int(input("enter a value:"))
#     c=a/b
# except ValueError: 
#     print("please provide numberic values")
# except ZeroDivisionError:
#     print("zero will not divide any other number")
# else:
#     print("the value of c is:",c)
def login(): 
    user1="admin"  
    pass1="admin"
    try:
        username=input()
        password=input()
        if user1 !=username:
            raise ZeroDivisionError
        elif pass1!=password:
            raise ValueError
    
    except ZeroDivisionError:
        print("username is invalid")
        login()
    except ValueError:
        print("password is invalid")
        login()
    else:
        print("login successful")
    finally:
        print("home")
login()