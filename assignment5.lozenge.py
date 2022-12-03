while True:
    m=int(input("enter the number:"))
    ma=m%2
    if ma ==0:
        break
m//=2
qq=[]
o=0
for i in range(m):
    o+1
    qq.append("*6"*o)
rr=len(qq)
w=0
for i in qq:
    rr-=1
    w+=1
    print(rr*" ",qq[ :w])
rr=0
w=0
for z in qq:
    rr+=1
    w+=1
    print(rr*" ",qq[w:])



