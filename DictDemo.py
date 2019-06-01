emp= {'empid':1001,'empname':'xyz'}
a = [0]*len(emp)
b = [0]*len(emp)
#print(emp['empname'])
i=len(emp)

for key in emp:
    a[i-1]=key
    b[i-1]=emp[key]
    i=i-1
for i in range(0,len(a)):
    print(a[i]+ str(b[i]))

    
    
    


