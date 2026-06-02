"""1. Username Validation System"""
u=input()
print("Valid Username" if u.isalnum() else "Invalid Username")


"""2. Password Strength Checker"""
p=input()
u=d=False
for i in p:
    if i.isupper():
        u=True
    if i.isdigit():
        d=True
if len(p)>=8 and u and d:
    print("Strong Password")
else:
    print("Weak Password")
    
    
"""3. Email Domain Extractor"""
e=input()
print(e.split("@")[1])


"""4. Log File Analyzer"""
log=input()
print(log.count("ERROR"))


"""5. Chat Message Cleaner"""
msg=input()
print(" ".join(msg.split()))


"""6. Product Code Verification"""
c=input()
print("Valid Product" if c.startswith("PRD") else "Invalid Product")


"""7. Reverse Customer Feedback"""
f=input()
print(f[::-1])


"""8. Word Frequency Counter"""
s=input().split()
d={}
for i in s:
    d[i]=d.get(i,0)+1
for i in d:
    print(i,":",d[i])
    
    
"""9. Secret Message Encryption"""
s=input()
r=""
for i in s:
    r+=chr(ord(i)+1)
print(r)


"""10. Anagram Checker"""
s1=input()
s2=input()
print("Anagram" if sorted(s1)==sorted(s2) else "Not Anagram")