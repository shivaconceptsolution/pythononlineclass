num = int(input("enter number to revese "))   #467
a = num%10  #7
num = num//10  #46
b = num%10   #6
c = num//10   #4
res = a*100+b*10+c*1
print("After reverse result is ",res)
