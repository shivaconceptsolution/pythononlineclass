def fun1():
    print("This is Default Function Without Return Type")

def fun2():
    return "Default With Return TYpe"

def fun3(arg):
    print(arg)

def fun4(arg):
    return arg


fun1()
print(fun2())
fun3("Param without Return Type")
print(fun4("Param With Return Type"))
