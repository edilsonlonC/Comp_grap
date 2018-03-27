import pygame
from math import *
if __name__ == '__main__':
    def fun (x):
        return 0.5*x
    # tansformation function
    def r2ar2 (cx,cy,x,y):
        xp=cx+x
        yp=cy-y
        return xp,yp
    xp,yp=r2ar2(200,300,200,100)
    xp1,yp1=r2ar2(200,300,-150,50)
    pygame.init()
    #print "probando --"
    screen=pygame.display.set_mode([600,400])

    close = False
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            #plano
            pygame.draw.line(screen,[0,155,0],[200,0],[200,400])
            pygame.draw.line(screen,[0,155,0],[0,300],[600,300])
            x=0
            while  x<600:
                y=fun(x)
                x1,y1=r2ar2(200,300,x,y)
                pygame.draw.circle(screen,[255,0,0],[int(x1),int(y1)],1)
                x+=1
                pygame.display.flip()
