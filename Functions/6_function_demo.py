print("function with arbitrary argument")
def addition(*num):
    print("am in addition function")
    sum=num[0]+num[1]+num[2]
    return sum
print("program of addition of 3 num")
result1=addition(5,20,10)
print("add of 3 int num:",result1)