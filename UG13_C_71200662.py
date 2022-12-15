import turtle


turtle.bgcolor("black")


turtle_obj = turtle.Turtle()


turtle_obj.shape("turtle")
turtle_obj.color("white")
turtle_obj.speed(100)

#Posisi start
turtle_obj.penup()
turtle_obj.goto(-200,0)
turtle_obj.pendown()

#T
turtle_obj.left(90)
turtle_obj.forward(120)
turtle_obj.right(90)
turtle_obj.forward(60)
turtle_obj.right(90)
turtle_obj.right(90)
turtle_obj.forward(120)


#Posisi start
turtle_obj.penup()
turtle_obj.goto(-60,120)
turtle_obj.pendown()

#J
turtle_obj.left(90)
turtle_obj.forward(120)
turtle_obj.right(90)
turtle_obj.forward(60)
turtle_obj.right(90)
turtle_obj.forward(40)

#posisi start
turtle_obj.penup()
turtle_obj.goto(20,0)
turtle_obj.pendown()

# 6
turtle_obj.right(90)
turtle_obj.forward(90)
turtle_obj.left(90)
turtle_obj.forward(60)
turtle_obj.left(90)
turtle_obj.forward(90)
turtle_obj.left(90)
turtle_obj.forward(60)
turtle_obj.right(180)
turtle_obj.forward(120)
turtle_obj.right(90)
turtle_obj.forward(60)

#Posisi start
turtle_obj.penup()
turtle_obj.goto(150,0)
turtle_obj.pendown()

# 6
turtle_obj.left(90)
turtle_obj.forward(120)
turtle_obj.right(180)
turtle_obj.forward(120)
turtle_obj.left(90)
turtle_obj.forward(90)
turtle_obj.left(90)
turtle_obj.forward(60)
turtle_obj.left(90)
turtle_obj.forward(90)
turtle_obj.right (90)
turtle_obj.forward (60)
turtle_obj.right (90)
turtle_obj.forward (60)

#Posisi start
turtle_obj.penup()
turtle_obj.goto(300,0)
turtle_obj.pendown()

# 2
turtle_obj.forward(90)
turtle_obj.left(180)
turtle_obj.forward(90)
turtle_obj.right(90)
turtle_obj.forward(60)
turtle_obj.right(90)
turtle_obj.forward(90)
turtle_obj.left(90)
turtle_obj.forward(60)
turtle_obj.left(90)
turtle_obj.forward(90)


turtle.done()
