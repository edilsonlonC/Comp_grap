import pygame
from pygame.locals import*
pygame.init()
def Create_images (url):
    image=pygame.image.load(url)
    return image
def Create_screen (SIZE):
    screen=pygame.display.set_mode(SIZE)
    return screen
def show_images (screen,image,pos):
    screen.blit(image,pos)
def show ():
    pygame.display.flip()
def clear (screen):
    screen.fill([0,0,0])

class megaman :
    def __init__(self):
        self.run1=Create_images("run1.png")
        self.run2=Create_images("run2.png")
        self.depie=Create_images("depie.png")
        self.background=Create_images("Esta.jpg")
        self.jump1=Create_images("jump.png")
        self.jump2=Create_images("jump2.png")
        self.clock=pygame.time.Clock()
        self.estado=0 # 0 depie 1 corriendo, 2 saltando
    def Run (self,screen,pos):
        screen.blit(self.run1,pos)
    def Run2 (self,screen,pos):
        screen.blit(self.run2,pos)
    def stop (self,screen,pos):
        screen.blit(self.depie,pos)
    def wait (self,TIME):
        self.clock.tick(TIME)
    def Jump1 (self,screen,pos):
        screen.blit(self.jump1,pos)
    def Jump2 (self,screen,pos):
        screen.blit(self.jump2,pos)
def main ():
    screen=Create_screen([800,800])
    Megaman=megaman()
    close=False
    x=0
    y=40
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
        if  pygame.key.get_focused():
            #Megaman.Run(screen,[x,y])
            x+=1
        show()
        Megaman.Run(screen,[x,y])

main()
