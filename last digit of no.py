# a=int(input("enter the last number"))
# if a>0:
#     r=a%10
#     print("last digit",r)
# else:
#     print("not a last digit")


a=int(input("enter the number"))
b=int(input("enter the last digit on a"))
if a>0:
    r=a%10
    print("last digit",r)
elif b%3:
    print("divisible by 3")
else:
    print("not divisible by 3")