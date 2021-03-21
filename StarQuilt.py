# setup
import turtle as t
res = 500                                       # resolution (x,y of the window)
sideLength = res/5                                # length of sides 
depth = 5
sides = 6
colorOne = "black"
colorTwo = "white"
t.setup(res, res)                         
t.setworldcoordinates(0, 9, res, res)
t.tracer(0, 100)
t.speed(0)
t.pu()
t.goto(res/2, res/2)



def octagon(sides, length, colorOne, colorTwo):
    t.pu() 
    #moves cursor to the bottom left of the screen to start drawing the shape
    point = (res/2-length+10),(res/2-50)
    t.goto(point)
    t.lt(90)
    t.fd(res/4)
    t.pd()
    t.color(colorTwo)
    t.begin_fill()
    for i in range(0, sides):
        t.color(colorOne)
        triangle(length, colorOne, colorTwo)
        t.rt(360/6)
        t.fd(length)
    t.end_fill()
    t.fd(length/2)
    t.pu()
    t.goto(res/2,res/2)
    #innerDesign(8, length/2+14, colorOne, point)
    



def triangle(length, colorOne, colorTwo):
    # setup variables needed
    a = (0, 0)
    b = (0, 0)
    c = (0, 0)
    heading1 = 0
    heading2 = 0
    heading3 = 0
    o = (0, 0)
    ox = 0
    oy = 0
    t.pd()
    t.color(colorOne)
    t.begin_fill()
    for i in range(0,3):
        t.pd()
        # need to get the point and heading when the triangle function is called
        if (i == 0):
            a = t.pos()
            heading1 = t.heading()
        elif (i == 1):
            b = t.pos()
            heading2 = t.heading()
        elif (i == 2):
            t.pu()
            c = t.pos()
            heading3 = t.heading()
        #move forward length 
        t.fd(length)
        #then right turn 
        t.rt(360/3)
    t.end_fill()
    #use the formula to find the x and y coordinate of o
    ox = (a[0]+b[0]+c[0])/3
    oy = (a[1]+b[1]+c[1])/3
    o = (ox, oy)
    t.rt(90)
    t.pu()
    t.goto(o)
    t.pd()
    #draw the siepernski triangle
    siepernski(length/4+7, 3, colorTwo)
    t.pu()
    t.fd(length/2)
    t.rt(90)    
    t.goto(a)
    t.seth(heading1)    
    



 
def siepernski(length, depth, color):
    # draw the triangle with the given color
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



def innerDesign(sides, length, colorOne, colorTwo, startingPoint):
    t.color(color)
    t.pu()
    t.goto(res/2-4,res/2+50)
    t.fd(length)
    t.rt(90)
    t.pd()
    t.begin_fill()
    for i in range(0, sides):
        t.rt(360/sides)
        for j in range(0,3):
            t.fd(length)
            t.rt(360/sides)
        t.fd(length)
        t.rt(360/sides)
    t.end_fill()



#build our star quilt:
#octagon(sides, sideLength, "blue", "pink")
#triangle(sideLength, "black", "white")
innerDesign(8, sideLength/2, colorOne, colorTwo, (res/2,res/2))
t.done()