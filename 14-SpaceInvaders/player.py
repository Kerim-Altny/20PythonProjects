from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setposition(0, -250)
        self.setheading(90)

        self.move_speed = 0.5
        # State tracking for smooth movement
        self.keys = {"Left": False, "Right": False}

    # Keyboard event methods
    def go_left(self):
        self.keys["Left"] = True

    def stop_left(self):
        self.keys["Left"] = False

    def go_right(self):
        self.keys["Right"] = True

    def stop_right(self):
        self.keys["Right"] = False

    # Movement logic to be called in the main loop
    def move(self):
        if self.keys["Left"]:
            x = self.xcor()
            x -= self.move_speed
            # Boundary check
            if x < -280:
                x = -280
            self.setx(x)

        if self.keys["Right"]:
            x = self.xcor()
            x += self.move_speed
            # Boundary check
            if x > 280:
                x = 280
            self.setx(x)