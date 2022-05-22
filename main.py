import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.move, "space")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    scoreboard.write_score()
    if player.ycor() == 290:
        scoreboard.clear()
        scoreboard.update_score()
        player.goto(0, -280)
        car_manager.level_up()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            player.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
            game_is_on = False

screen.exitonclick()
