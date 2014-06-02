import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print (camlist)
