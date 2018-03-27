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



def jumped (y,x,x_i,screen,image,Megaman):
    a=y
    while a>y-100:
        #Megaman.wait(500)
        show_images(screen,image,[x_i,0])
        Megaman.Jump2(screen,[x,a])
        show()
        a-=1

    for i in range (y-100,y):
        print i
        #Megaman.wait(100)
        show_images(screen,image,[x_i,0])
        Megaman.Jump1(screen,[x,i])
        show()
    show_images(screen,image,[x_i,0])
    Megaman.stop(screen,[x,y])


def main ():
    screen=Create_screen([800,1000])
    image=Create_images("Esta.jpg")
    show_images(screen,image,[0,0])
    Megaman=megaman()
    #Megaman.stop(screen,[20,30])
    #show()
    #clock=pygame.time.Clock()
    x=30
    y=500
    Megaman.stop(screen,[x,y])
    show()
    close=False
    run=1
    x_i=0
    while not close:
        show_images(screen,image,[x_i,0])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            if event.type==pygame.KEYDOWN:
                if event.key==K_RIGHT:
                    if run==1 or run==0 or run ==3:
                        Megaman.Run(screen,[x,y])
                        run=2
                    elif run==2:
                        Megaman.Run2(screen,[x,y])
                        run=1
                if event.key==K_LEFT:
                    run=0
                    Megaman.stop(screen,[x,y])
                if event.key==K_UP:
                    #run=3
                    #Megaman.Jump2(screen,[x,y-100])
                    #Megaman.wait(10)
                    jumped (y,x,x_i,screen,image,Megaman)

                #Megaman.stop(screen,[x,30])
                if x<600 and run!=0 and run !=3:
                    x+=20
                elif x>600 and run!=0 and run != 3:
                    x_i-=20
                if x_i==-300 and run!=0 and run != 3:
                    x_i=0
                #if run==3:
                    #Megaman.Jump1(screen,[x,y])
                show()
                clear(screen)
main()
