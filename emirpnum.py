s=input()
s=s[::-1]
n=int(s)
f=False
print(n)
for i in range(2,n):
    if n==1:
        f=True
        break;
    else:
        if n%i==0:
            f=False
            break;
        else:
            f=True
print("prime" if(f) else "not prime")