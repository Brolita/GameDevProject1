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
	if True: #wave 1
		if frame==30:
			SeagullA(Vector(300,-10),game,player,5)
		if frame==60:
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
			PelicanA(Vector(100,-10),game,player,10,7)
		if frame==180:
			PelicanA(Vector(100,-10),game,player,10,7)
		if frame==210:
			PelicanA(Vector(100,-10),game,player,10,7)
		if frame==240:
			PelicanA(Vector(100,-10),game,player,10,7)
		if frame==250:
			SeagullA(Vector(300,-10),game,player,15)
		if frame==270:
			PelicanA(Vector(100,-10),game,player,10,7)
		if frame==300:
			PelicanA(Vector(100,-10),game,player,10,7)
		if frame==300:
			SeagullA(Vector(200,-10),game,player,15)
		if frame==350:
			SeagullA(Vector(300,-10),game,player,10)
		if frame==400:
			SeagullA(Vector(500,-10),game,player,11)
		if frame==450:
			SeagullA(Vector(200,-10),game,player,13)
		if frame==470:
			PelicanB(Vector(100,780),game,player,10,7)
		if frame==500:
			PelicanB(Vector(100,780),game,player,10,7)
		if frame==500:
			SeagullA(Vector(400,-10),game,player,12)
		if frame==530:
			PelicanB(Vector(100,780),game,player,10,7)
		if frame==550:
			SeagullA(Vector(100,-10),game,player,15)
		if frame==560:
			PelicanB(Vector(100,780),game,player,10,7)
		if frame==600:
			SeagullA(Vector(500,-10),game,player,12)
		if frame==590:
			PelicanB(Vector(100,780),game,player,10,7)
		if frame==620:
			PelicanB(Vector(100,780),game,player,10,7)
	

	#update 
	game.update()
	
	#collision
	
	#draw
	game.draw()
	pygame.display.flip()
	frame+=1
	

