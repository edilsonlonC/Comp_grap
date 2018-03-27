import pygame,sys
from pygame.locals import*

pygame.init()

screen=pygame.display.set_mode([1000,1000])
x,y=170,300
pixel=1
image=pygame.image.load("airplane.png")


def move (screen,image,x,y):
	screen.blit(image,[x,y])
	pygame.display.update()
#image=pygame.image.load("airplane
while True:
	screen.fill([255,255,255])
	screen.blit(image,[x,y])	
	for event in pygame.event.get():
    
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.KEYDOWN:
			if event.key==K_RIGHT:
				move (screen,image,x,y)
				x+=5  
			elif event.key==K_LEFT:
				move(screen,image,x,y)
				x-=5
			elif event.key==K_TOP:
				move(screen,image,x,y)
				y+=5
	#pygame.display.update()
	pygame.display.update()

