from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        
        self.x_speed = 0

    def move(self):
        new_x = self.xcor() + self.x_speed
        if -350 < new_x < 350:
            self.setx(new_x)

    def start_left(self):
        self.x_speed = -15 

    def start_right(self):
        self.x_speed = 15 

    def stop(self):
        self.x_speed = 0