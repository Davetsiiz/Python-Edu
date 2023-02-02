import turtle
turtle.shape("arrow")

for a in range(11):
    for b in range(11):
        turtle.penup()
        turtle.goto(-300+a*60,+200+b*-30)
        turtle.pendown()
        turtle.write(str(a)+"x"+str(b)+"="+str(a*b))
