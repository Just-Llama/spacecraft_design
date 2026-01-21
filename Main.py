import turtle as trtl
wn = trtl.Screen()

#   turtle settings and background color
t = trtl.Turtle()
screen = trtl.Screen()
screen.bgcolor("DodgerBlue")
t.speed(4)
t.pensize(3)

#   colors
program_loop = True
while program_loop:
    color_list = ["white", "red", "blue", "green", "hotpink", "gold", ]
    while True:
        color_choice = input("Pick your main color: white, red, blue, green, hotpink, gold - ")
        if color_choice in color_list:
            color_choice2 = input("Pick your accent color: white, red, blue, green, hotpink, gold - ")
            if color_choice2 in color_list:
                break
        else:
            print("Pick again, that one is not an option")

    #  create body
    t.penup()
    t.goto(-25, 125)
    t.pendown()
    t.fillcolor(color_choice)
    t.begin_fill()
    for i in range(2):
        t.forward(75)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(12.5, 55)
    t.pendown()
    t.fillcolor("seashell2")
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-25, 25)
    t.pendown()
    t.fillcolor(color_choice2)
    t.begin_fill()
    for i in range(2):
        t.forward(75)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill()

#   ask user for base engine
    base_engine = int(input("Do you want 1 or 2 base engines? - "))

#   create base engine
    t.fillcolor("gray")
    if (base_engine == 1):

#   one large engine
        t.penup()
        t.goto(-11.5, -125)
        t.pendown()
        t.begin_fill()
        t.forward(50)
        t.right(65)
        t.forward(25)
        t.right(115)
        t.forward(75)
        t.right(115)
        t.forward(25)
        t.end_fill()
    if (base_engine == 2):

#   two small engines
        t.penup()
        t.goto(-3.5, -125)
        t.pendown()
        t.begin_fill()
        t.forward(5)
        t.right(65)
        t.forward(20)
        t.right(115)
        t.forward(35)
        t.right(115)
        t.forward(20) 
        t.end_fill()
        t.goto(35.5, -125)
        t.setheading(360)
        t.begin_fill()
        t.forward(5)
        t.right(65)
        t.forward(20)
        t.right(115)
        t.forward(35)
        t.right(115)
        t.forward(20) 
        t.end_fill()
    side_engine = input("Do you want side engines, yes or no? - ")

#   create side engines
    if (side_engine == "yes"):
        t.penup()
        t.goto(-25, 20)
        t.pendown()
        t.setheading(0)
 
#   left side engine
        t.fillcolor(color_choice)
        t.begin_fill()
        for i in range(2):
            t.right(90)
            t.forward(145)
            t.right(90)
            t.forward(35)
        t.end_fill()
        t.penup()
        t.goto(85, 20)
        t.pendown()
        t.setheading(0)
        t.begin_fill()
        for i in range(2):
            t.right(90)
            t.forward(145)
            t.right(90)
            t.forward(35)
        t.end_fill()
        t.penup()
        t.goto(-42.5, -125)
        t.pendown()
        t.fillcolor("gray")
        t.begin_fill()
        for i in range(2):
          t.forward(5)
          t.right(65)
          t.forward(20)
          t.right(115)
          t.forward(35)
          t.right(115)
          t.forward(20)
          t.penup()
          t.goto(74.5, -125)
          t.setheading(0)
          t.pendown()
        t.end_fill()

#   ask user for snout
    snout = input("Do you want a sharp or smooth snout? - ")

#   create sharp snout
    t.fillcolor(color_choice)
    if (snout == "sharp"):
        t.penup()
        t.goto(-25, 125)
        t.pendown()
        t.setheading(360)
        t.begin_fill()
        for i in range(3):
            t.forward(75)
            t.left(120)
        t.end_fill()

#   create smooth snout
    if (snout == "smooth"):
        t.setheading(90)
        t.penup()
        t.goto(50, 125)
        t.pendown()
        t.begin_fill()
        t.circle(37.5,180,8)
        t.end_fill()
    if (side_engine == "yes"):
  
#   create 2 smaller sharp snouts
        if (snout == "sharp"):
            t.penup()
            t.goto(-60.5, 20)
            t.pendown()  
            t.begin_fill()
            for i in range(3):
                t.forward(35)
                t.left(120)
            t.end_fill()
            t.penup()
            t.goto(50.5, 20)
            t.pendown() 
            t.begin_fill()
            for i in range(3):
                t.forward(35)
                t.left(120)
            t.end_fill()

#   create 2 smaller smooth snouts
        if (snout == "smooth"):
            t.penup()
            t.goto(-25.5, 20)
            t.pendown()
            for i in range(2):
              t.begin_fill()
              t.setheading(90)
              t.circle(17.5,180,8)
              t.end_fill()
              t.penup()
              t.goto(84.5, 20)
              t.pendown()
              
#   ask user for wings
    wings = input("Do you want wings, type yes or no? - ")

#   create wings
    if (wings == "yes"):

#   left wing
        t.penup()
        t.goto(-25, -5)
        t.pendown()
        t.setheading(215)
        t.fillcolor(color_choice2)
        t.begin_fill()
        t.forward(100)
        t.left(40)
        t.forward(40)
        t.left(110)
        t.forward(93)
        t.setheading(90)
        t.forward(88)
        t.end_fill()
#   right wing
        t.penup()
        t.goto(50, -5)
        t.pendown()
        t.setheading(325)
        t.begin_fill()
        t.forward(100)
        t.right(40)
        t.forward(40)
        t.right(110)
        t.forward(93)
        t.setheading(90)
        t.forward(88)
        t.end_fill()

#   middle wing
        t.penup()
        t.goto(15, -5)
        t.pendown()
        t.setheading(270)
        t.begin_fill()
        for i in range(2):
            t.forward(95)
            t.right(90)
            t.forward(5)
            t.right(90)
        t.penup()
        t.goto(10, -60)
        t.pendown()
        t.left(90)
        t.forward(5)
        t.end_fill()
    print("Congrats! You designed a Space Ship! - ")

#   end program
    t.hideturtle()
    program_loop = False
    wn = trtl.Screen()
    wn.mainloop()

