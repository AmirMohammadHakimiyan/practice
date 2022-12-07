import pyfiglet
import random
def show():
    for  row in game_board:
        for cell in row:
             print(cell,end=" | ")
        print()
title=pyfiglet.figlet_format("    Tic tac toe",font="slant")
print(title)
game_board=[["*","*","*"],
            ["*","*","*"],
            ["*","*","*"]]
show()
win=0
h=0
draw=0
com=[0,1,2]
menu=input("two player?yes or no:")
def check_game():
    win=0
    draw=0
    h=0
    for i in range(3):
        for j in range(3):
            if game_board[i][j]=="x" or game_board[i][j]=="o":
                draw+=1
    if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
        win+=1
        print("player 1 win")
    elif game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
        win+=1
        print("player 1 win")
    elif game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
        win+=1
        print("player 1 win")
    elif game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
        win+=1
        print("player 1 win")
    elif game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
        win+=1
        print("player 1 win")
    elif game_board[0][2]=="x" and game_board[1][2]=="x" and game_board[2][2]=="x":
        win+=1
        print("player 1 win")
    elif game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
        win+=1
        print("player 1 win")
    elif game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
        win+=1
        print("player 1 win")
    elif game_board[0][0]=="o" and game_board[0][1]=="o" and game_board[0][2]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[1][0]=="o" and game_board[1][1]=="o" and game_board[1][2]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[2][0]=="o" and game_board[2][1]=="o" and game_board[2][2]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[0][0]=="o" and game_board[1][0]=="o" and game_board[2][0]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[0][1]=="o" and game_board[1][1]=="o" and game_board[2][1]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[0][2]=="o" and game_board[1][2]=="o" and game_board[2][2]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[0][0]=="o" and game_board[1][1]=="o" and game_board[2][2]=="o":
        win+=1
        print("player 1 lose")
    elif game_board[0][2]=="o" and game_board[1][1]=="o" and game_board[2][0]=="o":
        win+=1
        print("player 1 lose")
    elif draw==9:
        h+=1
        print("you are draw")
while  win==0 and draw!=1:
    while menu=="yes" and win==0 and draw!=1:
        while win==0:
            print("player 1")
            while  win==0 and draw!=1:
                row=int(input("row: "))
                col=int(input("col: "))
                if 0<=row<=2 and 0<=row<=2:
                    if game_board[row][col]=="*":
                        game_board[row][col]="x"
                        break
                    else:   
                        print("you can't")
                else:
                    print("you can't!!!")
            show()
            check_game()
            print("player2")
            while win==0 and draw!=1:
                row=int(input("row: "))
                col=int(input("col"))
                if 0<=row<=2 and 0<=row<=2:
                    if game_board[row][col]=="*":
                        game_board[row][col]="o"
                        break
                    else:
                        print("you can't")
                else:       
                    print("you can't do that!!!")
            show()
            check_game()
    while menu=="no" and win==0 and draw!=1:
        while win==0:
            print("player 1")
            while  win==0:
                row=int(input("row: "))
                col=int(input("col: "))
                if 0<=row<=2 and 0<=row<=2:
                    if game_board[row][col]=="*":
                        game_board[row][col]="x"
                        break
                    else:
                        print("you can't")
                else:
                    print("you can't!!!")
            show()
            check_game()
            print("computer")
            while win==0 and draw!=1:
                row=random.choice(com)
                col=random.choice(com)
                if 0<=row<=2 and 0<=row<=2:
                    if game_board[row][col]=="*":
                        game_board[row][col]="o"
                        break
                    else:
                        print(end="")
                else:       
                    print(end="")
            show()
            check_game()
    if win==0 and h != 1: 
        menu=input("please yes or no:")