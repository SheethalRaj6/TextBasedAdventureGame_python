#creating the game of tictactoe
import tkinter as tk  
from tkinter import *  #importing the required libraries
import random
from tkinter import messagebox
count=0
global root
def tictactoe():
    global root
    root=tk.Tk() #creatingtkinter screen
    root.title("Tic Tac Toe") #giving a title to the window
    frame=Frame(root)#creating the grid in the screen
    frame.grid()
    l=[[0,0,0],[0,0,0],[0,0,0]] #2D to append the selected X/O 
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    def click(n):   #happens when a button is clicked
        global count
        count+=1
        global button1,button2,button3,button4,button5,button6,button7,button8,button9
        #displaying X depending on the button pressed by the user
        if n=="1":
            button1=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button1.grid(row=0,column=0)
            l[0][0]="X"
        elif n=="2":
            button2=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button2.grid(row=0,column=1)
            l[0][1]="X"
        elif n=="3":
            button3=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button3.grid(row=0,column=2)
            l[0][2]="X"
        elif n=="4":
            button4=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button4.grid(row=1,column=0)
            l[1][0]="X"
        elif n=="5":
            button5=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button5.grid(row=1,column=1)
            l[1][1]="X"
        elif n=="6":
            button6=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button6.grid(row=1,column=2)
            l[1][2]="X"
        elif n=="7":
            button7=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button7.grid(row=2,column=0)
            l[2][0]="X"
        elif n=="8":
            button8=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button8.grid(row=2,column=1)
            l[2][1]="X"
        else:
            button9=Button(root,text="X",fg="black",background="#ff9c9c",state=DISABLED,width=20,height=10)
            button9.grid(row=2,column=2)
            l[2][2]="X"
        c=0
        while c!=1 and count!=5:#displays random Os as the move of the computer
            a=random.randint(1,10)
            if a==1 and str(button1['state'])!=DISABLED:
                button1=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button1.grid(row=0,column=0)
                l[0][0]="O"
                c=1
            elif a==2 and str(button2['state'])!=DISABLED:
                button2=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button2.grid(row=0,column=1)
                l[0][1]="O"
                c=1
            elif a==3 and str(button3['state'])!=DISABLED:
                button3=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button3.grid(row=0,column=2)
                l[0][2]="O"
                c=1
            elif a==4 and str(button4['state'])!=DISABLED:
                button4=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button4.grid(row=1,column=0)
                l[1][0]="O"
                c=1
            elif a==5 and str(button5['state'])!=DISABLED:
                button5=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button5.grid(row=1,column=1)
                l[1][1]="O"
                c=1
            elif a==6 and str(button6['state'])!=DISABLED:
                button6=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button6.grid(row=1,column=2)
                l[1][2]="O"
                c=1
            elif a==7 and str(button7['state'])!=DISABLED:
                button7=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button7.grid(row=2,column=0)
                l[2][0]="O"
                c=1
            elif a==8 and str(button8['state'])!=DISABLED:
                button8=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button8.grid(row=2,column=1)
                l[2][1]="O"
                c=1
            elif a==9 and str(button9['state'])!=DISABLED:
                button9=Button(root,text="O",fg="black",background="#d3c5fc",state=DISABLED,width=20,height=10)
                button9.grid(row=2,column=2)
                l[2][2]="O"
                c=1
            else:
                continue
        c1=0#counting if all the buttons are used or not
        for i in l:
            for j in i:
                if j!=0:
                    c1+=1
        #checking for win then calling the other continuation games
        if (l[0][0]==l[0][1]==l[0][2]=="X" or l[1][0]==l[1][1]==l[1][2]=="X" or l[2][0]==l[2][1]==l[2][2]=="X" or
           l[0][0]==l[1][0]==l[2][0]=="X" or l[0][1]==l[1][1]==l[2][1]=="X" or l[0][2]==l[1][2]==l[2][2]=="X" or
           l[0][0]==l[1][1]==l[2][2]=="X" or l[0][2]==l[1][1]==l[2][0]=="X"):
                tk.messagebox.showinfo(title="Game over",message="You win",type='okcancel')
                root.destroy()
                import Difference#if tictactoe is won then only import the next game
                Marks=Difference.score
                if Marks==25:#if score is met then import the next game else show lost screen
                    import scrambledgame
                    Marks=scrambledgame.score
                    if Marks==30:#if score is met then import the next game else show lost screen
                        import guessthenumber
                    else:
                        import gamelost
                        gamelost.lost()
                else:
                    import gamelost
                    gamelost.lost()
        #checking for lost game
        elif (l[0][0]==l[0][1]==l[0][2]=="O" or l[1][0]==l[1][1]==l[1][2]=="O" or l[2][0]==l[2][1]==l[2][2]=="O" or
           l[0][0]==l[1][0]==l[2][0]=="O" or l[0][1]==l[1][1]==l[2][1]=="O" or l[0][2]==l[1][2]==l[2][2]=="O" or
           l[0][0]==l[1][1]==l[2][2]=="O" or l[0][2]==l[1][1]==l[2][0]=="O"):
               tk.messagebox.showinfo(title="Game over",message="You lost",type='ok')
               root.destroy()
               import gamelost
               gamelost.lost()
        #checking for draw
        elif c1==9:
            if l[0][0]!=l[0][1] or l[0][0]!=l[0][1] or l[0][0]!=l[1][0] or l[2][2]!=l[2][1] or l[2][2]!=l[1][1] or l[2][2]!=l[1][2]:
               tk.messagebox.showinfo(title="Game over",message="Match draw",type='ok')
               root.destroy()
               import gamelost
               gamelost.lost()
        else:
            return
    #creating the buttons
    button1=Button(root,command=lambda:click("1"),state=ACTIVE,width=20,height=10)
    button2=Button(root,command=lambda:click("2"),state=ACTIVE,width=20,height=10)
    button3=Button(root,command=lambda:click("3"),state=ACTIVE,width=20,height=10)
    button4=Button(root,command=lambda:click("4"),state=ACTIVE,width=20,height=10)
    button5=Button(root,command=lambda:click("5"),state=ACTIVE,width=20,height=10)
    button6=Button(root,command=lambda:click("6"),state=ACTIVE,width=20,height=10)
    button7=Button(root,command=lambda:click("7"),state=ACTIVE,width=20,height=10)
    button8=Button(root,command=lambda:click("8"),state=ACTIVE,width=20,height=10)
    button9=Button(root,command=lambda:click("9"),state=ACTIVE,width=20,height=10)
    #placing the buttons in the grid
    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=1,column=0)
    button5.grid(row=1,column=1)
    button6.grid(row=1,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)
tictactoe() #calling tictactoe

    
        






