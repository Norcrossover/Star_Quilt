# setup
import turtle as t
res = 500                                       # resolution (x,y of the window)
sideLength = 50                                # length of sides 
depth = 5
t.setup(res, res)                         
t.setworldcoordinates(0, 9, res, res)
t.tracer(0, 100)
t.speed(0)
t.pu()
t.goto(res/2, res/2)



def triangle(length, color):
    t.pd()
    #t.color("blue")
    #t.begin_fill()
    for i in range(0,3):
        t.fd(length)
        t.rt(360/3)
    siepernski(length, depth, color)
    
    #t.end_fill()



def siepernski(length, depth, color):
    t.color(color)
    if (depth == 0):
        t.pd()
        t.stamp()
        t.pu()
        return
    else:
        t.pu()
        for i in range(0, 3):
            t.fd(length)
            siepernski(length/2, depth-1, color)
            t.backward(length)
            t.lt(120)
            


def octagon(length, colorOne, colorTwo):
    t.pu()
    t.goto(res/2, res/2)
    t.fd(res/4)
    #t.rt(20)
    t.pd()
    #t.begin_fill()
    for i in range(0, 8):
        t.lt(90)
        siepernski(length, depth, colorTwo)
        #triangle(length)
        t.fd(length)
        t.rt(360/8)
    #t.end_fill()



def octagonInnerDesign(length, color):
    t.color(color)
    t.pu()
    t.goto(res/2, res/2)
    t.fd(res/4)
    t.rt(20)
    t.pd()
    #t.begin_fill()
    for i in range(0, 8):
        t.rt(180)
        triangle(length, color)
        t.fd(length)
        t.rt(360/8)
    #t.end_fill()



#build our star quilt:
octagon(sideLength, "light blue", "pink")
#octagonInnerDesign(sideLength/2, "red")

t.goto(res/2, res/2)
t.lt(90)
#siepernski(sideLength, depth)
#triangle(sideLength, color)
t.done()