#bif=background_image_file
background_image_file="bg.jpg"
#mif=mouse_image_file
mouse_image_file="ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(background_image_file).convert()
mouse_cursor=pygame.image.load(mouse_image_file).convert_alpha()

x,y=0,0
movex, movey=0,0

while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key==K_LEFT:
				movex=-1
			elif event.key==K_RIGHT:
				movex=+1
			elif event.key==K_UP:
				movey=-1
			elif event.key==K_DOWN:
				movey=+1
		if event.type==KEYUP:
			if event.key==K_LEFT:
				movex=0
			elif event.key==K_RIGHT:
				movex=0
			elif event.key==K_UP:
				movey=0
			elif event.key==K_DOWN:
				movey=0
	x+=movex
	y+=movey
	
	screen.blit(background,(0,0))
	screen.blit(mouse_cursor,(x,y))
	
	pygame.display.update()
