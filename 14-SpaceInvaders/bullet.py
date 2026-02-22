from turtle import Turtle


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.hideturtle()
        self.bullet_speed = 1
        self.state = "ready"

    def fire_bullet(self, player_x, player_y):
        if self.state == "ready":
            self.state = "fire"
            self.setposition(player_x, player_y + 10)
            self.showturtle()

    def move_bullet(self):
        if self.state == "fire":
            y = self.ycor()
            y += self.bullet_speed
            self.sety(y)
            if self.ycor() > 275:
                self.hideturtle()
                self.state = "ready"