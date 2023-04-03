from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,p):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(p)
        
        
    def go_up(self):
        new_y =self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y) 
    
    def Up(self):
        new_y =self.ycor()+20
        self.goto(self.xcor(),new_y)

    def Down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)