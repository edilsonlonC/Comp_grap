import pygame
import random
r=lambda: random.randint(0,255)
r2=lambda: random.randint(0,10)
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

def create_plane (screen):
    draw_line(screen,[300,0],[300,600])
    draw_line(screen,[0,300],[600,300])

def main ():
    screen=Create_screen()
    create_plane(screen)
    show()
    t=[]
    while True:
        while len(t)<3:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    t.append(list(event.pos))
        clear(screen)
        pygame.draw.polygon(screen,[r(),r(),r()],t)
        create_plane(screen)
        show()




main()
