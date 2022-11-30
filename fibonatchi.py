print("                      wellcome")
m=1
while m==1:
    n=1
    b=1
    g=0
    m=1
    chav=int(input("enter the sentences:"))
    for i in range (chav-1):
        if chav>2:
            s=n
            n=n+g
            g=s

    print(n)
    choon=(input("again?"))
    if choon=="no":
        m=3
print("thankyou")