import pygame
from pygame.locals import*
pygame.init()
class megaman :
    def __init__(self):
        self.run1=pygame.image.load("run1.png")
        self.run2=pygame.image.load("run2.png")
        self.depie=pygame.image.load("depie.png")
    def Run (self,pos):
        screen.blit(self.run1,pos)

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

def main ():
    screen=Create_screen([800,1000])
    image=Create_images("Esta.jpg")
    mega=Create_images("depie.png")
    show_images(screen,image,[0,0])
    show_images(screen,mega,[30,30])
    posImage=[30,30]
    pos_background=[0,0]
    show()
    close=False
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            if event.type==pygame.KEYDOWN:
                if event.key==K_RIGHT:
                    if posImage[0]>400:
                        pos_background[0]-=10
                    else:
                        posImage[0]+=10

        show_images(screen,image,pos_background)
        show_images(screen,mega,posImage)
        show()
        clear(screen)


main()
