def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

data = swap(int(input("enter first number")),int(input("enter second number")))
print(data[0],data[1])
