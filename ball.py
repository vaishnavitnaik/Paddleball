from turtle import Turtle
import random 
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        new_x= self.xcor() + self.xmove
        new_y= self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ymove *=-1 
        # once it reaches 280 in the top we need to decrease the value of Y so that it comes back and increase value of x so it keeps going
        # therefore we multipy ymove by -1 so that when bounce function is called instead of increasing value we decrease it
        

    def bounce_x(self):
        self.xmove *=-1 
        self.movespeed*=0.9

    # right paddle misses
    def reset(self):
        self.goto(0,0)
        self.movespeed=0.1
        self.bounce_x() #start from left
