def finallost():#image to be displayed when lost in guess the number
    import turtle

    screen=turtle.Screen()
    screen.tracer(0)
    screen.colormode(255)
    turtle.bgpic("finallost.gif")
    screen.title("You lost.")
    screen.setup(width=1000, height=800)
finallost()
