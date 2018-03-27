import pygame
import random
r=lambda: random.randint(0,255)

if __name__=='__main__':
    pygame.init()
    print "probando --"
    screen=pygame.display.set_mode([1000,1000])
    close=False
    position1=[[100,100],[200,300]]
    position2=[[100,100],[200,100],[200,300],[400,500]]
    listP=[2,8,6,8,9,10,15,4]
    while not close:
        for event in pygame.event.get():
            pygame.draw.polygon(screen,[r(),r(),r()],position1,1)
            pygame.display.flip()
            if event.type==pygame.QUIT:
                close = True
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos
                position1.append(pos)
                pygame.draw.polygon(screen,[r(),r(),r()],position1,1)
                pygame.display.flip()
