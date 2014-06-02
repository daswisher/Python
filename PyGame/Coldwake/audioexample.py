#!/usr/bin/python
import sys, pygame, pygame.mixer
pygame.init()

sound = pygame.mixer.Sound('start.wav')

sound.play()

size= width, height = 640,480
black=0,0,0

screen=pygame.display.set_mode(size)

tux = pygame.image.load("tux.png")

x=0
y=0
r=0
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	screen.fill((r,0,0))
	screen.blit(tux,(200,200))
	screen.blit(tux,(x,y))
	
	pygame.display.flip()
	x+=1
	y+=1
	if r==255:
		r1=-1
		sound.play()
	elif r ==0:
		r1=1
	r+=1
	sound.play()
