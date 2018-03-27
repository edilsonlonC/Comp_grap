import pygame
import random
r=lambda: random.randint(0,255)
pygame.init()

def wait ():
    reloj=pygame.time.Clock()
    reloj.tick(30)
def Create_screen ():
    screen=pygame.display.set_mode([600,400])
    return screen

def show_screen():
    pygame.display.flip()

def draw_circle (screen,x,y):
    pygame.draw.circle(screen,[r(),r(),r()],[x,y],5)

def move_circle(screen,x,y):

    #screen.fill([0,0,0])
    draw_circle(screen,x,y)
    #show_screen()
    #wait()
    #pygame.display.flip()

def main ():
    screen=Create_screen()
    puntos=[]

    #x,y=0
    while True:
        for p in puntos:
            if p[1]>=350:
                move_circle(screen,p[0],p[1])
                p[0]+=1
            else:
                move_circle(screen,p[0],p[1])
                p[1]+=1

            show_screen()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                puntos.append(list(event.pos))
        wait()
        screen.fill([0,0,0])




main()
