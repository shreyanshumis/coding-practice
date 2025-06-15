from turtle import *
color('orange', 'red')
pensize(3)
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()