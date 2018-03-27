import pygame
pygame.init()


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

def Create_screen (size):
    screen=pygame.display.set_mode(size)
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

def move_up (limit,screen,y):
    aux=0
    if limit[1][1] > limit[0][1]:
        aux=limit[0][1]
        y=limit[1][1]
    else:
        aux=limit[1][1]
        y=limit[0][1]
    while y>aux:
        clear(screen)
        draw_line(screen,[0,limit[0][1]],[600,limit[0][1]])
        draw_line(screen,[0,limit[1][1]],[600,limit[1][1]])
        draw_line(screen,[0,y],[600,y])
        show()
        y-=1
def Create_plane (screen,rect_X,rect_y):
    draw_line(screen,rect_X[0],rect_X[1])
    draw_line(screen,rect_y[0],rect_y[1])
def main ():
    screen=Create_screen([600,600])
    show()
    close=False
    points=[]
    limit=[]
    x,y=0,0
    contador=0
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                if (contador  != 2 ):
                    x,y=event.pos
                    limit.append([x,y])
                    draw_line(screen,[0,y],[600,y])
                    show()
                    contador+=1
        if contador==2 :
 #           clear(screen
                move_up(limit,screen,y)

                




main()
