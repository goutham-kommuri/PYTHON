a=int(input("enter the value of a ="))
if 10<=a and a<=100:
    print("true num = ",a)
else:
    print("false num = ",a)
#using functions
def numcheck(a):
    if 10<=a and a<=100:
        print("true")
    else:
        print("false")
numcheck(15)
