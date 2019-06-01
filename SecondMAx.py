arr =[2,23,34,11,45,67,78,58,98,12,91]
max=arr[0]
smax=arr[0]
tmax=arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        smax=max
        max=arr[i]
    elif smax<arr[i] and max!=arr[i]:
       tmax=smax 
       smax=arr[i]
    elif tmax<arr[i] and smax!=arr[i]:
       tmax=arr[i] 
        
          
    


print("Max Element Is"+str(max))
print("Second Max Element is "+str(smax))
print("Third Max Element is "+str(tmax))
