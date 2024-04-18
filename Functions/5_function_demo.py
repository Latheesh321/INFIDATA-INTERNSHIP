print("function with keyword argument")
def addition(a,b,c):
    print("am in addition function")
    n1=a
    n2=b
    n3=c
    sum=n1+n2+n3
    return sum
print("program for addition of 3 num")
result1=addition(b=5,c=10,a=2)
print("add of 3 int num:",result1)
result2=addition(a=3,c=100,b=50)
print("add of 3 int num id:",result2)