# setup
import turtle as t
res = 500                                       # resolution (x,y of the window)
sideLength = 100                                # length of sides 
depth = 5
t.setup(res, res)                         
t.setworldcoordinates(0, 9, res, res)
t.tracer(0, 100)
t.speed(0)
t.pu()
t.goto(res/2, res/2)



def triangle(length):
    t.pd()
    #t.color("blue")
    #t.begin_fill()
    for i in range(0,3):
        t.fd(length)
        t.rt(360/3)
    #t.end_fill()



def siepernski(length, depth):
    if (depth == 0):
        t.pd()
        t.stamp()
        t.pu()
        return
    else:
        t.pu()
        for i in range(0, 3):
            t.fd(length)
            siepernski(length/2, depth-1)
            t.backward(length)
            t.lt(120)
            


def octagon(length):
    t.pu()
    t.goto(9*res/4, res/3)
    t.fd(res/4)
    t.rt(20)

    t.pd()
    t.begin_fill()
    for i in range(0, 8):
        t.lt(90)
        #siepernski(length, depth)
        triangle(length)
        t.fd(length)
        t.rt(360/8)
    t.end_fill()



def octagonInnerDesign(length):
    t.pu()
    t.goto(5*res/2, res/2)
    t.fd(res/4)
    t.rt(20)
    t.pd()
    #t.begin_fill()
    for i in range(0, 8):
        t.rt(180)
        triangle(length)
        t.fd(length)
        t.rt(360/8)
    #t.end_fill()



#build our star quilt:
#octagonInnerDesign(sideLength)
octagon(sideLength)
#triangle(sideLength)
#siepernski(sideLength, depth)
t.done()