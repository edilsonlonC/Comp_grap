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
    pygame.draw.line(screen,[r(),r(),r()],p_i,p_f,r2())
def draw_point (screen,center):
    pygame.draw.circle(screen,[r(),r(),r()],center,r2())

def show ():
    pygame.display.flip()

def move_left (screen,center):
    x,y=cartesianas(300,200,center[0],center[1])
    limit1= -1*x
    print x,limit1
    while x>limit1 :
        screen.fill([0,0,0])
        draw_line(screen,[300,100],[300,300])
        draw_point(screen,center)
        draw_line(screen,[300,100],center)
        draw_line(screen,[300,300],center)
        center[0]-=1
        x-=1
        show()
def move_right (screen,center):
    x,y=cartesianas(300,200,center[0],center[1])
    limit1= -1*x
    print x,limit1
    while x<limit1 :
        screen.fill([0,0,0])
        draw_line(screen,[300,100],[300,300])
        draw_point(screen,center)
        draw_line(screen,[300,100],center)
        draw_line(screen,[300,300],center)
        center[0]+=1
        x+=1
        show()

def check_orientation(values):
    return values[0] >= 0

def main ():
    screen=Create_screen()
    show()
    close=False
    draw_line(screen,[300,100],[300,300])
    draw_point(screen,[300,200])
    show()
    while not close:
        for events in pygame.event.get():
            if events.type==pygame.MOUSEBUTTONDOWN:
                value=list(events.pos)
                x,y=cartesianas(300,200,value[0],value[1])
                print check_orientation([x,y])
                if check_orientation([x,y]):
                    while not close:
                        if events.type==pygame.QUIT:
                            close=True
                        move_left(screen,value)
                        show()
                        move_right(screen,value)
                        show()
                else:
                    while not close:
                        move_right(screen,value)
                        show()
                        move_left(screen,value)
                        show()
main()
