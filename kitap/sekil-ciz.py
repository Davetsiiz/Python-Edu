import turtle

renk=("red","yellow","purple","green","blue","brown","orange")
turtle.pensize(1)
turtle.home()
for x in range(200):
    srenk=x%7
    turtle.pencolor(renk[srenk])
    turtle.circle(x*5/6)
    turtle.forward(x)
    turtle.left(102)
    