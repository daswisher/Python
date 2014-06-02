background_image_file="bg.jpg"
mouse_image_file="ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(background_image_file).convert()
ball=pygame.image.load(mouse_image_file).convert_alpha()

x=0

while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(background, (0,0))
	screen.blit(ball, (x, 160))
	x+=1
	#causes the ball to reset when it leaves the screen
	if x>640:
		x=0
	pygame.display.update()
