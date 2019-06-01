for i in range(1,6):
    asc=65
    for j in range(1,7-i):
        if j%2==0:
            print(chr(asc+32),end=" ")
            asc=asc+1
        else:
           print(chr(asc),end=" ")
    print()        
