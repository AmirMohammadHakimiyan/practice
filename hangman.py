import random

wordbank=["fish","dog","math","robbit","scissor","rock","bird","human","weak","three","nine","wolf","line","bear","king"]
x= random.randint(0, len(wordbank)-1)
word=wordbank[x]
goodchar=[]
finish=0
badchar=[]
usermistake=0
l=len(word)
while usermistake < 6:
    c=0
    for i in range(len(word)):
        if word[i] in goodchar:
            print(word[i],end=" ")
        else:
            print("-",end=" ")
            c+=1
    if c==0:
        usermistake=10
        print(word)
    else:
        userchar=input("please write your gusses:")
        if len(userchar) == 1:
            if userchar in word:
                goodchar.append(userchar)
                print("yes")
            else:
                print("no")
                usermistake+=1
                badchar.append(userchar)
        else:
            print("please just write one number!!!")
if usermistake == 6:
    print("game over")
else:
    print("you win")


