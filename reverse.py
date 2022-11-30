p=0
n=[]
print('if you want to countine write the "y"')
while p==0 :
    x=input(" write:")
    n.append(x)
    y=input("again?")
    if y=="y":
        print("OK")
    else :
        break
kam=0
aghar=[]
for i in range(len(n)) :
    kam+=1
    aghar.append(n[len(n)-kam])
print(aghar)
