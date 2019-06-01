u = float(input("enter unit price"))
t = float(input("enter total consumption"))
s = float(input("enter security amount"))
p = float(input("enter late fee"))
due=float(input("enter previous bill"))
CAP= 250
nbill= u*t
if t>CAP:
    bil=(u+u*0.03)*t
else:    
    bil = u*t
l = bil-nbill
print("Total ebill is ",bil+p+due,"\n Load amount is ",l,"\n Security Amount is ",s)
