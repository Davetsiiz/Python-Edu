import turtle
turtle.shape("arrow")

for a in range(4):
    for b in range(10):
        turtle.penup()
        turtle.goto(-300+a*160,+200+b*-30)
        turtle.pendown()
        turtle.write("Seni Seviyorum")