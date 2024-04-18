print("function with return value")
def addition():
    print("am in addition function")
    n1 = int(input("enter num 1:"))
    n2 = int(input("enter num 2:"))
    sum = n1+n2
    return sum
print("progrom for addition of 2 num")
result = addition()
print("addition of 2 integer num:",result)