#interfaz
import pygame
import random
r=lambda: random.randint(0,255)

if __name__ == '__main__':
    pygame.init()

    screen=pygame.display.set_mode([1000,1000])
    close=False
    position1=[0,0]
    position2=[100,100]
    while not close:
        for event in pygame.event.get():

            pygame.draw.line(screen,[0,0,255],position2,position1)
            pygame.display.flip()
            #position2=position1
            if event.type == pygame.QUIT:
                close=True
            #if event.type==pygame.MOUSEBUTTONDOWN:
            #    print 'Click'
            position1= event.pos
            pygame.draw.line(screen,[r(),r(),r()],position2,position1,20)
                #position2=position1
