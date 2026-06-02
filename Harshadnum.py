s=int(input())
c=0
n=s
while(n>0):
    c=c+(n%10)
    n=n//10
print("Harshad num " if (s%c==0) else "not harshad")