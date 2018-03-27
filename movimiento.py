import pygame
import random
r=lambda: random.randint(0,255)
r2=lambda: random.randint(0,1000)
pygame.init()

def wait ():
    reloj=pygame.time.Clock()
    reloj.tick(10000)
def Create_screen ():
    screen=pygame.display.set_mode([600,600])
    return screen

def show_screen():
    pygame.display.flip()

def draw_circle (screen,x,y):
    pygame.draw.circle(screen,[r(),r(),r()],[x,y],100)

def move_circle(screen,x,y):

    #screen.fill([0,0,0])
    draw_circle(screen,x,y)
    show_screen()
    #wait()
    #pygame.display.flip()

def main ():
    screen=Create_screen()
    show_screen()
    x,y=0,0
    while True:

        while x<600:
            move_circle(screen,x,y)
            x+=1
            y+=1
            wait()
            #screen.fill([0,0,0])
        while y>0:
            move_circle(screen,x,y)
        #    x+=1
            y-=1
            wait()
            #screen.fill([0,0,0])
        while x>0:
            move_circle(screen,x,y)
            x-=1
            y+=1
            wait()
            #screen.fill([0,0,0])
        while y>0:
            move_circle(screen,x,y)
            y-=1
            wait()
            #screen.fill([0,0,0])






    #show_screen()




main()
