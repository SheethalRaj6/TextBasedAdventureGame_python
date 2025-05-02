import turtle
def charnpath():#creating a function charnpath
    global numchar
    global char1
    screen_size=1000,800
    wn=turtle.Screen()#creating a screen
    wn.tracer(0)
    wn.colormode(255)
    wn.setup(*screen_size)#setting screen size
    turtle.bgpic("chgame.gif")#giving image as a backgroud
    numchar=turtle.textinput('CHARACTER', 'Number:')#taking input of character and storing it in numchar
    char1=int(numchar)
    f=open("character.txt",'w')#updating the value of char1 in a file to access at the end
    f.write(str(char1))
    f.close()
    turtle.color(74,44,42)#displaying the text of the choosen character
    turtle.goto(0,-102)
    turtle.write(' You have chosen \n     Character ',font=('Goudy Old Style',38,'italic'),align='center')
    turtle.goto(0,-200)
    turtle.write(numchar,font=('Goudy Old Style',38,'italic'),align='center')

    def fun(x,y):#depending on the character selected a different image is shown for path selectiono
        global char1
        if char1==1:
            turtle.bgpic("cochpath.gif")
        elif char1==2:
            turtle.bgpic("elfchpath.gif")
        elif char1==3:
            turtle.bgpic("hechpath.gif")
        elif char1==4:
            turtle.bgpic("thchpath.gif")
        
        turtle.clear()#clearing previous objects to prevent overlapping
        
        def buttonClick(x,y):#choosing paths
            if x<-200 and x>-400 and y<-100 and y>-400: #importing the base with the games of path A
                import base
                turtle.exitonclick()
            elif  x>100 and x<400 and y<-100 and y>-400:    #importing the base with the games of path A
                import base2
                turtle.exitonclick()
        turtle.onscreenclick(buttonClick,1) #on clicking it calls buttonClick 
    turtle.onscreenclick(fun)#calling path selection on click
charnpath() #calling the function









