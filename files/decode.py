import turtle
import random
def decodegame():#creating a function decodegame
    global score
    score=0
    wn=turtle.Screen()#creating a screen
    wn.tracer(0)
    wn.colormode(255)
    wn.setup(1000,800)#setting screen size
    wn.title("decode")#giving window title
    wn.bgpic("dee.gif")#giving image as a backgroud
    turtle.penup()
    turtle.color(255,216,1)#color of the sentence
    turtle.goto(10,260)#To position the sentence at the given coordinate (0,240)
    turtle.write("LET'S  PLAY  THE  DECODE  WORD  GAME",font=('Broadway',32,'italic'), align='center')
    turtle.color('white')
    turtle.goto(0,200)
    #example
    turtle.write("( Example : For the word DESKTOP the encoded word is DFUNXTV ) ",font=('Times',25,'bold'), align='center')
    turtle.color(255,216,1)
    turtle.goto(0,140)
    turtle.write("Decode the give word:", font=('Times',25,'italic','bold'), align='center')
    turtle.penup()
    turtle.color(255,255,255)
    turtle.goto(15,-260)
    turtle.write("Decode this word to move to the next level",font=('Arial Bold',28,'italic'), align='center')

    E=['message', 'database' , 'graphics' , 'screen']
    L=[]
    for w in E:#accessing word in list E
        st=''
        for i in range(len(w)):# encoding the word
            ad=ord(w[i])+i#getting ascii value and encoding the word
            st+=chr(ad)#adding it to a string st after making it a character
        L.append(st)
    n=random.randint(0,3)
    turtle.goto(0,65)
    turtle.color('black')
    turtle.write(L[n],font=('Calisto MT',50,'italic','bold'), align='center')
    #getting decoded input from user
    g=turtle.textinput('decode',"Correct word: ")

    if g==E[n]:#checking if user's input is correct and updating score
        score=score+10
        
    turtle.clear()
def scores(score):
    return score
decodegame()
scores(score)


