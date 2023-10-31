import colorgram
import turtle as t
import random
import draw_painting as d

# gets colours from picture and puts them in an array
colors = colorgram.extract('image.jpg', 30)
my_colors = []

for c in colors:
    my_colors.append((c.rgb[0], c.rgb[1], c.rgb[2]))

# create Turtle and drawing objects
sam = t.Turtle()
t.colormode(255)
sam.hideturtle()
draw = d.Draw_painting(sam)


turn = 'forward'

for x in range(10):
    for y in range(10):
        draw.draw_dot(random.choice(my_colors))
    sam.penup()
    if turn == 'forward':
        draw.turn_right()
        turn = 'back'
    else:
        draw.turn_left()
        turn = 'forward'
    sam.pendown()

screen = t.Screen()
screen.exitonclick()