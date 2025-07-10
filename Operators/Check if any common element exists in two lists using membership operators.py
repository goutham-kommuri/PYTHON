a=[1,2,3,4,5]
b=[5,6,7,8,9]
print(any(x in b for x in a ))
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            print("true")
        else:
            print("false")
