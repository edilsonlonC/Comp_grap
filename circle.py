import pygame

pygame.init()

def retroceso ():
    reloj=pygame.time.Clock()
    reloj.tick(10)
def Create_screen ():
    screen=pygame.display.set_mode([600,400])
    return screen

def show_screen():
    pygame.display.flip()

def draw_circle (screen,x,y):
    pygame.draw.circle(screen,[255,0,0],[x,y],5)

def move_circle(screen,x,y):

    screen.fill([0,0,0])
    draw_circle(screen,x,y)
    show_screen()
    retroceso()
    pygame.display.flip()
def main ():
    screen = Create_screen()
    x=50
    y=50
    move=y
    circle_move=1

    while move<600:
        if circle_move==1:
            move_circle(screen,move,y)
        if circle_move==2:
            #x=move
            #move=y
            move_circle(screen,x,move)
        move+=1
        for event in pygame.event.get():
            if  event.type==pygame.MOUSEBUTTONDOWN:
                x=move
                move=y
                circle_move=2
main()
