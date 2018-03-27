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
def rotation (point,A):
     xp=point[0]*cos(A)-point[1]*sin(A)
     yp=point[0]*sin(A)+point[1]*cos(A)
     return xp,yp


def Create_plane (screen,rect_X,rect_y):
    draw_line(screen,rect_X[0],rect_X[1])
    draw_line(screen,rect_y[0],rect_y[1])

def Rose(a,n,Thetha):
    r=a*cos(Thetha*n)
    return r
def fixed_point (x,pfx,y,pfy):
    xp=x-pfx
    yp=y-pfy
    return xp,yp
def wait (n):
    reloj=pygame.time.Clock()
    reloj.tick(n)

def main ():
    screen=Create_screen([800,800])
    show()
    close=False
    coorcart=[[30,50],[40,30],[10,20]]
    triangle=[]
    i=0




    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                coor_plane=list(event.pos)
                Create_plane(screen,[[coor_plane[0],0],[coor_plane[0],800]],[[0,coor_plane[1]],[800,coor_plane[1]]])
                for i in range (0,len(coorcart)):
                    coorcart[i]=transformation(coor_plane[0],coor_plane[1],coorcart[i][0],coorcart[i][1])
                draw_polygon(screen,coorcart)
                for i in range (0,len(coorcart)):
                    coorcart[i]=cartesianas(coor_plane[0],coor_plane[1],coorcart[i][0],coorcart[i][1])
                for i in range (len(coorcart)):
                    coorcart[i]=fixed_point(coorcart[i][0],20,coorcart[i][1],10)
                for i in range (len(coorcart)):
                    coorcart[i]=rotation(coorcart[i],radians(30))
                for i in range (0,len(coorcart)):
                    coorcart[i]=first_position(coorcart[i][0],20,coorcart[i][1],10)
                for i in range(len(coorcart)):
                    coorcart[i]=transformation(300,300,coorcart[i][0],coorcart[i][1])
        draw_polygon(screen,coorcart)
        show()







main()
