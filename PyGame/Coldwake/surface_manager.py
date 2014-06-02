#These are all of the surface controls
import pygame

surface_list = pygame.sprite.RenderUpdates()
#Adds objects to surface
def add(surface):
    global surface_list
    surface_list.add(surface)
#Removes objects from surface
def remove(surface):
    global surface_list
    surface_list.remove(surface)
#Updates surface object displayd 
def update():
    global surface_list
    surface_list.update()
#Draws objects onto surface
def draw(display):
    global surface_list
    dirty_rects = surface_list.draw(display)
    return dirty_rects
#Cleans the surface
def clear(display, background):
    global surface_list
    surface_list.clear(display, background)
#Check the surface if it contains an object already
def has(surface):
    if surface_list.has(surface):
        return True
    else:
        return False
#Empties the surface list
def empty():
    global surface_list
    surface_list.empty()
