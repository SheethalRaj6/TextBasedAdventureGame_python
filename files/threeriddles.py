global score #to keep the score
import turtle
def riddle(): #defining the main function 

    fi=open("riddles.txt","r") #opening the txt file where the questions are stored
    lines=fi.readlines() #reading all the lines in the txt file
    
    # initialize turtle screen
    turtle1=turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)
    screen.colormode(255)
    screen.bgpic("ridbg1.gif")#the background image
    screen.title("Riddles")
    screen.setup(width=1000, height=800)
    turtle1.penup()
    turtle1.goto(0,269)#the position where the following should be placed
    turtle1.color('Yellow')
    style = ('Courier', 30, 'italic')
    turtle1.write('Hello, Traveller! \nLets play a riddle game', font=style, align='center') #main title
    turtle1.pendown()
    turtle1.penup()
    turtle1.goto(20,-329)#the position where the following should be placed
    turtle1.color('Yellow')
    style = ('Courier', 28, 'italic')
    turtle1.write('You have three chances to solve each riddle. \n\nComplete at least two riddles to qualify.', font=style, align='center') #main title
    turtle1.pendown()


    def actualriddle(): #defining the function where the riddle is played
        turtle2=turtle.Turtle()
        global score
        score=0
        global x
        name=('map','time','photo') #tuple to store the answers
        x=0
        i=0
        while(x<3):#while no of tries is not exceeded
                turtle.clear()
                turtle.penup()
                turtle.goto(0,109)
                turtle.color(255,222,237)
                qstyle=('Ink Free',19,'bold')
                jstyle=('Century Gothic',20,'italic')
                turtle.write(lines[i],font=qstyle,align='center') #display the question
                turtle.pendown()
                guess=turtle.textinput("What am I?","Your answer: ") #input the answer
                if guess==name[x]: #checking if its correct
                    turtle2.penup()
                    turtle2.goto(0,209)
                    turtle2.color(255,222,237)
                    jstyle=('Century Gothic',20,'italic')
                    turtle2.color(255,222,237)
                    turtle2.write("Correct! Great job. Next Question: ",font=jstyle,align='center')
                    score=score+10
                    turtle2.penup()
                    turtle2.goto(0,200)
                    turtle2.pendown()
                else:
                    u=0
                    while u<2: #giving two additional chances per question, if incorrect
                        turtle2.clear()
                        turtle.penup()
                        turtle.goto(0,-200)
                        turtle.write("Unfortunately, that's incorrect. Try again.",font=jstyle,align='center')
                        turtle.pendown()
                        guess=turtle.textinput("What am I?","Your answer: ")
                        u+=1
                        if  guess==name[x]:#if answer is correct
                            '''turtle.clear()
                            turtle2.penup()
                            turtle2.goto(0,209)
                            turtle2.color(255,222,237)
                            turtle2.write("Correct! Great job. ",font=jstyle,align='center')
                            turtle2.pendown()'''
                            score=score+10
                            break
                turtle2.clear()
                    
                x+=1
                i+=1
                
    actualriddle()
    turtle.clear()
    turtle1.clear()
def scores(score):
    return score
riddle()
scores(score)


