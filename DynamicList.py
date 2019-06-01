size = int(input("enter size of list"))
x = [0]*size
for i in range(0,size):
    x[i] = input("Enter element for "+str(i)+" Index")

for i in range(0,size):
    print(x[i])
