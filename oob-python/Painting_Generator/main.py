import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.hideturtle()
color_list = [
    (160, 111, 175), (210, 150, 207), (254, 247, 191), (188, 130, 129),
    (190, 210, 181), (175, 226, 146), (103, 225, 239), (121, 220, 199),
    (144, 175, 123), (229, 171, 159), (176, 152, 128), (142, 111, 252),
    (117, 103, 196), (180, 168, 147), (112, 150, 122), (111, 167, 176),
    (248, 249, 135), (114, 231, 166), (254, 195, 173), (253, 119, 196),
    (124, 251, 155), (246, 234, 114), (206, 214, 141), (140, 228, 192),
    (167, 115, 193), (144, 188, 223), (150, 113, 223), (191, 124, 104)
]

tim.setheading(210)
tim.forward(300)
tim.setheading(270)
tim.forward(70)
tim.setheading(0)
tim.speed("fastest")
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()