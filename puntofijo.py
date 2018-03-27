import pygame
from math import *
import random
r=lambda: random.randint(0,255)
r2=lambda: random.randint(1,10)

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
    pygame.draw.line(screen,[r(),r(),r()],p_i,p_f,2)

def draw_point (screen,center):
    pygame.draw.circle(screen,[r(),r(),r()],center,2)

def show ():
    pygame.display.flip()
def clear (screen):
    screen.fill([0,0,0])



def escalamiento (point,s):
     xp=point[0]*s[0]
     yp=point[1]*s[1]
     return xp,yp
def puntofijo (x,pfx,y,pfy):
    xp=x-pfx
    yp=y-pfy
    return xp,yp
def draw_polygon (screen,point):
     pygame.draw.polygon(screen,[r(),r(),r()],point,1)
def rotacion (point,A):
     xp=point[0]*cos(A)-point[1]*sin(A)
     yp=point[0]*sin(A)+point[1]*cos(A)
     return xp,yp
def first_position (x,pfx,y,pfy):
    xp=x+pfx
    yp=y+pfy
    return xp,yp
def polares (r,Thetha):
    x=r*cos(Thetha)
    y=r*sin(Thetha)
    return x,y


def Create_plane (screen,rect_X,rect_y):
    draw_line(screen,rect_X[0],rect_X[1])
    draw_line(screen,rect_y[0],rect_y[1])

def Rose(a,n,Thetha):
    r=a*cos(Thetha*n)
    return r

def wait (n):
    reloj=pygame.time.Clock()
    reloj.tick(n)

def main ():
    close=False
    screen=Create_screen([600,600])
    Create_plane(screen,[[300,0],[300,600]],[[0,300],[600,300]])
    Tr=[[20,10],[50,10],[50,30]]
    Tp=[]
    for T in Tr:
        Tp.append(transformation(300,300,T[0],T[1]))
    draw_polygon(screen,Tp)
    show()
    for i in range(0,len(Tr)):
        Tr[i]=puntofijo(Tr[i][0],20,Tr[i][1],10)
    for i in range(0,len(Tr)):
        Tp[i]=transformation(300,300,Tr[i][0],Tr[i][1])
    draw_polygon(screen,Tp)
    show()
    for i in range(0,len(Tr)):
        Tr[i]=escalamiento(Tr[i],[2,2])
    for i in range(0,len(Tr)):
        Tp[i]=transformation(300,300,Tr[i][0],Tr[i][1])
    for i in range(0,len(Tr)):
        Tr[i]=first_position(Tr[i][0],20,Tr[i][1],10)
    for i in range(0,len(Tr)):
        Tp[i]=transformation(300,300,Tr[i][0],Tr[i][1])
    draw_polygon(screen,Tp)
    show()
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True



main()
