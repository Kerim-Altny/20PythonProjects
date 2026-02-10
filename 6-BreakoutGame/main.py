import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import create_bricks
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)


paddle = Paddle((0, -250))
ball = Ball((0, -230))
bricks = create_bricks(6, 15)
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle.start_left, "Left")   
screen.onkeyrelease(paddle.stop, "Left")      


screen.onkeypress(paddle.start_right, "Right") 
screen.onkeyrelease(paddle.stop, "Right")      

game_is_on = True
while game_is_on:
    time.sleep(0.01) 
    screen.update()
    paddle.move()
    ball.move()

    
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

   
    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -230:
       if ball.dy < 0:
            ball.bounce_y()
    

    for brick in bricks:
        if ball.distance(brick) < 35:
            scoreboard.point()
            
            brick.hit()       
            bricks.remove(brick) 
            ball.bounce_y()   
            break              

    if ball.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()