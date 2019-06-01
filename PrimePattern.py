c=0
for i in range(2,30):
    flag=True
    
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag==True:
       print(i,end=' ')
       c=c+1
       if c==1 or c==3 or c==6:
           print()
       
