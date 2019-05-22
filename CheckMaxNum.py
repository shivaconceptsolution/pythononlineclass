a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
if a>b:
    if a>c:
        if a>d:
            print("a is max")
        else:
            print("d is max")
    else:
        if c>d:
            print("c is max")
        else:
            print("d is max")
            
else:
    if b>c:
        if b>d:
            print("b is max")
        else:
            print("d is max")
    else:
        if c>d:
            print("c is max")
        else:
            print("d is max")
       
        
    
