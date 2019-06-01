x = [2,3,4,5,6,7,8,9,11,13,45,1]

size1= len(x)//3    # 2
size2 = len(x)//3  #2
size3=len(x)-(size1+size2) #3
y=[0]*size1
z=[0]*size2
k=[0]*size3
for i in range(0,len(x)):
    if i<size1:
        y[i]=x[i]
        print("first list element is ",y[i])
    elif i<size1+size2:
       z[i-size1]=x[i]
       print("second list element is ",z[i-size1])
    else:
      k[i-(size1+size2)]=x[i]
      print("third list element is ",k[i-(size1+size2)])
