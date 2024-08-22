import tkinter
import turtle
import random
import time

#Score
score = 0
high_score = 0

#Screen
turt = turtle.Screen()
turt.title("Snake by AT")
turt.bgcolor("#F4FFFD")
turt.setup(width=800, height=800)
turt.tracer(0)
turt.cv._rootwindow.resizable(False, False)

#Head of the Snake
hd = turtle.Turtle()
hd.speed(0)
hd.shape("square")
hd.color("#F9DC5C")
hd.penup()
hd.goto(0,0)
hd.drct = "stop"

#Snake's food a bug
bug = turtle.Turtle()
bug.speed(0)
bug.shape("circle")
bug.color("#ED254E")
bug.penup()
bug.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#011936")
pen.penup()
pen.hideturtle()
pen.goto(-350, 320)
pen.write("Score: 0", align="left", font=("Arial", 24, "normal"))
pen.goto(-350, 280)
pen.write("High Score: 0", align="left", font=("Arial", 24, "normal"))


#Delay
delay = 0.1

#Functions for Movement of the Snake

def go_left():
    if hd.drct != "right":
        hd.drct = "left"

def go_right():
    if hd.drct != "left":
        hd.drct = "right"

def go_up():
    if hd.drct != "down":
        hd.drct = "up"

def go_down():
    if hd.drct != "up":
        hd.drct = "down"

def move():
    if hd.drct == "up":
        y = hd.ycor()
        hd.sety(y + 20)

    if hd.drct == "down":
        y = hd.ycor()
        hd.sety(y - 20)

    if hd.drct == "left":
        x = hd.xcor()
        hd.setx(x - 20)

    if hd.drct == "right":
        x = hd.xcor()
        hd.setx(x + 20)

# Keyboard bindings can be played with both: WASD and Arrow Keys
turt.listen() #in order to collect key-events
turt.onkeypress(go_up, "w")
turt.onkeypress(go_down, "s")
turt.onkeypress(go_left, "a")
turt.onkeypress(go_right, "d")

turt.onkeypress(go_up, "Up")
turt.onkeypress(go_down, "Down")
turt.onkeypress(go_left, "Left")
turt.onkeypress(go_right, "Right")

while True:
    turt.update()

    #Check for a collision with the border, game ends if collision occurs:
    if hd.xcor()>390 or hd.xcor()<-390 or hd.ycor()>390 or hd.ycor()<-390:
        time.sleep(1)
        hd.goto(0,0)
        hd.drct = "stop"
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        bug.goto(x,y)

        #Hiding the segements outside the view
        for segment in segments:
            segment.goto(1000, 1000)

        #Clearing Segments list
        segments.clear()

        #Game Restarts, Resetting the score to 0
        score = 0

        #Resetting delay, game restarts
        delay = 0.1

        pen.clear()
        pen.goto(-350, 320)
        pen.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))
        pen.goto(-350, 280)
        pen.write("High Score: {}".format( high_score), align="left", font=("Arial", 24, "normal"))
        

    #Checks if the snake eats the bug
    if hd.distance(bug) < 20:
        #Move a new bug to a random spot
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        bug.goto(x,y)

        #Increase snake's length
        if score%2==0:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("#465362")
            new_segment.penup()
            segments.append(new_segment)

        elif score%2!=0:
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("#999799")
            new_segment.penup()
            segments.append(new_segment)

        #Make the game faster
        delay -= 0.005

        #Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.goto(-350, 320)
        pen.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))
        pen.goto(-350, 280)
        pen.write("High Score: {}".format( high_score), align="left", font=("Arial", 24, "normal"))

    #Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = hd.xcor()
        y = hd.ycor()
        segments[0].goto(x,y)

    move()    

    #Check if the snake bites itself
    for segment in segments:
        if segment.distance(hd) < 20:
            time.sleep(1)
            hd.goto(0,0)
            hd.drct = "stop"
            x = random.randint(-390, 390)
            y = random.randint(-390, 390)
            bug.goto(x,y)
        
            #Hiding the segements outside the view
            for segment in segments:
                segment.goto(1000, 1000)
        
            #Clearing the segments list
            segments.clear()

            #Game Restarts, Resetting the score to 0
            score = 0

            #Resetting delay, game restarts
            delay = 0.1
        
            #Updating Score
            pen.clear()
            pen.goto(-350, 320)
            pen.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))
            pen.goto(-350, 280)
            pen.write("High Score: {}".format( high_score), align="left", font=("Arial", 24, "normal"))
    time.sleep(delay)

turt.mainloop()