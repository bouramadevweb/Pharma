import turtle

# Création d'une tortle
t = turtle.Turtle()

# Déplacer la tortue à la position de départ
t.penup()
t.goto(-50, 0)
t.pendown()

# Dessiner l'étoile sans lignes internes
for _ in range(5):
    t.forward(100)
    t.left(144)

# Affichage de la fenêtre
turtle.done()
