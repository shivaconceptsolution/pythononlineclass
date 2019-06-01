x = [2,3,4,5,6,7,8,2,2,3]

for i in range(0,len(x)):
      flag=True
      for j in range(i+1,len(x)):
        if x[i]==x[j]:
            flag=False
            break

      for k in range(i-1,-1,-1):
            if x[i]==x[k]:
               flag=False
               break

      if flag:
          print(x[i])
