from turtle import Turtle

class Alien:
    def __init__(self):
        self.aliens = []
        self.fleet_speed = 0.3
        self.create_fleet()

    def create_fleet(self):
        start_x = -200
        start_y = 250
        for row in range(3):
            for col in range(8):
                alien = Turtle()
                alien.color("blue")
                alien.shape("circle")
                alien.penup()
                alien.speed(0)
                x = start_x + (col * 60)
                y = start_y - (row * 60)
                alien.setposition(x, y)

                self.aliens.append(alien)

    def move_alien(self):
        check_border = False
        for alien in self.aliens:
            x=alien.xcor()
            x+=self.fleet_speed
            alien.setx(x)
            if alien.xcor()<-280 or alien.xcor()>280:
                check_border = True


        if check_border == True:
            self.fleet_speed *= -1



