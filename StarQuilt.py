# setup
import turtle as t
res = 500                                       # resolution (x,y of the window)
sideLength = res/5                                # length of sides 
depth = 5
sides = 6
t.setup(res, res)                         
t.setworldcoordinates(0, 9, res, res)
t.tracer(0, 100)
t.speed(0)
t.pu()
t.goto(res/2, res/2)



def octagon(sides, length, colorOne, colorTwo):
    t.pu() 
    #t.goto(res/2, res/2)
    #moves cursor to the bottom left of the screen to start drawing the shape
    point = (res/2-length+10),(res/2-50)
    t.goto(point)
    t.lt(90)
    t.fd(res/4)
    t.pd()
    #t.rt(90)
    #t.fd(length/2)
    count = 1
    for i in range(0, sides):
        #print(count)
        t.color(colorOne)
        
        #if (count != 4 or count != 8):
            #siepernski(length/4, 3, colorOne)
        triangle(length, colorOne)
        
        t.rt(360/6)
        t.fd(length)
        #count += 1

    #t.fd(length/2)
    t.pu()
    #t.rt(20)
    #t.pd()



def triangle(length, color):
    
    t.pd()
    theta = 0
    t.lt(theta)
    #t.color("blue")
    #t.begin_fill()
    point = (0, 0)
    heading = 0
    for i in range(0,3):
        if (i == 0):
            point = t.pos()
            heading = t.heading()
        t.fd(length)
        t.rt(360/3)
    print(point)
    print(heading)
    t.rt(30)
    siepernski(length/4, 3, color)
    t.pu()
    t.fd(length/2)
    t.rt(90)
    # one corner of the serpinski triangle is aequal to the actual triangle i want
    # go to the first points positiion ((x + length), 0)
    
    t.lt(30)
    #t.fd(length/2)
    t.rt(theta)
    t.goto(point)
    t.seth(heading)
    #t.lt(45)
    t.pd()
    
''' #for testing
    t.begin_fill()
    t.circle(length/8)
    t.end_fill()
    '''


 
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



def innerDesign(sides, length, color):
    t.color(color)
    t.pu()
    t.goto(res/2, res/2)
    t.fd(res/4)
    t.rt(20)
    t.pd()
    #t.begin_fill()
    for i in range(0, sides):
        t.rt(180)
        '''
        for j in range(0,3):
            t.fd(length)
            t.rt(360/sides)
            '''
        t.fd(length)
        t.rt(360/sides)
    #t.end_fill()



#build our star quilt:
#octagon(sides, sideLength, "black", "white")
#innerDesign(8, sideLength, "black")

t.goto(res/2, res/2)
t.rt(60)
#siepernski(sideLength/4, 3, "blue")
triangle(sideLength, "black")
t.done()