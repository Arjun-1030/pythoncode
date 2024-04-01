user_id={110,111,112}
print(user_id)
str='adfdgfgdfigedfgfghgdhvjgfd'
new_list=list(str)
new_tuple=tuple(str)
new_set=set(str)
print("list:",new_list)
print("list:",new_tuple)
print("list:",new_set)

a={1,2,3,4,5}
a.add(6)
a.add('nepal')
print(a)
a.remove(5)
print(a)
b=a.copy()
print(b)
b.clear()
print(b)
# difference
A={'a','b','c','d','e'}
B={'f','b','c','d','g'}
print(A.difference(B))
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.issubset(B))

re=a.pop()
print(re)
y={'a','b','c','d'}
rel=y.pop()
print(rel)
print(A.symmetric_difference(B))
print(A.union(B))
