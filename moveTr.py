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


def Create_plane (screen,rect_X,rect_y):
    draw_line(screen,rect_X[0],rect_X[1])
    draw_line(screen,rect_y[0],rect_y[1])

def main ():
    screen=Create_screen([600,600])
    show()
    close=False
    points=[]
    relog=pygame.tick()
    while not close:
        clear(screen)
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                close=True
            if len(points) < 3:
                if events.type==pygame.MOUSEBUTTONDOWN:
                    points.append(list (events.pos))
            
        if len(points)==3:
            relog.tick(20)
            draw_polygon(screen,points)
            for p in points:
                p[0]+=1
                if p[0]==600:
                    points=[]

        Create_plane(screen,[[300,0],[300,600]],[[0,300],[600,300]])
        show()
       
        



main()
