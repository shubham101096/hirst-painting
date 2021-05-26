import colorgram
import turtle as t
import random

colors = colorgram.extract("image.jpg", 30)

color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)

print(color_list)

# color_list = [(36, 95, 184), (236, 165, 79), (244, 223, 88), (216, 69, 105), (98, 197, 234), (250, 51, 22), (204, 70, 20), (240, 107, 144), (186, 47, 91), (142, 233, 216), (252, 136, 166), (166, 175, 233), (66, 45, 13), (71, 206, 170), (82, 187, 99), (252, 220, 0), (20, 156, 51), (167, 27, 8), (24, 36, 86), (250, 153, 2), (107, 38, 44), (22, 152, 228), (106, 214, 249), (254, 12, 3), (93, 96, 192), (37, 47, 99)]

timmy = t.Turtle()
t.colormode(255)
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()

for i in range(10):
    timmy.setposition(-300, -300 + i*50)
    for j in range(10):
        timmy.pendown()
        timmy.dot(10, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)


screen = t.Screen()

screen.exitonclick()