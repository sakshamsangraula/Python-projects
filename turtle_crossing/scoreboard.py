from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_BOLD = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.time_speed = 0.1
        self.update_level()

    def update_level(self):
        # clear previous entry
        self.clear()
        self.penup()
        self.goto(-210, 220)
        self.write(f"Level: {self.level}", align = "center", font=FONT)

    def level_up(self):
        self.level += 1
        self.time_speed *= 0.5
        self.update_level()


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT_BOLD)



