import pygame, sys, random, fileinput, math
from player import Player
from snowball import Snowball
from Vector import Vector
from engine import Engine
from bullet import *
from enemy import *

pygame.init()
screen = pygame.display.set_mode((600, 800))
levelOneBackground = pygame.image.load('Art Stuff\level one background.png')
clock = pygame.time.Clock()

def processPlayerEvents(player):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print pygame.key.name(event.key)
			if event.key == pygame.K_ESCAPE:
				sys.exit()
	
			if event.key == pygame.K_UP:
				player.moving[0] = True
				player.moving[1] = False
				
			if event.key == pygame.K_DOWN:
				player.moving[1] = True
				player.moving[0] = False
				
			if event.key == pygame.K_LEFT:
				player.moving[2] = True
				player.moving[3] = False
				
			if event.key == pygame.K_RIGHT:
				player.moving[3] = True
				player.moving[2] = False
				
			if event.key == pygame.K_TAB:
				player.getPosition()
				
			if event.key == pygame.K_SPACE:
				player.firing = True
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player.moving[0] = False
				
			if event.key == pygame.K_DOWN:
				player.moving[1] = False
				
			if event.key == pygame.K_LEFT:
				player.moving[2] = False
				
			if event.key == pygame.K_RIGHT:
				player.moving[3] = False

			if event.key == pygame.K_SPACE:
				player.firing = False
				
gameRunning = True
game = Engine(screen)
player = Player(game)
frame = 0



while gameRunning:
	clock.tick(60)
	processPlayerEvents(player)
	screen.blit(levelOneBackground, levelOneBackground.get_rect(), [0, 0, 600, 800])
	
	#frame actions 
	# if frame == 60:	
		# SeagullA(Vector(300, -10), game, player)
		
	# if frame == 120:	
		# SeagullA(Vector(150, -10), game, player)
		# SeagullA(Vector(450, -10), game, player)
		
	# if frame == 150:
		# SeagullB(Vector(200, -10), game, player)
	
	# if frame == 210:
		# SeagullB(Vector(400, -10), game, player)
		
	# if frame == 275:
		# SeagullA(Vector(100, -10), game, player)
	
	# if frame == 300:
		# SeagullB(Vector(350, -10), game, player)
		
	# if frame == 315:
		# SeagullA(Vector(500, -10), game, player)
		
	# if frame == 330:
		# SeagullB(Vector(250, -10), game, player)
	if frame==30:
		SeagullA(Vector(300,-10),game,player,5)
	if frame==60:
		SeagullA(Vector(500,-10),game,player,8)
		SeagullA(Vector(100,-10),game,player,7)
	if frame==90:
		SeagullA(Vector(400,-10),game,player,6)
	if frame==100:
		SeagullA(Vector(200,-10),game,player,5)
	if frame==110:
		SeagullA(Vector(300,-10),game,player,8)
	if frame==120:
		SeagullA(Vector(500,-10),game,player,9)
	if frame==130:
		SeagullA(Vector(100,-10),game,player,10)
	if frame==150:
		SeagullB(Vector(100,750),game,player)
	#update 
	game.update()
	
	#collision
	
	#draw
	game.draw()
	pygame.display.flip()
	frame+=1
	

