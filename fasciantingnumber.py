n=int(input())
s=str(n)+str(n*2)+str(n*3)
print("Yes" if len(s)==9 and sorted(s)==list("123456789") else "No")