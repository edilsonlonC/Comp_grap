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
    screen=Create_screen([1000,1000])
    image=Create_images("airplane.png")

    show()
    close=False
    x_move=200
    draw_image=False
    pos=[]
    while not close:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos.append(list(event.pos))
                show_images(screen,image,pos[0])
                draw_image=True
        if draw_image==True:
            if (pos[0][0]<=900):
                show_images(screen,image,[pos[0][0],pos[0][1]])
                pos[0][0]+=1
                show()
                clear(screen)
main()
