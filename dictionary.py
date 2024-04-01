student = {
    'name':"ram",
    'age':20,
    'adress':'besigaun'
}
print(student)

capital={
    "nepal":"kathmandu",
    "india":"new delhi",
    "china":"beijing"
}
print(capital)
print(len(capital))
print(type(capital))

print(capital.keys())  #gives list of the keys
print(capital.values()) #gives values of the keys
print(capital['nepal'])#gives values of given keys
capital['japan']="tokyo"#adds the values in dictionary
print(capital)
capital['america']="washington DC"
print(capital)
pop_element=capital.pop('america')
print(pop_element)

marks={
    "science":80,
    "math":80,
    "nepali":80
}
print(marks)
capital.update(marks)#gives the combine values in captial/extends
print(capital)

a={1,2,3,4}
b=(1,2,3,4)
c=['a','b','c','e','f','d']
print(c.index('a'))#gives the index number of given data
c.sort()#ascending order ma sorting
c.sort(reverse=True)
print(c)

copy_captial=capital.copy()
print('this is copy:',copy_captial)
copy_captial.clear()
print(copy_captial)

