a="MY country name is Nepal"
print(len(a))
print(a[19:])
print(a.upper())
print(a.lower())
print(a.replace("Nepal","America"))
print(a.split(" "))
b="i am studying in xaiver college"
c=a+b
print(c)
price=43.33
item_no=957
quality=5
myorder="i want to pay {} dollars for {} pieces of item {}"
print(myorder.format(price,quality,item_no))