# OOP in python:We deal with real time object and its entities.
# class Room:#blueprint of object
#     l=int(input("enter a length:"))
#     w=int(input("enter a width:"))
#     h=int(input("enter a height:"))
#     def area(self):
#         print("Area of room is:",self.l*self.w)
#     def volume(self):
#         print("volume if room is:",self.l*self.w*self.h)

# area_of_room=Room()
# volume_of_room=Room()
# print(area_of_room.area())
# print(volume_of_room.volume())

class calculator:
     def _intit_(self,num1,num2):
          self.num1=num1
          self.num2=num2

     def add(self,*args):
          total=0
          for n in args:
               total += n
          return total
     def subtract(self,*args):
          total=args[0]
          for n in args[1:]:
               total -= n
          return total
     
     def multiply(self,num1,num2):
          return num1*num2
     def divide(self,num1,num2):
          try:
               return num1/num2
          except ZeroDivisionError:
               print("Error:Division by zero!")

call=calculator()
print(cal.sub(4,6,2,5))




