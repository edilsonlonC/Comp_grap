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
def draw_line (screen,pi,pf):
    pygame.display-draw_line(screen,[r(),r(),r()],pi,pf)


def main ():
    screen=Create_screen()
    
