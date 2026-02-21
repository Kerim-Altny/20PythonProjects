
from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("red")
        self.penup()
        self.goto(position)
    
    def hit(self):
        self.goto(1000, 1000)
        self.hideturtle()
        
def create_bricks(rows, cols):
    bricks = []
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    start_x = -360
    start_y = 250
    for row in range(rows):
        current_color = colors[row % len(colors)]
        for col in range(cols):
            x = start_x + (col * 50) 
            y = start_y - (row * 30)
            brick = Brick((x, y))
            brick.color(current_color)
            bricks.append(brick)
            
    return bricks