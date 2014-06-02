background_image_file="bg.jpg"
mouse_image_file="ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
background=pygame.image.load(background_image_file).convert()
ball=pygame.image.load(mouse_image_file).convert_alpha()

x=0
y=0
clock=pygame.time.Clock()
speedx=150
speedy=100

while True:
	
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(background, (0,0))
	screen.blit(ball, (x,y))
	milli=clock.tick()
	seconds=milli/1000.
	distance_moved_x=seconds*speedx
	distance_moved_y=seconds*speedy
	x+=distance_moved_x
	y+=distance_moved_y
	if x>140:
		x=0
	if y>480:
		y=0
	pygame.display.update()

