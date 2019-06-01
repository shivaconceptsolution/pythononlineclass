x=[1,2,4,5,6,7,7,8,9,1,1,1,2]
y=()*len(x) #y is tuple
y=x   #list to tuple    y point to x
s="("
i=0
for y1 in y:
   if i<len(y)-1: 
    s+=str(y1)+","
   else:
    s+=str(y1)
   i=i+1  
s+=")"
print(s)
   
