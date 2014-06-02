background_image_file="bg.jpg"
#Have to use .png for images that will have transparency
mouse_image_file="ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480), 0, 32)

background=pygame.image.load(background_image_file).convert()
#Using convert_alpha gives transparency to image
mouse_cursor=pygame.image.load(mouse_image_file).convert_alpha()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
	screen.blit(background, (0,0))
	
	x,y = pygame.mouse.get_pos()
	x -= mouse_cursor.get_width()/2
	y -= mouse_cursor.get_height()/2
	
	screen.blit(mouse_cursor,(x,y))
	
	pygame.display.update()
