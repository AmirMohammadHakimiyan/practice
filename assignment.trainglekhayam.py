def pas(m):
    l=[]
    for i in range(m):
        l.append([1]*(i+1))
    for i in range(2,m):
        for z in range(i-1):
            l[i][z]=l[i-1][z-1]+l[i-1][z]
    return l
c=int(input("enter the number:"))
x=pas(c)
for i in x:
    print(i)
