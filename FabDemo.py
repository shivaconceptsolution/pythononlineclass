a=-1
b=1
t = int(input("enter number of terms"))
i=1
for i in range(1,t+1):
    c=a+b
    j=2
    flag=True
    for j in range(2,c//2+1):
      if c%j==0:
        flag=False
        break
      j=j+1
    if flag and c>1:
     print(c,end=' ')
    a=b
    b=c
    i=i+1




    
