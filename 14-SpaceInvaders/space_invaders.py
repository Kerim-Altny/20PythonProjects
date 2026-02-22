import turtle
import math

from player import Player
from alien import Alien
from bullet import Bullet



screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=600, height=600)

screen.tracer(0)


player =Player()
aliens=Alien()
bullet = Bullet()


def fire_action():
    bullet.fire_bullet(player.xcor(), player.ycor())


screen.listen()
screen.onkeypress(fire_action, "space")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeyrelease(player.stop_left, "Left")
screen.onkeyrelease(player.stop_right, "Right")



def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 20
try:
    while True:
        player.move()
        aliens.move_alien()
        bullet.move_bullet()

        for alien in aliens.aliens:
            if is_collision(bullet, alien):
                bullet.hideturtle()
                bullet.state = "ready"
                bullet.setposition(0, -400)
                alien.hideturtle()
                alien.setposition(-1000, 1000)
                aliens.aliens.remove(alien)
                break
        screen.update()
except turtle.Terminator:
    print("Game Over")




