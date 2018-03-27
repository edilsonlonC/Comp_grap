import pygame
import random
r=lambda:random.randint(0,255)
r2=lambda:random.randint(1,100)
if __name__ == '__main__':
    # tansformation function
    def r2ar2 (cx,cy,x,y):
        xp=cx+x
        yp=cy-y
        return xp,yp
    # return values x and y
    def coorcart (cx,cy,xp,yp):
        x=xp-cx
        y=cy-yp
        return x,y
    xp,yp=r2ar2(200,300,200,100)
    xp1,yp1=r2ar2(200,300,-150,50)
    pygame.init()
    #print "probando --"
    screen=pygame.display.set_mode([600,400])

    close = False
    reloj=pygame.time.Clock()
    z=0
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            #plano

            #rectas
            #pygame.draw.line(screen,[0,255,0],[200,300],[xp,yp])
            #pygame.draw.line(screen,[0,255,0],[200,300],[xp1,yp1])
            #pygame.draw.circle(screen,[255,0,0],[200,300],25,1)
            #if event.type==pygame.MOUSEBUTTONDOWN:
            while z<600:
                screen.fill([0,0,0])
                xp,yp=event.pos
                pygame.draw.line(screen,[0,255,0],[200,0],[200,400])
                pygame.draw.line(screen,[0,255,0],[0,300],[600,300])
                pygame.draw.circle(screen,[r(),r(),r()],[xp,z],5,1)
                z+=1
                x,y=coorcart(200,300,xp,yp)
                print 'Coordenadas cartesianas',x,y
                print  'Coordenadas de pantalla',xp,yp
                pygame.display.flip()
                reloj.tick(10)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    screen.fill([0,0,0])
                    xp,yp=event.pos
                    pygame.draw.line(screen,[0,255,0],[200,0],[200,400])
                    pygame.draw.line(screen,[0,255,0],[0,300],[600,300])
                    pygame.draw.circle(screen,[r(),r(),r()],[z,yp],5,1)

                    display.flip()

                    reloj.tick(10)


            pygame.display.flip()
