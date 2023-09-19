import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
def game():
    car_countddown=6

    player = Player()
    car=CarManager()
    score_board=Scoreboard()
    screen.listen()
    screen.onkey(player.move, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        score_board.update_level()
        if car_countddown==6:
            car.create_car()
            car_countddown=0
        car.move()
        if player.ycor()>250:
            time.sleep(0.3)
            player.level_up()
            score_board.level_up()
            car.level_up()
        for _car in car.cars:
            if _car.distance(player)<20:
                time.sleep(0.2)
                for car in car.cars:
                    car.goto(-350,-350)
                    car.color("white")
                score_board.game_over()
                game_is_on=False
        car_countddown+=1
        screen.update()
    screen.onkey(restart_game,"r")

def restart_game():
    screen.clear()
    game()
game()
screen.exitonclick()