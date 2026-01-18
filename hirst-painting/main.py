# import colorgram
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as n
import random

n.colormode(255)
nilu = n.Turtle()
rgb_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5),
            (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17),
            (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62),
            (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238),
            (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

nilu.penup()
nilu.speed("fastest")
nilu.hideturtle()
number_of_dots = 100
nilu.setheading(225)
nilu.forward(300)
nilu.setheading(0)


for dots_count in range(1, number_of_dots + 1):
    nilu.dot(20, random.choice(rgb_list))
    nilu.forward(50)
    if dots_count %10 == 0:
        nilu.setheading(90)
        nilu.forward(50)
        nilu.setheading(180)
        nilu.forward(500)
        nilu.setheading(0)

n.exitonclick()
