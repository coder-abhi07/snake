from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = "center", font= ("Arial, 25"))    


    def update_score(self):
        self.write(f"SCORE : {self.score}", align = "center", font= ("Arial, 15"))    
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


