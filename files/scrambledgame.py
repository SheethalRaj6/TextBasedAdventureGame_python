import turtle
import random
def scramblegame(): #creating a function scramgame
    global score
    score=0
    wn=turtle.Screen()#creating a screen
    wn.tracer(0)
    wn.colormode(255)
    wn.setup(1000,800)#setting screen size
    wn.title("scramble")#giving window title
    turtle.bgpic("scra.gif")#giving image as a backgroud
    turtle1=turtle.Turtle()
    turtle1.penup()
    turtle1.color(0,0,0)#color of the sentence
    turtle1.goto(0,240)#To position the sentence at the given coordinate (0,240)
    turtle1.write("LET'S  PLAY  THE  SCRAMBLE  GAME",font=('Broadway',29,'italic','bold'), align='center')
    turtle1.color('white')#text color
    turtle1.goto(0,140)#text position
    turtle1.write("Guess the given scrambled word :", font=('Broadway',29,'italic'), align='center')
    turtle1.color('yellow')#text color
    turtle1.goto(0,200)#To position the sentence at the given coordinate (0,200)
    turtle1.write("Unscramble three words to qualify to the next round",font=('Times',20,'italic','bold'), align='center')

    
    turtle3=turtle.Turtle()
    turtle2=turtle.Turtle()
    l=[]
    with open("names.txt") as f: #opening a text file, names.txt
        for line in f:
            a=line.split(" ")
            l.append(a)

    count=0
    cheat=[]
    i=0
    while i<3:#giving 3 scrambled words
        s=random.randint(0,11)#generating random integer 
        if s not in cheat:#for not repeating the same scrambled word
            i+=1
            word=l[s][0]#accessing the orginal word
            scram=l[s][1]#accessing the scrambled word
            turtle.goto(0,-150)
            turtle.color('white')
            turtle.write("The scrambled word is : ",font=('Broadway',20),align='center')
            turtle.color(251,232,252)
            turtle.goto(0,-330)
            turtle.write(scram,font=('Calisto MT',49,'bold'),align='center')
            cheat.append(s)
            #inputing user's guess word
            guess=turtle.textinput('Give it a try', 'Guess:')
            turtle.clear()

            if guess==word:#checking if the orginal word and guess word is similar
                score=score+10
                #print(score)
                turtle3.clear()
                turtle2.pencolor(210,154,156)
                turtle2.color('white')
                turtle2.goto(30,80)
                turtle2.write("Correct Word",font=('Broadway',40,'italic'),align='center')
                turtle2.goto(30,5)
                turtle2.pendown()
                count+=1
                

            else:#if the guessed word is incorrect
                turtle2.clear()
                turtle3.pencolor(210,154,156)
                turtle3.color('black')
                turtle3.goto(30,80)
                turtle3.write("Wrong Word",font=('Broadway',40,'italic'),align='center')
                turtle3.goto(30,5)
                turtle3.pendown()
        else:
            continue
    
    turtle1.clear()
    turtle2.clear()
    turtle3.clear()
    turtle.clear()
    #print(score)
def scores(score):
    return score
scramblegame()#calling the function
scores(score)


