# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=int(input("enter the number: "))
# d=int(input("enter the number: "))

# if(a>b and a>c and a>d):
#     print("the greatest number is ",a)
# elif(b>c and b>a and b>d):
#     print("the greatest number is ",b)
# elif(c>a and c>b and c>d):
#     print("the greatest number is ",c)
# else:
#     print("the greatest number is ",d)

# question 2

sub_1=int(input("enter the marks: "))
sub_1_percetage=(sub_1/100)*100
sub_2=int(input("enter the marks: "))
sub_2_percetage=(sub_2/100)*100
sub_3=int(input("enter the marks: "))
sub_3_percetage=(sub_3/100)*100

total_marks=sub_1+sub_2+sub_3

percetage=(total_marks/300)*100
print( "percentage ",percetage)

if(percetage>40 and sub_1_percetage>33 and sub_2_percetage>33 and sub_3_percetage>33):
    print("Result is : PASS")
else:
    print("result is : FAIL")
