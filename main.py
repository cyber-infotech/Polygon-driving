import turtle
#Drawing Star
drawing_board=turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Star")
turtle_instance=turtle.Turtle()
num_sides = 8
angle = 360.0/num_sides
side_lenght = 100
for i in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_lenght)
turtle.done()
