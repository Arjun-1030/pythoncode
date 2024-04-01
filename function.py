#function is a block of code.we used function to reuse the code.two type of function
# 1.built-in function.
# 2.user-defined function

#def function_name():
#    function body 
#function_name()

#simple program in user defined function
#def function_code():
   # print("hello world")
#function_code()

# positional arguments-takes value according to proper positional order.
# def hello(name,course_name):#parameter
#     print("hello",name,"welcome to web development training")
#     print(course_name)
#     hello('Ram','Python with django')#arguments
    
# keywords arguments-takes values according to keyword.
# hello(name='Ram',course_name='Python with django')#arguments

# default arguments-
# def hello(name,course_name='python with django'):#parameter
#     print("hello",name,"welcome to web development training")
#     print(course_name)
#     hello(name='saurav')

# arbitary arguments- denoted by "*"
# def sum(*args):#multiple values assign 
#     total=0
#     for n in args:
#         total+=n
#     return total#return gives result of the function and stop the execution of function
# result =sum(2,3,5)
# print(result)

# def hello(**kwargs):#parameter
#     print("hello",kwargs['name'],"welcome to web development training")
#     print(kwargs['course_name'])
# hello(name='ram',course_name='python with data science',another_course='python with data science')

#scope of variable
#global variable->which can accessible from any place.
l=float(input("enter a length:"))
b=float(input("enter a breadth:" ))
def area():
    #local variable->that is defined inside the function and cannot be accessible from outside the function.its scope is only around the declared function
    area_of_object=l*b                               # adjust= alt+z
    return area_of_object                            #comment=ctrl+/
def volume():
    h=float(input("enter a height:"))
    v=l*b*h
    return v
result_volume=volume()
result=area()
print(result)
print(result_volume)

#lambda function:the function without name.it is used for instant use and its one-time uses.lambda keyword is used.
# x=lambda a, b:a * b
# area=x(2,3)
# print(area)
# #recursive function- function calling itself again and again.
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# result=factorial(5)
# print(result)


#filter()
#map()