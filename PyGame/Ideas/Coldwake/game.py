from __future__ import division, absolute_import, print_function, unicode_literals
import pygame, sys, pygame.mixer

from pygame.locals import *
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('gameaudio.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
#bif=background_image_file
background_image_file="background.jpg"
#mif=mouse_image_file
character_image_file="character.png"
enemy_image_file="bad_guy.png"

game_title="Coldwake Orange"
fps=30

screen=pygame.display.set_mode((1280,1000),0,32)
pygame.display.set_caption(game_title)
background_image=pygame.image.load(background_image_file).convert()
character_image=pygame.image.load(character_image_file).convert_alpha()
bad_guy_image=pygame.image.load(enemy_image_file).convert_alpha()
#Define coordinate system and rate of movement
x,y=0,0
badx, bady= 200,200
movex, movey=0,0
fps_clock=pygame.time.Clock()
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		#Establish key events
		if event.type == KEYDOWN:
			if event.key==K_LEFT or event.key==K_a:
				movex=-1
			elif event.key==K_RIGHT or event.key==K_d:
				movex=+1
			elif event.key==K_UP or event.key==K_w:
				movey=-1
			elif event.key==K_DOWN or event.key==K_s:
				movey=+1
			elif event.key==K_q:
				pygame.quit()
				sys.exit()
			else:
				event.key==pygame.key.get_pressed()
				print("STAHP PRESSING MY BUTTONS!")
		if event.type==KEYUP:
			if event.key==K_LEFT or event.key==K_a:
				movex=0
			elif event.key==K_RIGHT or event.key==K_d:
				movex=0
			elif event.key==K_UP or event.key==K_w:
				movey=0
			elif event.key==K_DOWN or event.key==K_s:
				movey=0
		character_box=Rect((x,y), character_image.get_size())
		enemy_box=Rect((badx,bady), bad_guy_image.get_size())
		if character_box.colliderect(enemy_box):
			print("You're dead as shit son!")
			print("Seriously, dafuq you doing??? GET OUT OF THERE!!!")
	#Define the rate of movement
	x+=(10*movex)
	y+=(10*movey)
	#Put the graphics element within the window
	screen.blit(background_image,(0,0))
	screen.blit(character_image,(x,y))
	screen.blit(bad_guy_image,(badx,bady))
	#Keep the program updating the graphics
	pygame.display.update()
	fps_clock.tick(fps)
pygame.quit()
