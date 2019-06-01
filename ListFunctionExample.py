def sum(arr):
    s=0
    for a in arr:
        s=s+a
    print("Result is "+str(s))


size = int(input("enter size"))
data = [int]*size
for i in range(0,size):
    data[i]=int(input("enter element"))
sum(data)    
