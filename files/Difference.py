import turtle
def difference():#creating a function called difference to execute the game
    global score
    score=0
    first = 'im1.gif' #loading the images to be displayed into variables
    second = 'im2.gif'

    screen = turtle.Screen() #creating a screen and setting its size and colormode
    screen.setup(1000,800)
    screen.colormode(255)
    turtle.bgpic("castle.gif")  #giving an image as the background
    screen.title("Find the differences")    #titling the window
    screen.register_shape(first)    #adding to the list of shapes
    screen.register_shape(second)

    turtle1 = turtle.Turtle(shape=first)    #placing image1, image 1 is placed as a shape
    turtle1.penup()
    turtle1.goto(200, 100)
    turtle1.stamp()
    turtle1.hideturtle()

    turtle2 = turtle.Turtle(shape=second)   #placing image2
    turtle2.penup()
    turtle2.goto(-200, 100)
    turtle2.stamp()
    turtle2.hideturtle()
    
    #writing the text to be displaced with all the required characteristics
    turtle3=turtle.Turtle()
    turtle3.penup()
    turtle3.hideturtle()
    turtle3.setposition(0,300)
    turtle3.color("brown")
    turtle3.write("Find the differences",False,align="center",font=("Bodoni MT",50))
    turtle3.setposition(0,-250)
    turtle3.color("white")
    turtle3.write("Guess any five differences to qualify",align="center",font=("Broadway",30))

    
    ans=["bee","leaf","hand","tree","cloud","smile","flower","snow","grass","branch","stone","grass",]  #correct answers are stored in this list
    enter=[]    #entered answers and stored here
    
    for i in range(5):  #taking the input of answers and verifying to update score
        option1=turtle.textinput("Differences","Enter a difference")
        
        turtle.clear()
        if option1.lower() in ans and option1.lower() not in enter:
            enter.append(option1)
            score=score+5
            turtle.penup()
            turtle.hideturtle()
            turtle.setposition(-200,-150)
            turtle.write("Correct",align="center",font=("Arial",30))
            turtle.setposition(-200,-200)
            turtle.write(score,align="center",font=("Arial",20))
        else:
            turtle.penup()
            turtle.hideturtle()
            turtle.setposition(-200,-150)
            turtle.write("Wrong",align="center",font=("Arial",30))
            turtle.setposition(-200,-200)
            turtle.write(score,align="center",font=("Arial",20))
            
    if score==25:
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition(200,-150)
        turtle.write("Qualified",align="center",font=("Arial",20))
        turtle.color(0,0,0)
    else:
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition(200,-150)
        turtle.write("Disqualified",align="center",font=("Arial",20))
        turtle.color(0,0,0)
               
    turtle.clearscreen()#clears the screen for the next game
def scores(score):#creating another function with attribute score so that we can access it elsewhere
    return score
difference()    #calling the functions
scores(score)

