ch = input("enter char")

if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
    print("Alphabet")
elif ch>='0' and ch<='9':
    print("Numeric")
else:
    print("Special")
