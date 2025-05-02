import turtle
def gamestart():#defining the main function where the program is
    screen=turtle.Screen()
    screen.tracer(0)
    screen.colormode(255)
    turtle.bgpic("gamestart.gif")
    screen.title("Adventure Game - Group E3")
    screen.setup(width=1000, height=800)
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-150,-330)
    pen.pendown()
    for i in range(2): #drawing the box where the button will be placed
        pen.color(255,202,56)
        pen.forward(300)
        pen.left(90)
        pen.forward(70)
        pen.left(90)
    pen.penup()
    pen.goto(-150,-320)
    pen.color(255,202,56)
    pen.write('Start Game',font=('Felix Titling',34,'italic'))#the text inside the box
    def buttonClick(x,y):#the function and range of the button
        if x>-150 and x<2000 and y>-329 and y<-239:
            pen.clear()
            import charselect#going to the next stage of the game
    turtle.onscreenclick(buttonClick, 1)#the button is being called
    turtle.listen()
    turtle.done()
gamestart()
    


    
