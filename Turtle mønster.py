import turtle

circles = 1
t = turtle
increment = 1
t.speed(0)

t.tracer(False)

while True:
    t.shape("turtle")

    t.penup()
    t.goto(0, -400)
    t.pendown()

    turtle.pencolor("red")
    t.circle(circles)
    circles += increment
    
    turtle.pencolor("orange")
    t.circle(circles)
    circles += increment
    
    turtle.pencolor("yellow")
    t.circle(circles)
    circles += increment
    
    turtle.pencolor("green")
    t.circle(circles)
    circles += increment
    
    turtle.pencolor("blue")
    t.circle(circles)
    circles += increment
    
    turtle.pencolor("indigo")
    t.circle(circles)
    circles += increment
    
    turtle.pencolor("violet")
    t.circle(circles)
    circles += increment
    
    turtle.update()