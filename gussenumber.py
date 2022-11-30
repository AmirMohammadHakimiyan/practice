import random
import time
x=0
print("                    wellcome")
time.sleep(3)
print("you can choce 7 time")
choce2= random.randint(1, 50)
n=1
while n==1:
    for i in range(1):
        if n==2:
            break
        if x==8:
           print("you loooooose")
           break
        else:
            choce=int(input("please choce the numer of 1 to 50="))
            if choce==choce2:
                print("                       victory")
                print("you can win after", x+1)
                again=input("Do you want play again? y or n")
                if again=="y":
                    choce2= random.randint(1, 50)
                elif again=="n":
                    print("                     good by")
                    n=n+1
            elif choce>choce2:
                print("go down")
                x=x+1
            elif choce<choce2:
                print("go up")
                x=x+1
            elif x==8:
                n=n+1
                print("you loooooose")
                break
