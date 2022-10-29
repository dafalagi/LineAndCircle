from pygame import gfxdraw
import sys,pygame
pygame.display.init()

screen = pygame.display.set_mode((800,400))
screen.fill((0,0,0))
pygame.display.flip()

def circle(radius,offset):
	x,y = 0,radius
	plotCircle(x,y,radius,offset)

def symmetry_points(x,y,offset):
	gfxdraw.pixel(screen,x+offset,y+offset,(255,255,255))
	gfxdraw.pixel(screen,-x+offset,y+offset,(255,255,255))
	gfxdraw.pixel(screen,x+offset,-y+offset,(255,255,255))
	gfxdraw.pixel(screen,-x+offset,-y+offset,(255,255,255))
	gfxdraw.pixel(screen,y+offset,x+offset,(255,255,255))
	gfxdraw.pixel(screen,-y+offset,x+offset,(255,255,255))
	gfxdraw.pixel(screen,y+offset,-x+offset,(255,255,255))
	gfxdraw.pixel(screen,-y+offset,-x+offset,(255,255,255))
	pygame.display.flip()

def plotCircle(x,y,radius,offset):
	d = 1 - radius
	symmetry_points(x,y,radius+offset)
	while x < y:
		if d < 0:
			x += 1
			d += 2*x + 1
		else:
			x += 1
			y -= 1
			d += 2*(x-y) + 1
		symmetry_points(x,y,radius+offset)

Fradius = int(input("Masukan nilai radius : "))
Foffset = int(input("Masukan nilai offset : "))
circle(Fradius,Foffset)
pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()