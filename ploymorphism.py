class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print('details:',self.name,self.color,self.price)

    def max_speed(self):
        print("vehicle max speed is 150")
    
    def change_gear(self):
        print('vehicle change gear 6')


class Car(Vehicle):
    def max_speed(self):
        print('car max speed is 240')
    
    def change_gear(self):
        print('car change gear 6')


car = Car('car x1' , 'red', 20000)
car.show()
car.max_speed()
car.change_gear()