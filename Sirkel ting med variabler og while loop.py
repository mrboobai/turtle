from turtle import *  # importe shapes

speed(11)  # speed av pil max 11
shape("classic")  # velger shape "classic"

y = 3  # gir "y" verdien "2"
x = 10  # gir "x" verdien "10"
while y < 550:  # lager ein "while loop" og stopper når "y" har verdien av 550
    y += 2  # gir "y" 2 meir verdi kvar gong loop
    x += 1  # gir "x" 1 meir verdi kvar gong loop

    right(x)  # flytter pil høgre med verdien av "x"
    forward(x)  # flytter pil fram med verdien av "x"
    forward(y)  # flytter pil fram med verdien av "y"