import pygame
#r=lambda: random.randint(0,255)
#z=lambda: random.randint(0,1000)

if __name__=='__main__':
    pygame.init()
    print "probando --"
    screen=pygame.display.set_mode([1000,1000])
    close=False
    while not close:
        for event in pygame.event.get():
            pygame.draw.polygon(screen,[r(),r(),r()],position1,1)
            pygame.display.flip()
            if event.type==pygame.QUIT:
                close = True
            pygame.display.flip()
