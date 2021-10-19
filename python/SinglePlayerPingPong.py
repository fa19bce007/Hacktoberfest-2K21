import turtle
import time

# Score varibales
Score = 0
HighScore = 0
Speed = 1

#set up the screen
win = turtle.Screen()
win.title("Single player Ping-Pong game")

try:
    win.bgpic("E:/Python CODE/game.gif")
except:
    win.bgcolor("black")

win.setup(width=800,height=600)
win.tracer(0)

#Border
border = turtle.Turtle()
border.color("white")
border.penup()
border.setposition(-400,-300)
border.pendown()
border.pensize(2)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.hideturtle()

# Creating stick for the game
stick = turtle.Turtle()
stick.shape("square")
stick.color("white")
stick.shapesize(stretch_wid=1,stretch_len=6)
stick.penup()
stick.goto(0,-280)
stick.speed('fastest')

# Creating a ball for the game
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 0.5   # Setting up the pixels for the ball movement.
ball_dy = 0.5

# Creating a pen for updating the Score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write(f"Score: {Score}    High Score: {HighScore}    Speed: {Speed}",align="center",font=('Monaco',20,"normal"))

# Creating a pen for game over message
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color('white')
pen1.penup()
pen1.hideturtle()
pen1.goto(0,0)

# Moving the stick using the keyboard
def stick_left():
    x = stick.xcor()
    x = x - 15
    stick.setx(x)

def stick_right():
    x = stick.xcor()
    x = x + 15
    stick.setx(x)

# Keyboard binding
def quit():
    global running
    running = False

win.listen()
win.onkeypress(stick_left,"Left")
win.onkeypress(stick_right,"Right")
win.onkeypress(quit,"Escape")

# Moving the Stick using Mouse

MOVING = range(2)  # states

def move_handler(x, y):
    if state != MOVING:  # ignore stray events
        return

    onmove(win, None)  # avoid overlapping events
    stick.penup()
    stick.setheading(stick.towards(x, -280))
    stick.goto(x, -280)
    onmove(win, move_handler)

def onmove(self, fun, add=None):

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)

state = MOVING
onmove(win, move_handler)

running = True
# Main game loop
while running:
    win.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border
    if ball.ycor() > 290:   # Top Border
        ball.sety(290)
        ball_dy = ball_dy * -1

    if ball.xcor() > 390:   # Right  Border
        ball.setx(390)
        ball_dx = ball_dx * -1
        
    if ball.xcor() < -390:  # Left Border
        ball.setx(-390)
        ball_dx = ball_dx * -1

    if ball.ycor() < -290:   # Fall into Bottom
        ball.goto(0,0)
        ball_dy = ball_dy * -1

        if HighScore < Score:
            HighScore = Score

        pen1.write(f"Your High Score: {HighScore} & Speed: {Speed}\n     Press Esc to Exit",align="center",font=('Monaco',20,"normal"))
        time.sleep(5)
        pen1.clear()

        Score = 0       # Set Score to 0
        Speed = 1       # Set Speed to 0
        ball_dx = 0.5   # Setting up the pixels for the ball movement.
        ball_dy = 0.5

        pen.clear()
        pen.write(f"Score: {Score}    High Score: {HighScore}    Speed: {Speed}",align="center",font=('Monaco',20,"normal"))

    # Handling the ball with Stick.
    if(ball.ycor() > -270) and (ball.ycor() < -260) and (ball.xcor() < stick.xcor() + 70 and ball.xcor() > stick.xcor() - 70):
        
        Score = Score + 1   # Increasing Score
        if HighScore < Score:   # Increasing High Score
            HighScore = Score

        if Score % 5 == 0:
            ball_dx = ball_dx * 1.3  # Increasing the pixels for the ball movement.
            ball_dy = ball_dy * 1.3
            Speed = Speed + 1

        pen.clear()
        pen.write(f"Score: {Score}    High Score: {HighScore}    Speed: {Speed}",align="center",font=('Monaco',20,"normal"))

        ball_dy = ball_dy * -1
