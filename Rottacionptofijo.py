import pygame
from math import *
import random
r=lambda: random.randint(0,255)
r2=lambda: random.randint(1,10)

pygame.init()



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
def fixed_point (x,pfx,y,pfy):
    xp=x-pfx
    yp=y-pfy
    return xp,yp
def draw_polygon (screen,point):
     pygame.draw.polygon(screen,[r(),r(),r()],point,1)
def rotation (point,A):
     xp=point[0]*cos(A)-point[1]*sin(A)
     yp=point[0]*sin(A)+point[1]*cos(A)
     return xp,yp
def first_position (x,pfx,y,pfy):
    xp=x+pfx
    yp=y+pfy
    return xp,yp
def polares (r,Theta):
    x=r*cos(Theta)
    y=r*sin(Theta)
    return x,y
def transformation (cx,cy,x,y):
        xp=cx+x
        yp=cy-y
        return xp,yp
def Cartesian(cx,cy,xp,yp):
    x=xp-cx
    y=cy-yp
    return x,y

def Create_plane (screen,rect_X,rect_y):
    draw_line(screen,rect_X[0],rect_X[1])
    draw_line(screen,rect_y[0],rect_y[1])

def Rose(a,n,Theta):
    r=a*cos(Theta*n)
    return r

def wait (n):
    reloj=pygame.time.Clock()
    reloj.tick(n)

def main ():
    screen=Create_screen([600,600])
    Tr=[[20,10],[50,10],[50,30]]
    Tp=[]
    Thetha=0
    for T in Tr:
        Tp.append(transformation(300,300,T[0],T[1]))
    close=False
    #for i in range (len(Tr)):
     #   Tr[i]=puntofijo(Tr[i][0],20,Tr[i][1],10)
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True

        while Thetha<=360:

            wait(20)
            for i in range (len(Tr)):
                Tr[i]=fixed_point(Tr[i][0],20,Tr[i][1],10)
            for i in range (len(Tr)):
                Tr[i]=rotation(Tr[i],radians(Thetha))
            for i in range (0,len(Tr)):
                Tr[i]=first_position(Tr[i][0],20,Tr[i][1],10)
            for i in range(len(Tr)):
                Tp[i]=transformation(300,300,Tr[i][0],Tr[i][1])
            Thetha+=1


            Create_plane(screen,[[300,0],[300,600]],[[0,300],[600,300]])
            draw_polygon(screen,Tp)
            show()
            clear(screen)
            










main()
