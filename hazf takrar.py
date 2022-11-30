dec=[]
while True :
    x=input("enter the word:")
    dec.append(x)
    s=input("again?")
    if s!="y":
        break
new=[]
for c in dec :
    if c not in new :
        new.append(c)

print(new)
    