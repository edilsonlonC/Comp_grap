import pygame
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

def main ():
    screen=Create_screen([1000,700])
    image=Create_images("Esta.jpg")
    mega=Create_images("Megaman.png")
    show_images(screen,image,[0,0])
    show_images(screen,mega,[200,300])
    x=0
    y=0
    show()
    close=False
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
        pos=pygame.mouse.get_pos()
        if pos[0]>900:
            x+=1
        if pos[0]<100:
            x-=1
        if pos[1]<100:
            y-=1
        if pos[1]>600:
            y+=1


        show_images(screen,image,[x,y])
        show()
        clear(screen)
main()
