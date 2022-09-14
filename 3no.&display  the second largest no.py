a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b and a>c:
    if b>c:
        print("2nd largest number b")
    else:
        print("2nd largest number c")
elif b>c and b>a:
    if b>c:
        print("2nd largest number c")
    else:
        print("2nd largest number a")
elif a>b:
    print("2nd largest number a")
else:
    print("2nd largest number b")