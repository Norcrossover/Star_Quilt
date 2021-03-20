# setup
import turtle as t
res = 500                                       # resolution (x,y of the window)
sideLength = res/5                                # length of sides 
depth = 5
sides = 6
t.setup(res, res)                         
t.setworldcoordinates(0, 9, res, res)
'''
t.tracer(0, 100)
t.speed(0)
'''
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
    for i in range(0, sides):
        t.color(colorOne)
        triangle(length, colorOne)
        t.rt(360/6)
        t.fd(length)
    t.fd(length/2)
    t.pu()
    



def triangle(length, color):
    
    t.pd()
    theta = 0
    t.lt(theta)
    a = (0, 0)
    b = (0, 0)
    c = (0, 0)
    o = (0, 0)
    ox = 0
    oy = 0
    heading1 = 0
    heading2 = 0
    heading3 = 0
    for i in range(0,3):
        #need to get the point and heading when the triangle function is called
        if (i == 0):
            a = t.pos()
            heading1 = t.heading()
        elif (i == 1):
            b = t.pos()
            heading2 = t.heading()
        elif (i == 2):
            c = t.pos()
            heading3 = t.heading()
        t.fd(length)
        t.rt(360/3)

    # find the center of the triangle each time
    ox = (a[0]+b[0]+c[0])/3
    oy = (a[1]+b[1]+c[1])/3
    o = (ox, oy)
    '''
    print("Point 1:")
    print(a)
    print(heading1)
    print("Point 2:")
    print(b)
    print(heading2)
    print("Point 3:")
    print(c)
    print(heading3)
    '''
    #t.goto(point)
    #t.seth(heading) 
    t.rt(90)
    #need to go to the center of the triangle b having the point x and y = 0
    t.pu()
    #add 5 to point 1 if the outcome is not as desired
    t.goto(o)
    t.pd()
    siepernski(length/4, 3, color)
    t.pu()
    t.fd(length/2)
    t.rt(90)
    # one corner of the serpinski triangle is aequal to the actual triangle i want
    # go to the first points positiion ((x + length), 0)
    t.rt(theta)
    
    t.goto(a)
    t.seth(heading1)    
    



 
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
octagon(sides, sideLength, "black", "white")
#innerDesign(8, sideLength, "black")
t.goto(res/2, res/2)
t.rt(60)
#triangle(sideLength, "black")
t.done()