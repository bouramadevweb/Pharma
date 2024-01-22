import turtle 


fenetre =turtle.Screen()
demTur=turtle.Turtle()
demTur.speed(2)

for _ in range(5):
    for _ in range(5):
        demTur.forward(100)
        demTur.right(144)
    demTur.penup()
    demTur.forward(150)
    demTur.pendown()
    
turtle.exitonclick()