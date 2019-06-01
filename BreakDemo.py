for i in range(1,12):
    if i==3 or (i==5 and i!=7):
        continue
    if i==3:
        break
    print(i)

