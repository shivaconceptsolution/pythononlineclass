p= int(input("Enter physics marks "))
c1= int(input("Enter chem marks "))
m= int(input("Enter maths marks "))
e= int(input("Enter eng marks "))
h= int(input("Enter hindi marks "))
if (p>=0 and p<=100) and (c1>=0 and c1<=100) and (m>=0 and m<=100) and (e>=0 and e<=100) and (h>=0 and h<=100):
    c=0
    gm=0
    sub=""
    dist=""
    if p>=75:
       dist+=" PHY "
    if c1>=75:
       dist+=" CHEM"
    if m>=75:
       dist+=" MATHS "
    if e>=75:
       dist+=" ENG"
    if h>=75:
       dist+=" HIN "
    if p<33:
        c=c+1
        gm=p
        sub+="PHY "
    if c1<33:
        c=c+1
        gm=c1
        sub+="CHEM "
    if m<33:
        c=c+1
        gm=m
        sub+="MATHS "
    if e<33:
        c=c+1
        gm=e
        sub+="ENG "
    if h<33:
        c=c+1
        gm=h
        sub+="HIN "
    if c==0 or (c==1 and gm>=28):
        if c==0:
         per=(p+c1+m+e+h)/5
        else:
         per=(p+c1+m+e+h+(33-gm))/5   
        if per>33 and per<45:
            print("Congrats you are pass with third division with "+str(per)+"%")
        elif per<60:
            print("Congrats you are pass with second division with "+str(per)+"%")
        else:
            print("Congrats you are pass with first division with "+str(per)+"%")
        if dist!="":
            print("Distinction subject name is "+dist)
        if c==1:
            print("You are pass by grace and grace subject name is "+sub+" grace mark is "+str(33-gm)) 
    elif c==1:
        print("try again you are suppl in "+sub)
    else:
        print("sorry you are fail in "+sub)
else:
    print("all subject marks should be 0 to 100")
