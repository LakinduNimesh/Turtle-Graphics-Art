from turtle import *
bgcolor("#000")
speed(0)
pensize(3)
for i in range(9):
  color("#ff0101")
  left(60)
  circle(-18, 200)
  color("#ff0101", "#e8b60f")
  r = 100
  for j in range(12):
    begin_fill()
    circle(r-11*j, 90)
    end_fill()
  left(180)
  penup()
  goto(0,0)
  pendown()
  hideturtle()
done()