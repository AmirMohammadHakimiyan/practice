a=input("number=")
b=list(a)
n=0
for i in range(0,int(len(b)/2),1):
    if b[i]==b[-(i+1)]:
        n+=1
if n==int(len(b)/2):
    print("gharine")