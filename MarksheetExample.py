p = int(input("enter physics marks"))
c = int(input("enter chemistry marks"))
m = int(input("enter maths marks"))
e= int(input("enter english marks"))
h = int(input("enter hindi marks"))

if (p>=0 and p<=100) and (c>=0 and c<=100) and (m>=0 and m<=100) and (e>=0 and e<=100) and (h>=0 and h<=100):
    per=(p+c+m+e+h)/5
    if per>=33 and per<45:
        print("Pass With Third Division")
    elif per<60:
        print("Pass With Second Division")
    else:
        print("Pass With First Division")
     
else:
    print("all subejct marks should be 0 to 100")
