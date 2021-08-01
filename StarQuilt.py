# setup
import turtle as t
res = 500                                       # resolution (x,y of the window)
sideLength = res/5                                # length of sides 
depth = 5
sides = 6
primaryColor = "blue"
secondaryColor = "red"
stitchColor = "black"
backgroundColor = "white"
t.setup(res, res)                         
t.setworldcoordinates(0, 9, res, res)
t.tracer(0, 100)
t.speed(0)
t.pu()
t.goto(res/2, res/2)



def getColors(primaryColor: str, secondaryColor: str) -> None:
    stitchColor     = input("Enter the name of the stitching color: ")
    backgroundColor = input("Enter the name of the background color: ")
    primaryColor    = input("Enter the name of the primary color: ")
    secondaryColor  = input("Enter the name of the secondary color: ")
    
def starQuilt(sides: int, length: int, primaryColor: str, secondaryColor: str) -> None:
    t.pu() 
    #moves cursor to the bottom left of the screen to start drawing the shape
    point = (res/2-length+10),(res/2-50)
    t.goto(point)
    t.lt(90)
    t.fd(res/4)
    for i in range(0, sides):
        t.color(secondaryColor)
        triangle(length, primaryColor, secondaryColor)
        t.rt(360/6)
        t.fd(length)
    hexagon(secondaryColor, point, sideLength, sides)
    innerDesign(8, length/2+14, primaryColor, secondaryColor)
    


def triangle(length: int, primaryColor: str, secondaryColor: str) -> None:
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
    t.color(primaryColor)
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
    siepernski(length/4+7, 3, secondaryColor)
    t.pu()
    t.fd(length/2)
    t.rt(90)    
    t.goto(a)
    t.seth(heading1)    
    

 
def siepernski(length: int, depth: int, color: str) -> None:
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


def stitchPathing(res: int) -> None:
    traversed = 0
    t.pd()
    while (traversed < res):
        t.seth(0)
        #pos_one = t.xcor()
        t.lt(30)
        t.fd(10)
        t.rt(60)
        t.fd(10)
        #pos_two = t.xcor()
        # the last stitch was not going all the way, so I found a value that allowed for it to work
        traversed += (12)

def background(res: int, backgroundColor: str, stitchColor: str) -> None:
    # need space in between each "stitch
    # there will be 8 stitches across, but may change depending on how it looks
    stitches = 8
    space = res/stitches
    t.bgcolor(backgroundColor)
    t.goto(0,0)
    t.color(stitchColor)
    #t.begin_fill()
    for i in range(0,stitches):
        t.pu()
        t.goto(0, i*space)
        if (i!=0 and i!=stitches):
            stitchPathing(res)
    #t.end_fill()




def innerDesign(sides: int, length: int, primaryColor: str, secondaryColor: str) -> None:
    t.color(secondaryColor)
    t.pu()
    t.goto(res/2-4,res/2+50)
    t.fd(length)
    t.rt(90)
    t.pd()
    t.begin_fill()
    for i in range(0, sides):
        t.rt(360/sides)
        #t.begin_fill()
        t.color(primaryColor)
        for j in range(0,3):
            t.fd(length)
            t.rt(360/sides)
        #t.end_fill()
        t.fd(length)
        t.rt(360/sides)
    t.end_fill()



def hexagon(color: str, startingPoint: str, length: int, sides: int) -> None:
    t.pu()
    t.goto(startingPoint)
    t.begin_fill()
    t.fd(res/4)
    for i in range(0, sides):
        t.color(secondaryColor)
        t.rt(360/6)
        t.fd(length)
    t.end_fill()



#build our star quilt:
def main():
    background(res, backgroundColor, stitchColor)
    '''
    getColors(primaryColor, secondaryColor)
    starQuilt(sides, sideLength, primaryColor, secondaryColor)
    '''
    t.done()

#two underscores it seems XD
if __name__ == "__main__":
    main()