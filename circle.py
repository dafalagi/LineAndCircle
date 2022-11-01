# Install pygame untuk menjalankan kode dibawah ini
# Gunakan perintah "pip install -U pygame --user" untuk install pygame
# berikut link dokumentasi https://www.pygame.org/wiki/GettingStarted

from pygame import gfxdraw
import pygame
pygame.display.init()

inputRadius = int(input("Masukan nilai radius : "))

screen = pygame.display.set_mode((inputRadius*3,inputRadius*3))
screen.fill((90,90,90))
pygame.display.update()

def symmetry_points(x,y,offset):
	gfxdraw.pixel(screen,x+offset,y+offset,(255,255,255))
	gfxdraw.pixel(screen,-x+offset,y+offset,(255,255,255))
	gfxdraw.pixel(screen,x+offset,-y+offset,(255,255,255))
	gfxdraw.pixel(screen,-x+offset,-y+offset,(255,255,255))
	gfxdraw.pixel(screen,y+offset,x+offset,(255,255,255))
	gfxdraw.pixel(screen,-y+offset,x+offset,(255,255,255))
	gfxdraw.pixel(screen,y+offset,-x+offset,(255,255,255))
	gfxdraw.pixel(screen,-y+offset,-x+offset,(255,255,255))
	pygame.display.update()

def plotCircle(x,y,radius,offset):
	d = 1 - radius
	symmetry_points(x , y , radius + offset)
	while x < y:
		if d < 0:
			x += 1
			d += 2 * x + 1
		else:
			x += 1
			y -= 1
			d += 2 * ( x - y ) + 1
		symmetry_points(x , y , radius + offset)

def circle(radius,offset):
	x,y = 0,radius
	plotCircle(x,y,radius,offset)

circle(inputRadius,inputRadius // 2)
pygame.display.update()

isRun = True

while isRun:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: isRun = False
pygame.quit()