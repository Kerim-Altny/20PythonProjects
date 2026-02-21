from turtle import Turtle
class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(position)
        self.dx = 3
        self.dy = 3

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1