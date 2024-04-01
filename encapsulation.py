#data hiding using encapsulation
class Employee:
    def __init__(self,name,project,salary):
        self.name = name #public member(accessible within or outside the class)
        self.project = project #protected member(accessible within the class  and its sub-classes)
        self.__salary = salary #private member(accessible only within a class)
    def show(self):
        print("name:",self.name)
emp = Employee('mahadev','xavier',1000)
emp.show()
print(emp.name)
print(emp.project)
print(emp._Employee__salary)