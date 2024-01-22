"""gesion_des_erreur
"""
# [erreur]
import turtle
# [FENETRE_SCREEN]
FENETRE_SCREEN = turtle.Screen()
#
demTur = turtle.Turtle()
#
demTur.speed(2)
# [boocle for]
for _ in range(5):
    for _ in range(5):
        demTur.forward(100)
        demTur.right(144)
    demTur.penup()
    demTur.forward(150)
    demTur.pendown()
FENETRE_SCREEN.exitonclick()
# [missing-final-newline]
