num = int(input("enter number"))
res = ""
i=num
f=1
for i in range(num,0,-1):
    if i>1:
     res = res+str(i)+"*"
    else:
     res=res+str(i)    
    f=f*i
print(res+"="+str(f))    
