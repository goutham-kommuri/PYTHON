import copy
a=[1,2,3]
c=a
b=copy.copy(a)
print(id(c) == id(a))
print(b is a)
