import pygame
import random
from math import*
r=lambda: random.randint(0,255)
r2=lambda: random.randint(1,5)

pygame.init()

def transformation (cx,cy,x,y):
        xp=cx+x
        yp=cy-y
        return xp,yp
def cartesianas(cx,cy,xp,yp):
    x=xp-cx
    y=cy-yp
    return x,y

def Create_screen ():
    screen=pygame.display.set_mode([600,600])
    return screen

def draw_line (screen,p_i,p_f):
    pygame.draw.line(screen,[r(),r(),r()],p_i,p_f)
def draw_point (screen,center):
    pygame.draw.circle(screen,[r(),r(),r()],center,r2())

def show ():
    pygame.display.flip()
def clear (screen):
    screen.fill([0,0,0])


def escalamiento (point,s):
    xp=point[0]*s[0]
    yp=point[1]*s[0]
    return xp,yp
def draw_polygon (screen,point):
    pygame.draw.polygon(screen,[r(),r(),r()],point,1)
def rotacion (point,An):
    A=radians(90)
    xp=point[0]*cos(A)-point[1]*sin(A)
    yp=point[0]*sin(A)+point[1]*cos(A)
    return xp,yp

def main ():
    screen=Create_screen()
    draw_line(screen,[300,0],[300,600])
    draw_line(screen,[0,300],[600,300])
    show()

    while True:
            i=0
            xp1,yp1=transformation(300,300,30,50)
            xp2,yp2=transformation(300,300,70,80)
            xp3,yp3=transformation(300,300,100,200)
            pygame.draw.polygon(screen,[0,0,200],[[xp1,yp1],[xp2,yp2],[xp3,yp3]],1)
            xp1,yp1=cartesianas(300,300,xp1,yp1)
            xp2,yp2=cartesianas(300,300,xp2,yp2)
            xp3,yp3=cartesianas(300,300,xp3,yp3)
            xpp1,ypp1=rotacion([xp1,yp1],i)
            xpp2,ypp2=rotacion([xp2,yp2],i)
            xpp3,ypp3=rotacion([xp3,yp3],i)
            xpp1,ypp1=transformation(300,300,xpp1,ypp1)
            xpp2,ypp2=transformation(300,300,xpp2,ypp2)
            xpp3,ypp3=transformation(300,300,xpp3,ypp3)
            i+=10
            print xpp1,xpp1,ypp1,xpp2,ypp2,xpp3,ypp3
            draw_polygon(screen,[[xpp1,ypp1],[xpp2,ypp2],[xpp3,ypp3]])
            show()

main()
