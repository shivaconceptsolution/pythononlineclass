a= r'c:\\hello'
print(a)
b= r"c:\\hello hi "
print(b)
c= """ hello
                     how  r u

       welcome"""


print(c)   #complete String

print(a[0],a[1],a[2],a[3])  #print particular char

print("USING FOR LOOP")
for i in range(0,len(a)):    
    print(a[i])

print("USING FOR EACH LOOP")
for j in a:
    print(j)
    
