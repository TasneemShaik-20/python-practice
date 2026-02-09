a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
d=int(input("enter the number: "))

if(a>b and a>c and a>d):
    print("the greatest number is ",a)
elif(b>c and b>a and b>d):
    print("the greatest number is ",b)
elif(c>a and c>b and c>d):
    print("the greatest number is ",c)
else:
    print("the greatest number is ",d)


