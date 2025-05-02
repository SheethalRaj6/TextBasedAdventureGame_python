import turtle
import random
def guess(): #defining the main function where the program is stored
    screen = turtle.Screen()
    screen.tracer(0)
    screen.colormode(255)
    screen.bgpic("nombresgif1.gif")
    screen.title("Guess the Number")
    screen.setup(width=1000, height=800)
    turtle1=turtle.Turtle()
    turtle1.penup()
    turtle1.goto(0,199)
    turtle1.color('White')
    style = ('Engravers MT', 25, 'normal')
    turtle1.write('Hello, Traveller! \n    Lets play a \n     guessing game', font=style, align='center') #main title
    turtle1.pendown()

    def actualguess(): #function where the actual game is played

        style = ('Engravers MT', 25, 'normal')
        y=1
        u=1
        v=1
        gstyle = ('Felix Titling', 25, 'normal')
        fstyle=('Cascadia Mono Semilight',29,'bold')
        
        turtle2=turtle.Turtle()
        turtle3=turtle.Turtle()
        turtle4=turtle.Turtle()
        turtle5=turtle.Turtle()
        rand=random.randint(0,25)
        turtle4.penup()
        turtle4.goto(-35,-325)
        turtle4.color(174, 241, 252)
        turtle4.write('\n\n\tThis integer number \n\tis between 0 and 25. \n\tWhat do you \n\tthink it is? \n\tYou must guess \n\twithin 5 attempts',font=style,align='center')
        turtle4.pendown()
        guess=turtle.textinput("Which number is it?","Your answer: ") #input the answer
        while int(guess)!=rand: #as long as the input answer is incorrect
            turtle5.clear()
            
            turtle3.clear()
            turtle2.penup()
            turtle2.goto(-350,-10)
            turtle2.color('White')
            style2 = ('Engravers MT', 20, 'normal')
            turtle2.write('Number of \nattempts \nso far:', font=style2, align='center') #main title
            turtle2.pendown()
            turtle5.penup()
            turtle5.color("White")
            turtle5.goto(-350,-70)
            turtle5.write(y, font=('Engravers MT', 25, 'normal'), align='center') #no of tries
            turtle5.pendown()
            if int(guess)<rand:
                turtle3.penup()
                turtle3.goto(0,129)#the position where the following should be placed
                turtle3.color(255, 237, 196)
                turtle3.write('Go higher.',font=fstyle,align='center')
                turtle3.pendown()
                guess=turtle.textinput("Which number is it?","Your answer: ")
                y+=1
                
            else:
                turtle5.clear()
                turtle5.penup()
                turtle5.color("White")
                turtle5.goto(-350,-70)
                turtle5.write(y, font=('Engravers MT', 25, 'normal'), align='center') #no of tries
                turtle5.pendown()
                turtle3.penup()
                turtle3.goto(0,129)#the position where the following should be placed
                turtle3.color(255, 237, 196)
                turtle3.write('Go lower.',font=fstyle,align='center')
                guess=turtle.textinput("Which number is it?","Your answer: ")
                y+=1
                
                
                
        else: #if input is the correct answer
            turtle2.clear()
            turtle3.clear()
            turtle4.clear()
            turtle5.clear()
            turtle3.penup()
            turtle3.goto(0,129)
            turtle3.color(93, 255, 43)
            turtle3.write('Correct guess! Good job :)',font=gstyle,align='center')
            turtle3.penup()
            turtle3.goto(0,79)
            turtle3.color(93, 255, 43)
            turtle3.write('No of tries taken:',font=gstyle,align='center')#total no of tries
            turtle3.goto(0,49)
            turtle3.color(93, 255, 43)
            turtle3.write(y,font=gstyle,align='center')
            if (y<6):#if no of attempts was less than 6, the game is won
                turtle.hideturtle()
                turtle3.clear()
                f=open("character.txt",'r')
                line=f.readline()#reading which character was chosen 
                import win
                if line=='1': #and displaying accordingly
                    win.commanderwin()
                elif line=='2':
                    win.elfwin()
                elif line=='3':
                    win.healerwin()
                else:
                    win.thiefwin()
                f.close() 
            else:#if no of attempts was 6 or more
                turtle3.goto(0,-49)
                turtle3.color(93, 255, 43)
                turtle3.write("Unfortunately, you exceed the maximum \nnumber of tries. You have lost.",font=gstyle,align='center')
                import finallost
                turtle3.clear()
    actualguess()
    turtle1.clear()
guess()
