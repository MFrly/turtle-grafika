import turtle
import random


def spirala():
    for i in range(50):
        turtle.forward(i)
        turtle.left(20)
    turtle.ontimer(turtle.Screen().bye, 2000)
    
def random_shape():
    for i in range(50):
        turtle.forward(random.randint(1,100))
        turtle.right(random.randint(1,100))
    turtle.ontimer(turtle.Screen().bye, 3500)
    
def zprava():
    turtle.write("Kreslime si pomoci Python :)")
    
def jednicka():
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(135)
    turtle.forward(70)
    turtle.hideturtle()
    turtle.mainloop()
 