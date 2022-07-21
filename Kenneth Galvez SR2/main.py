from gl import Render, color, V2

width = 400
height = 80


rend = Render()
rend.glCreateWindow(width, height)

def drawPoli(poligono, clr = None):
    for i in range(len(poligono)):
        rend.glLine(poligono[i],
                    poligono[ (i + 1) % len(poligono)],
                    clr)

#Triangulo
pol1 = [V2(20, 10), V2(50, 40), V2(80, 10), V2(19, 11)]

#Cuadrado
pol2 = [V2(90, 10), V2(91, 40), V2(150, 41)] 
pol3 = [V2(155, 10), V2(90, 11), V2(150, 40)]

#Trapecio
pol4 = [V2(170, 10), V2(189.99, 40), V2(190, 11)]
pol5 = [V2(190, 10), V2(191, 40), V2(230, 41)] 
pol6 = [V2(235, 10), V2(190, 11), V2(230, 40)]
pol7 = [V2(235, 10), V2(231, 40), V2(255, 11)]

#Rombo
pol8 = [V2(270, 30), V2(290, 50), V2(310, 30)]
pol9 = [V2(270, 30), V2(290, 10), V2(310, 30)]

#Deltoide
pol10 = [V2(330, 40), V2(345, 60), V2(360, 40)]
pol11 = [V2(330, 40), V2(345, 5), V2(360, 40)]

drawPoli(pol1, color(1,0,0))
drawPoli(pol2, color(1,0,0))
drawPoli(pol3, color(1,0,0))
drawPoli(pol4, color(1,0,0))
drawPoli(pol5, color(1,0,0))
drawPoli(pol6, color(1,0,0))
drawPoli(pol7, color(1,0,0))
drawPoli(pol8, color(1,0,0))
drawPoli(pol9, color(1,0,0))
drawPoli(pol10, color(1,0,0))
drawPoli(pol11, color(1,0,0))

rend.glFinish('output.bmp')