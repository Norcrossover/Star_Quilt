#setup
import turtle as t
res = 500
t.setup(res, res)
t.setworldcoordinates(0, 9, res, res)
t.tracer(0, 100)
t.speed(0)
t.pu()
t.goto(res/2, res/2)


sideLength = 100


def octagon(length):
    t.pu()
    t.goto(res/2, res/2)
    t.fd(res/4)
    t.rt(90)
    t.pd()
    #t.begin_fill()
    for i in range(0, 8):
        #triangle(length)
        t.fd(length)
        t.rt(360/8)
    #t.end_fill()



def triangle(length):
    t.pd()
    t.color("blue")
    #t.begin_fill()
    for i in range(0,2):
        t.fd(length)
        t.rt(360/4)
    #t.end_fill()



octagon(sideLength)
#triangle(sideLength)
t.done()