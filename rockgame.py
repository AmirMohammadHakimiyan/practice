print("                     wellcome")
import time
import random
time.sleep(4)
amtiaz=0
amtiaz2=0
x="trtr"
while True :
    if x=="no":
        break
    user=input("chicee the r,p or s:")
    computer=random.randint(1,3)
    if x=="no":
         break
    elif user=="r":
        user=1
        if user==computer:
            amtiaz=amtiaz+1
            amtiaz2=amtiaz2+1
            print("rock")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==1 and computer==2:
            amtiaz2=amtiaz2+1
            print("paper")
            print("'harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==1 and computer==3:
            amtiaz=amtiaz+1
            print("scissor")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==2 and computer==1:
            amtiaz=amtiaz+1
            print("paper")
            print("farif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==2 and computer==3:
            amtiaz2=amtiaz2+1
            print("scissor")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==3 and computer==1:
            amtiaz2=amtiaz2+1
            print("rock")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==3 and computer==2:
            amtiaz=amtiaz+1
            print("paper")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif x=="no":
            break
    elif user=="p":
        user=2
        if user==computer:
            amtiaz=amtiaz+1
            amtiaz2=amtiaz2+1
            print("paper")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==1 and computer==2:
            amtiaz2=amtiaz2+1
            print("paper")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==1 and computer==3:
            amtiaz=amtiaz+1
            print("scissor")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==2 and computer==1:
            amtiaz=amtiaz+1
            print("rock")
            print(" harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==2 and computer==3:
            amtiaz2=amtiaz2+1
            print("scissor")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==3 and computer==1:
            amtiaz2=amtiaz2+1
            print("rock")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==3 and computer==2:
            amtiaz=amtiaz+1
            print("paper")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif x=="no":
            break
    elif user=="s":
        user=3
        if user==computer:
            amtiaz=amtiaz+1
            amtiaz2=amtiaz2+1
            print("scissor")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==1 and computer==2:
            amtiaz2=amtiaz2+1
            print("paper")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==1 and computer==3:
            amtiaz=amtiaz+1
            print("scissor")
            print("",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==2 and computer==1:
            amtiaz=amtiaz+1
            print("rock")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==2 and computer==3:
            amtiaz2=amtiaz2+1
            print("scissor")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==3 and computer==1:
            amtiaz2=amtiaz2+1
            print("rock")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif user==3 and computer==2:
            amtiaz=amtiaz+1
            print("paper")
            print("harif=",amtiaz2,"you=",amtiaz)
            x=input("againe?")
        elif x=="no":
            break
    else :
       print("!!!YOU HAVE WRONGE!!!")
print("goooodbye")

