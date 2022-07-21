from distutils.ccompiler import gen_lib_options
import struct
from collections import namedtuple

V2 = namedtuple('Point2D', ['x', 'y'])

def char(c):
    # 1 byte length
    return struct.pack('=c', c.encode('ascii'))


def word(w):
    # 2 bytes length
    return struct.pack('=h', w)


def dword(d):
    # 3 bytes length
    return struct.pack('=l', d)


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


class Render(object):
    # Constructor
    def __init__(self):
        self.viewPortX = 0
        self.viewPortY = 0
        self.height = 0
        self.width = 0
        self.clearColor = color(0, 0, 0)
        self.currColor = color(1, 1, 1)
       
        self.glViewport(0,0,self.width, self.height)
        
        self.glClear()

        

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()

      
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, b, g)
        self.glClear()

    def glColor(self, r, g, b):
        self.currColor = color(r, g, b)

    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)]
                       for x in range(self.width)]

    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPoint(x,y,clr)

    def glViewport(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height
    
    def glPoint(self, x, y, clr=None):
        if (0 <= x < self.width) and (0 < + y < self.height):
            self.pixels[x][y] = clr or self.currColor

    def glPoint_vp(self, ndcX, ndcY, clr=None):
        if ndcX < -1 or ndcX > 1 or ndcY < -1 or ndcY > 1 :
            return 


        x = (ndcX + 1) * (self.vpWidth / 2) + self.vpX
        y = (ndcY + 1) * (self.vpHeight / 2) + self.vpY

        x = int(x)
        y = int(y)

        self.glPoint(x,y,clr)
    
    def glLine(self, v0, v1, clr=None):
        # Bresenham line algorithm
        #Y = m * x + b
        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        if x0 == x1 or y0 == y1:
            self.glPoint(x0,y0,clr) 
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx 

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0) 
        dx = abs(x1 - x0)
    
        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0 

        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(y,x,clr)
            else:
                self.glPoint(x,y,clr)

            offset += m 

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1
                

    # Función para crear la imagen
    def glFinish(self, filename):
        with open(filename, 'wb') as file:
            # Header
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))

            # file size
            file.write(dword(14 + 40 + self.height * self.width * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # Info Header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
            file.close()

    