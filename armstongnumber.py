n=int(input())
t=n
d=len(str(n))
s=0
while t>0:
    r=t%10
    s+=r**d
    t//=10
print("Yes" if s==n else "No")

