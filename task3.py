x=int(input("enter your number:"))
if (x%3==0 and x%5==0):
    print("fizzbuzz")
elif(x%5):
    print("fizz")
elif(x%3):
    print("buzz")
else:
    print(x)
