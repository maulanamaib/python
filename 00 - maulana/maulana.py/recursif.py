# 2
import turtle as x
x.speed(5)
def square(line,level):
    color = ['blue' , 'red' , 'green' , 'pink']
    screen = level % 4
    if level == 0 :
        x.begin_fill()
        x.color('black' , color[screen])
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.end_fill()
    else :
        x.begin_fill()
        x.color('black' , color[screen])
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.forward(line)
        x.right(90)
        x.end_fill()
        x.forward(line/2)
        x.right(90)
        x.forward(line/2)
        x.right(180)
        square(line/2 , level-1)
        
square(100 , 3)
x.done()