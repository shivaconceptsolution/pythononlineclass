def greatest(a,b,c):
  
  if a>b and a>c:
        print("a is greatest")
  elif b>c:
        print("b is greatest")
  else:
        print("c is greatest")

a= int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
greatest(a,b,c)        
        
