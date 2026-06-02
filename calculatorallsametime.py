
'''print("Simple calculator\n")
print("enter value a and b\n ")
a=int(input())
b=int(input())
print("\n")
print("addition = ",a+b)
print("\n substraction = ",a-b)
print("\n multiplication = ",a*b)
print("\n division = " ,a/b)'''

print("simple calculator \n")
print(" choice 1.addition 2.substraction 3.multiplication 4.division\n")
c=int(input("enter choice= "))
print("\n enter numbers a and b : ")
a=int(input())
b=int(input())
if c==1:
    print("addition = ",a+b)
elif c==2:
    print("\n substraction = ",a-b)
elif c==3:
    print("\n multiplication = ",a*b)
elif c==4:
    print("\n division = " ,a/b)
else:
    print("invalid choice\n")