laptops=['dell','hp','sony','lenovo','mac']
laptops.append('microsoft')
print(laptops)
laptops.insert(2,'microsoft')
print(laptops)
laptops.extend('microsoft')
print(laptops)
laptops.pop(1)
print(laptops)
laptops.remove('dell')
print(laptops)
a=[1,2,3,4,5]
a.extend(laptops)
print(a)
a.append('microsoft')
print(a)
count=laptops.count('microsoft')
print(count)

copy_list = laptops.copy()
print('this is orginal list:' ,laptops)
print('this is a copy list:' , copy_list)
copy_list.clear()
print(copy_list)

number=(1,2,6) #tuple
print(number)