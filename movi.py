import pygame
import random
r=lambda: random.randint(0,255)
r2=lambda: random.randint(0,10)
pygame.init()


def Create_screen (Size):
    screen=pygame.display.set_mode(Size)
    return screen

def draw_line (screen,p_i,p_f):
    pygame.draw.line(screen,[r(),r(),r()],p_i,p_f)
def draw_point (screen,center):
    pygame.draw.circle(screen,[r(),r(),r()],center,5)
#show new change in screen
def show ():
    pygame.display.flip()

def move_left (screen,center):
    limit=300
    c=600
    while c>limit:
        clear(screen)
        draw_line(screen,[300,0],[300,600])
        c-=1
        center[0]=c
        draw_point(screen,center)
        show()
    #center[0]=298
def move_right (screen,center):
    limit=600
    c=300
    while c<limit:
        clear(screen)
        draw_line(screen,[300,0],[300,600])
        c+=1
        center[0]=c
        draw_point(screen,center)
        show()
    #center[0]=298
def check_orientation(values):
    return values[0] >= 0
#def check_orientation_display(values):

#color in screen
def clear (screen):
    screen.fill([0,0,0])
#define limit in coordenate x
def check_limit_x (position,size):
    return position[0]>=(size[0]/2)


def main ():
    position=[200,50]
    size=[600,600]
    screen=Create_screen(size)
    draw_line(screen,[300,0],[300,600])
    draw_point(screen,position)
    speed=0
    show()
    while True:
        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    position[1]-=10
                    clear(screen)
                if event.key==pygame.K_DOWN:
                    position[1]+=10
                    clear(screen)
                if event.key==pygame.K_LEFT:
                    position[0]-=10
                    clear(screen)
                if event.key==pygame.K_RIGHT:
                    position[0]+=10
                    clear(screen)
                    #draw_line(screen,[300,0],[300,600])

        if check_limit_x(position,size):
            move_right(screen,position)
            move_left(screen,position)

            position[0]=295
        else:
            position[0]+=speed
        clear(screen)
        draw_line(screen,[300,0],[300,600])
        draw_point(screen,position)
        show()


main()
