print("function with default values")
def addition(a=10,b=20,c=30):
    print("am in addition function")
    n1=a
    n2=b
    n3=c
    sum=n1+n2+n3
    return sum
print("program for addition of 3 num:")
result1=addition(6)
print("add of 3 int num:",result1)
result2=addition(7,8)
print("add of 3 int num id:",result2)