def function():
    a=[1,2,3,4]
    b=[1,3,5,6]
    c=a
    print(c is a)
    print(c is not b)
    print(any(x in a for x in b))
    print(any(x not in a for x in b))
function()
