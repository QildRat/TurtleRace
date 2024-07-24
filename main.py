import turtle as t
from turtle_book import Appearance


def finish_line(x, y, margin):
    f_line = t.Turtle()
    f_line.hideturtle()
    f_line.color("gray")
    f_line.width(10)
    f_line.speed("fast")

    f_line.penup()
    f_line.goto(x=x / 2 - margin, y=int((y / 2) * -1) + margin)
    f_line.setheading(90)
    f_line.pendown()
    f_line.forward(y - margin * 2)

    turtle_size = 40 / 2    # prevent turtle overlapped before winning. win when touches the line.
    return f_line.xcor() - turtle_size


# -------------------------------------------
screen = t.Screen()
screen_x = 500
screen_y = 400
screen_margin = 50
screen.setup(width=screen_x, height=screen_y)

user_choice = screen.textinput("Make your bet", "what color of turtle will win? \n(red/orange/blue/violet/green)")

position = (-100, -50, 0, 50, 100)

red = Appearance("red", position[0])
orange = Appearance("orange", position[1])
blue = Appearance("blue", position[2])
violet = Appearance("violet", position[3])
green = Appearance("green", position[4])

finish = finish_line(screen_x, screen_y, screen_margin)
racer = (red, orange, blue, violet, green)

is_finish = False
winner = ""

while not is_finish:
    for i in racer:
        i.move_turtle()
        pos = i.obj.xcor()
        if pos >= finish:
            is_finish = True
            winner += i.name

if user_choice.lower() == winner.lower():
    print("You win!")
else:
    print("You lose!")

print(f"{winner.title()} is the winner")

screen.exitonclick()
