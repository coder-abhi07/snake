from snake import Snake
from food import Food
from score import Score
from turtle import Screen
import time

screen = Screen()
screen.title("snake game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

running = True
while (running):
    screen.update()
    time.sleep(.1)
    snake.move()

    if (snake.head.distance(food) < 15):
        food.refresh()
        snake.extend()
        score.increase_score()

    if (snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280):
        score.gameOver()
        running = False
    
    for seg in snake.segments[1:]:
        if (snake.head.distance(seg) < 10):
            score.gameOver()
            running = False
screen.exitonclick()
