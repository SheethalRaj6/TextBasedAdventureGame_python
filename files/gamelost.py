def lost():#screen to be displayed for lost game
    import turtle

    screen=turtle.Screen()
    screen.tracer(0)
    screen.colormode(255)
    turtle.bgpic("gamelost.gif")
    screen.title("Game has ended.")
    screen.setup(width=1000, height=800)

