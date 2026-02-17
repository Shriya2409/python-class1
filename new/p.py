# full_pikachu.py
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Full Pikachu with Turtle")

t = turtle.Turtle()
t.speed(10)

# Function to draw filled circle
def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.penup()

# Function to draw filled polygon
def draw_polygon(color, points):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()
    t.penup()

# ------------------
# Head
# ------------------
draw_circle("#FFD700", 0, 0, 100)  # Yellow face

# ------------------
# Eyes
# ------------------
draw_circle("black", -35, 50, 15)  # Left eye
draw_circle("black", 35, 50, 15)   # Right eye
draw_circle("white", -35, 55, 7)   # Left sparkle
draw_circle("white", 35, 55, 7)    # Right sparkle

# ------------------
# Cheeks
# ------------------
draw_circle("red", -60, 0, 20)   # Left cheek
draw_circle("red", 60, 0, 20)    # Right cheek

# ------------------
# Mouth
# ------------------
t.goto(-20, -20)
t.pendown()
t.right(90)
t.circle(20, 180)  # Smiling mouth
t.penup()
t.goto(0, -20)
t.pendown()
t.right(180)
t.circle(20, 180)
t.penup()

# ------------------
# Ears
# ------------------
draw_polygon("black", [(-70, 120), (-90, 200), (-50, 150)])
draw_polygon("black", [(70, 120), (90, 200), (50, 150)])

# ------------------
# Body
# ------------------
draw_circle("#FFD700", 0, -100, 70)  # Body

# Arms
draw_circle("#FFD700", -90, -60, 25)  # Left arm
draw_circle("#FFD700", 90, -60, 25)   # Right arm

# Feet
draw_circle("#FFD700", -40, -170, 25)  # Left foot
draw_circle("#FFD700", 40, -170, 25)   # Right foot

# Tail
draw_polygon("#FFD700", [(70, -60), (150, 0), (120, -30), (140, 50), (70, 20)])

# Hide turtle
t.hideturtle()

turtle.done()

