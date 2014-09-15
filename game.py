import pygame, sys, random, fileinput, math
from player import *
from snowball import Snowball
from Vector import Vector
from engine import Engine
from sidebar import Sidebar
from bullet import *
from enemy import *


pygame.init()
screen = pygame.display.set_mode((800, 800))
levelOneBackground = pygame.image.load('Art Stuff\level one background.png')
sidebar = Sidebar()
clock = pygame.time.Clock()
mainMenuNewGame = pygame.image.load('Art Stuff\MenuNewGame.png')
mainMenuHighScores = pygame.image.load('Art Stuff\MenuHighScores.png')
mainMenuExit = pygame.image.load('Art Stuff\MenuExit.png')
#print 'levelOneBackground has loaded as ', levelOneBackground
#print 'mainMenuNewGame has loaded as ', mainMenuNewGame
#print 'mainMenuHighScores has loaded as ', mainMenuHighScores
#print 'mainMenuExit has loaded as ', mainMenuExit
game = Engine(screen, sidebar)
player = Player(game)
frame = 0
gameOpen = True
currentMenuScreen = mainMenuNewGame
screenSelect = [True, False, False]

def processPlayerEvents(player, gameRunning):
	gameRunning = True
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			#print pygame.key.name(event.key)
			if event.key == pygame.K_ESCAPE:
				gameRunning = False
	
			#if player.dash:
			#	return
	
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
				print player.getPosition()
				
			if event.key == pygame.K_SPACE:
				player.firing = True
				
			if event.key == pygame.K_LSHIFT:
				player.focus = True
				
			#if event.key == pygame.K_z:
			#	player.dash(sidebar)
				
		if event.type == pygame.KEYUP:
			#if player.dash:
			#	return
		
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
				
			if event.key == pygame.K_LSHIFT:
				player.focus = False
	
	return gameRunning
				
def mainGameProcess(frame):
	gameRunning = True
	wave = 0
	while gameRunning:
		clock.tick(60)
		gameRunning = processPlayerEvents(player, gameRunning)
		screen.blit(levelOneBackground, levelOneBackground.get_rect(), [0, 0, 600, 800])
		
		if wave == 0:
			Dialogue("penguin_ava1", "Bleh", (200,255,255), game, player)
		
		#frame actions 
		if wave == 5: #wave 5
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
			if frame==170:
				PelicanA(Vector(100,-10),game,player,10,7)
			if frame==200:
				PelicanA(Vector(100,-10),game,player,10,7)
			if frame==240:
				PelicanA(Vector(100,-10),game,player,10,7)
			if frame==270:
				PelicanA(Vector(100,-10),game,player,10,7)
			if frame==250:
				SeagullA(Vector(300,-10),game,player,15)
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
				PelicanB(Vector(500,780),game,player,10,7)
			if frame==500:
				PelicanB(Vector(500,780),game,player,10,7)
			if frame==500:
				SeagullA(Vector(400,-10),game,player,12)
			if frame==530:
				PelicanB(Vector(500,780),game,player,10,7)
			if frame==550:
				SeagullA(Vector(100,-10),game,player,15)
			if frame==560:
				PelicanB(Vector(500,780),game,player,10,7)
			if frame==600:
				SeagullA(Vector(500,-10),game,player,12)
			if frame==590:
				PelicanB(Vector(500,780),game,player,10,7)
			if frame==620:
				PelicanB(Vector(500,780),game,player,10,7)
			if frame==800:
				wave += 1
				frame = 0
		
		
		if wave == 6: #wave 6
			if frame==30:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==50:
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,5)
				SeagullA(Vector(500,-10),game,player,5)
			if frame==90:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==150:
				PelicanC(Vector(500,-10),game,player,20,7)
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,5)
				SeagullA(Vector(500,-10),game,player,5)
			if frame==210:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==240:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==250:
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,5)
				SeagullA(Vector(500,-10),game,player,5)
			if frame==270:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==300:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==330:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==350:
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,6)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,4)
				SeagullA(Vector(500,-10),game,player,5)
			if frame==360:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==390:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==420:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==450:
				PelicanC(Vector(500,-10),game,player,20,7)
				SeagullA(Vector(100,-10),game,player,8)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,9)
				SeagullA(Vector(400,-10),game,player,2)
				SeagullA(Vector(500,-10),game,player,5)
			if frame==480:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==510:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==540:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==550:
				SeagullA(Vector(100,-10),game,player,5)
			if frame==556:
				SeagullA(Vector(200,-10),game,player,5)
			if frame==560:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==552:
				SeagullA(Vector(400,-10),game,player,5)
			if frame==558:
				SeagullA(Vector(500,-10),game,player,5)
			if frame==570:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==600:
				PelicanC(Vector(500,-10),game,player,20,7)
			if frame==656:
				SeagullA(Vector(100,-10),game,player,7)
			if frame==650:
				SeagullA(Vector(200,-10),game,player,9)
			if frame==658:
				SeagullA(Vector(300,-10),game,player,6)
			if frame==654:
				SeagullA(Vector(400,-10),game,player,5)
			if frame==652:
				SeagullA(Vector(500,-10),game,player,8)
			if frame==800:
				wave += 1
				frame = 0
		
		
		if wave == 2: #wave 2
			if frame==40:
				SeagullA(Vector(300,-10),game,player,9)
			if frame==80:
				SeagullB(Vector(400,790),game,player,9)
			if frame==120:
				SeagullA(Vector(200,-10),game,player,8)
			if frame==160:
				SeagullA(Vector(300,-10),game,player,9)
			if frame==200:
				SeagullB(Vector(200,790),game,player,8)
			if frame==240:
				SeagullA(Vector(500,-10),game,player,9)
			if frame==280:
				SeagullB(Vector(400,790),game,player,8)
			if frame==320:
				SeagullA(Vector(100,-10),game,player,9)
			if frame==360:
				SeagullB(Vector(100,790),game,player,8)
			if frame==400:
				SeagullA(Vector(500,-10),game,player,9)
			if frame==440:
				SeagullB(Vector(300,790),game,player,9)
			if frame==480:
				SeagullA(Vector(200,-10),game,player,8)
			if frame==520:
				SeagullB(Vector(500,790),game,player,9)
			if frame==560:
				SeagullA(Vector(100,-10),game,player,9)
			if frame==600:
				SeagullB(Vector(400,790),game,player,9)
			if frame==800:
				wave += 1
				frame = 0
		
		
		if wave == 1: #wave 1
			if frame==50:
				SeagullA(Vector(100,-10),game,player,3)
			if frame==100:
				SeagullA(Vector(400,-10),game,player,4)
			if frame==150:
				SeagullA(Vector(200,-10),game,player,3)
			if frame==200:
				SeagullA(Vector(400,-10),game,player,4)
			if frame==250:
				SeagullA(Vector(100,-10),game,player,3)
			if frame==300:
				SeagullA(Vector(500,-10),game,player,4)
			if frame==350:
				SeagullA(Vector(300,-10),game,player,4)
			if frame==400:
				SeagullA(Vector(500,-10),game,player,4)
			if frame==450:
				SeagullA(Vector(300,-10),game,player,4)
			if frame==500:
				SeagullA(Vector(100,-10),game,player,5)
			if frame==550:
				SeagullA(Vector(500,-10),game,player,4)
			if frame==600:
				SeagullA(Vector(400,-10),game,player,5)
			if frame==650:
				SeagullA(Vector(100,-10),game,player,6)
			if frame==800:
				wave += 1
				frame = 0
		
		
		if wave == 3: #wave 3
			if frame==30:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==50:
				PelicanA(Vector(100,-10),game,player,20,7)
			if frame==90:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==150:
				PelicanA(Vector(100,-10),game,player,20,7)
				SeagullA(Vector(300,-10),game,player,5)
			if frame==210:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==250:
				PelicanA(Vector(100,-10),game,player,20,7)
			if frame==270:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==330:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==350:
				PelicanA(Vector(100,-10),game,player,20,7)
			if frame==390:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==450:
				PelicanA(Vector(100,-10),game,player,20,7)
				SeagullA(Vector(300,-10),game,player,5)
			if frame==510:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==550:
				PelicanA(Vector(100,-10),game,player,20,7)
			if frame==570:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==800:
				wave += 1
				frame = 0
		
		
		if wave == 4: #wave 4
			if frame==30:
				SeagullA(Vector(100,-10),game,player,20)
				SeagullA(Vector(200,-10),game,player,20)
				SeagullA(Vector(300,-10),game,player,20)
				SeagullA(Vector(400,-10),game,player,20)
				SeagullA(Vector(500,-10),game,player,20)
				SeagullA(Vector(150,-10),game,player,20)
				SeagullA(Vector(250,-10),game,player,20)
				SeagullA(Vector(350,-10),game,player,20)
				SeagullA(Vector(450,-10),game,player,20)
			if frame==100:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if frame==130:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==150:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==190:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==200:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if frame==250:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==300:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if frame==310:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==370:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==400:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if frame==430:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==490:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==500:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if frame==550:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==600:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if frame==610:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==670:
				SeagullA(Vector(300,-10),game,player,5)
			if frame==800:
				wave += 1
				frame = 0
		
		
		if wave == 7: #level 2 wave 1
			if frame==30:
				HummingbirdA(Vector(300,-10),game,player,1,2,50)
			if frame==60:
				HummingbirdA(Vector(400,-10),game,player,1,2,50)
			if frame==90:
				HummingbirdA(Vector(500,-10),game,player,1,3,50)
			if frame==120:
				HummingbirdA(Vector(200,-10),game,player,1,3,50)
			if frame==150:
				HummingbirdA(Vector(500,-10),game,player,1,4,50)
			if frame==180:
				HummingbirdA(Vector(100,-10),game,player,1,4,50)
			if frame==210:
				HummingbirdA(Vector(200,-10),game,player,1,5,50)
			if frame==240:
				HummingbirdA(Vector(300,-10),game,player,1,5,50)
			if frame==270:
				HummingbirdA(Vector(400,-10),game,player,1,6,50)
			if frame==300:
				HummingbirdA(Vector(300,-10),game,player,1,6,50)
			if frame==330:
				HummingbirdA(Vector(500,-10),game,player,1,7,50)
			if frame==360:
				HummingbirdA(Vector(100,-10),game,player,1,7,50)
			if frame==390:
				HummingbirdA(Vector(200,-10),game,player,1,8,50)
			if frame==420:
				HummingbirdA(Vector(400,-10),game,player,1,8,50)
			if frame==450:
				HummingbirdA(Vector(300,-10),game,player,1,9,50)
			if frame==480:
				HummingbirdA(Vector(200,-10),game,player,1,9,50)
			if frame==610:
				HummingbirdA(Vector(500,-10),game,player,1,10,50)
				
				
		if wave == 8: #level2 wave2
			if frame==30: 
				HummingbirdC(Vector(300,-10),game,player,1,5,30)
			if frame==60:
				HummingbirdC(Vector(100,-10),game,player,-1,4,30)
			if frame==100:
				HummingbirdB(Vector(400,-10),game,player,1,8,40)
			if frame==110:
				HummingbirdB(Vector(200,-10),game,player,-1,9,40)
			if frame==140:
				DoveB(Vector(300,-10),game,player,50,9)
			if frame==200:
				DoveA(Vector(300,-10),game,player)
				DoveA(Vector(100,-10),game,player)
				DoveA(Vector(500,-10),game,player)
			if frame==250:
				HummingbirdA(Vector(100,-10),game,player,1,5,30)
			if frame==300:
				HummingbirdA(Vector(300,-10),game,player,-1,6,30)
			if frame==350:
				HummingbirdA(Vector(400,-10),game,player,1,5,30)
			if frame==400:
				HummingbirdA(Vector(200,-10),game,player,-1,6,30)
			if frame==500:
				DoveA(Vector(300,-10),game,player)
			if frame==530:
				DoveB(Vector(300,-10),game,player,50,9)
				DoveA(Vector(200,-10),game,player)
				DoveA(Vecotr(400,-10),game,player)
			if frame==560:
				HummingbirdA(Vector(200,-10),game,player,1,6,30)
				HummingbirdA(Vector(400,-10),game,player,-1,6,30)
		
		
		if wave == 9: #Level2 wave3
			if frame==30:
				DoveA(Vector(300,-10),game,player)
				DoveA(Vector(200,-10),game,player)
				DoveA(Vector(100,-10),game,player)
				DoveA(Vector(400,-10),game,player)
				DoveA(Vector(500,-10),game,player)
			if frame==60:
				HummingbirdA(Vector(200,-10),game,player,1,6,30)
				HummingbirdA(Vector(400,-10),game,player,1,6,30)
			if frame==90:
				DoveB(Vector(500,-10),game,player,50,9)
				DoveB(Vector(100,-10),game,player,50,9)
			if frame==120:
				HummingbirdC(Vector(200,-10),game,player,1,3,30)
			if frame==150:
				HummingbirdC(Vector(400,-10),game,player,-1,4,30)
				DoveB(Vector(500,-10),game,player,50,9)
			if frame==180:
				HummingbirdC(Vector(400,-10),game,player,1,3,30)
			if frame==200:
				DoveA(Vector(200,-10),game,player)
				DoveA(Vector(400,-10),game,player)
			if frame==210:
				HummingbirdC(Vector(100,-10),game,player,-1,4,30)
			if frame==240:
				HummingbirdC(Vector(500,-10),game,player,1,3,30)
			if frame==250:
				DoveB(Vector(300,-10),game,player,50,9)
			if frame==270:
				HummingbirdB(Vector(200,-10),game,player,1,10,60)
				HummingbirdB(Vector(400,-10),game,player,-1,10,60)
			if frame==300:
				DoveB(Vector(100,-10),game,player,50,9)
			if frame==350:
				DoveB(Vector(400,-10),game,player,50,9)
			if frame==400:
				DoveB(Vector(300,-10),game,player,50,9)
			if frame==430:
				HummingbirdC(Vector(100,-10),game,player,1,4,30)
			if frame==460:
				HummingbirdB(Vector(500,-10),game,player,1,5,30)
			if frame==500:
				DoveB(Vector(200,-10),game,player,50,9)
			if frame==530:
				HummingbirdA(Vector(200,-10),game,player,1,10,30)
			if frame==560:
				HummingbirdA(Vector(300,-10),game,player,-1,11,30)
		
		
		if wave == 10: #level 2 wave 4
			if frame==30:
				HummingbirdA(Vector(200,-10),game,player,1,5,30)
				HummingbirdA(Vector(400,-10),game,player,-1,5,30)
			if frame==90:
				HummingbirdA(Vector(100,-10),game,player,1,6,30)
				HummingbirdA(Vector(500,-10),game,player,-1,6,30)
			if frame==150:
				HummingbirdA(Vector(200,-10),game,player,1,7,30)
				HummingbirdA(Vector(400,-10),game,player,-1,7,30)
				DoveA(Vector(300,-10),game,player)
			if frame==210:
				HummingbirdA(Vector(100,-10),game,player,1,8,30)
				HummingbirdA(Vector(500,-10),game,player,-1,8,30)
				DoveA(Vector(300,-10),game,player)
			if frame==270:
				HummingbirdB(Vector(200,-10),game,player,1,7,30)
				HummingbirdB(Vector(400,-10),game,player,1,7,30)
				DoveA(Vector(300,-10),game,player)
			if frame==330:
				HummingbirdB(Vector(100,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveA(Vector(300,-10),game,player)
			if frame==390:
				HummingbirdB(Vector(200,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveA(Vector(100,-10),game,player)
				DoveA(Vector(500,-10),game,player)
			if frame==450:
				HummingbirdB(Vector(100,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveA(Vector(200,-10),game,player)
				DoveA(Vector(300,-10),game,player)
				DoveA(Vector(400,-10),game,player)
			if frame==510:
				HummingbirdB(Vector(200,-10),game,player,1,9,30)
				HummingbirdB(Vector(400,-10),game,player,-1,9,30)
				DoveB(Vector(300,-10),game,player, 50,9)
			if frame==570:
				HummingbirdB(Vector(100,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveB(Vector(200,-10),game,player,50,9)
				DoveB(Vector(400,-10),game,player,50,9)
		
		
		if wave == 11: #Level 2 wave 5
			if frame==30:
				DoveC(Vector(300,-10),game,player,5)
			if frame==50:
				HummingbirdB(Vector(300,-10),game,player,1,4,30)
			if frame==60:
				DoveC(Vector(200,-10),game,player,5)
			if frame==90:
				DoveC(Vector(500,-10),game,player,5)
			if frame==100:
				HummingbirdB(Vector(400,-10),game,player,-1,5,30)
			if frame==120:
				DoveC(Vector(500,-10),game,player,5)
			if frame==150:
				DoveC(Vector(100,-10),game,player,5)
				HummingbirdB(Vector(200,-10),game,player,1,5,30)
			if frame==180:
				DoveC(Vector(200,-10),game,player,5)
			if frame==200:
				HummingbirdB(Vector(300,-10),game,player,-1,5,30)
			if frame==210:
				DoveC(Vector(500,-10),game,player,5)
			if frame==240:
				DoveC(Vector(200,-10),game,player,5)
			if frame==250:
				HummingbirdB(Vector(400,-10),game,player,1,5,30)
			if frame==270:
				DoveC(Vector(500,-10),game,player,5)
			if frame==300:
				DoveC(Vector(400,-10),game,player,5)
				HummingbirdB(Vector(100,-10),game,player,-1,5,30)
			if frame==330:
				DoveC(Vector(200,-10),game,player,5)
			if frame==350:
				HummingbirdB(Vector(500,-10),game,player,1,5,30)
			if frame==360:
				DoveC(Vector(100,-10),game,player,5)
			if frame==390:
				DoveC(Vector(300,-10),game,player,5)
			if frame==400:
				HummingbirdB(Vector(100,-10),game,player,-1,5,30)
			if frame==420:
				DoveC(Vector(500,-10),game,player,5)
			if frame==450:
				DoveC(Vector(400,-10),game,player,5)
				HummingbirdB(Vector(200,-10),game,player,1,5,30)
			if frame==480:
				DoveC(Vector(500,-10),game,player,5)
			if frame==500:
				HummingbirdB(Vector(100,-10),game,player,-1,5,30)
			if frame==510:
				DoveC(Vector(300,-10),game,player,5)
			if frame==540:
				DoveC(Vector(400,-10),game,player,5)
			if frame==550:
				HummingbirdB(Vector(300,-10),game,player,1,5,30)
			if frame==570:
				DoveC(Vector(200,-10),game,player,5)
			if frame==600:
				DoveC(Vector(500,-10),game,player,5)
				HummingbirdB(Vector(200,-10),game,player,1,5,30)
		
		
		if wave == 12:	#Level 2 Wave 6
			if frame==30:
				DoveA(Vector(100,-10),game,player)
			if frame==50:
				DoveC(Vector(200,-10),game,player,4)
			if frame==60:
				DoveA(Vector(300,-10),game,player)
			if frame==90:
				DoveA(Vector(200,-10),game,player)
			if frame==100:
				DoveC(Vector(500,-10),game,player,5)
			if frame==120:
				DoveA(Vector(100,-10),game,player)
			if frame==150:
				DoveA(Vector(400,-10),game,player)
				DoveC(Vector(500,-10),game,player,5)
			if frame==180:
				DoveA(Vector(200,-10),game,player)
			if frame==200:
				DoveC(Vector(400,-10),game,player,5)
			if frame==210:
				DoveA(Vector(500,-10),game,player)
			if frame==240:
				DoveA(Vector(300,-10),game,player)
			if frame==250:
				DoveC(Vector(200,-10),game,player,5)
			if frame==270:
				DoveA(Vector(400,-10),game,player)
			if frame==300:
				DoveA(Vector(200,-10),game,player)
				DoveC(Vector(100,-10),game,player,5)
			if frame==330:
				DoveA(Vector(500,-10),game,player)
			if frame==350:
				DoveC(Vector(200,-10),game,player,5)
			if frame==360:
				DoveA(Vector(300,-10),game,player)
			if frame==390:
				DoveA(Vector(200,-10),game,player)
			if frame==400:
				DoveC(Vector(300,-10),game,player,5)
			if frame==420:
				DoveA(Vector(100,-10),game,player)
			if frame==450:
				DoveA(Vector(400,-10),game,player)
				DoveC(Vector(20,-10),game,player,5)
			if frame==480:
				DoveA(Vector(100,-10),game,player)
			if frame==500:
				DoveC(Vector(200,-10),game,player,5)
			if frame==510:
				DoveA(Vector(400,-10),game,player)
			if frame==540:
				DoveA(Vector(300,-10),game,player)
			if frame==550:
				DoveC(Vector(200,-10),game,player,5)
			if frame==570:
				DoveA(Vector(400,-10),game,player)
			if frame==600:
				DoveA(Vector(200,-10),game,player)
				DoveC(Vector(500,-10),game,player,5)
		
		
		if wave == 13: #Level 3 wave 1
			if frame==30:
				ToucanA(Vector(300,-10),game,player,5,5,15)
			if frame==60:
				ToucanA(Vector(500,-10),game,player,4,5,15)
			if frame==90:
				ToucanA(Vector(100,-10),game,player,4,5,15)
			if frame==120:
				ToucanA(Vector(200,-10),game,player,4,5,15)
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if frame==150:
				ToucanA(Vector(300,-10),game,player,6,5,15)
			if frame==180:
				ToucanA(Vector(100,-10),game,player,5,5,15)
			if frame==210:
				ToucanA(Vector(500,-10),game,player,5,5,15)
			if frame==240:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if frame==270:
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if frame==300:
				ToucanA(Vector(200,-10),game,player,6,5,15)
			if frame==330:
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if frame==360:
				ToucanA(Vector(500,-10),game,player,6,5,15)
			if frame==390:
				ToucanA(Vector(300,-10),game,player,6,5,15)
			if frame==420:
				ToucanA(Vector(500,-10),game,player,6,5,15)
			if frame==450:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if frame==480:
				ToucanA(Vector(300,-10),game,player,5,5,15)
			if frame==510:
				ToucanA(Vector(400,-10),game,player,6,5,15)
			if frame==540:
				ToucanA(Vector(500,-10),game,player,5,5,15)
			if frame==570:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if frame==600:
				ToucanA(Vector(500,-10),game,player,6,5,15)
		
		
		if wave == 14: #Level 3 wave 2
			if frame==30:
				ToucanB(Vector(300,-10),game,player,5,15)
			if frame==90:
				ToucanB(Vector(100,-10),game,player,5,15)
				ToucanB(Vector(500,-10),game,player,5,15)
			if frame==150:
				ToucanB(Vector(200,-10),game,player,7,15)
			if frame==210:
				ToucanB(Vector(400,-10),game,player,7,15)
			if frame==270:
				ToucanB(Vector(200,-10),game,player,6,15)
				ToucanB(Vector(500,-10),game,player,6,15)
			if frame==330:
				ToucanB(Vector(300,-10),game,player,8,15)
			if frame==390:
				ToucanB(Vector(400,-10),game,player,7,15)
			if frame==450:
				ToucanB(Vector(300,-10),game,player,11,15)
			if frame==510:
				ToucanB(Vector(500,-10),game,player,11,15)
			if frame==570:
				ToucanB(Vector(100,-10),game,player,8,15)
		
		
		if wave == 15:	#Level 3 wave 3
			if frame==30:
				BlueparrotA(Vector(300,-10),game,player,1,4,30)
			if frame==60:
				BlueparrotA(Vector(100,-10),game,player,-1,3,30)
			if frame==90:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if frame==120:
				BlueparrotA(Vector(200,-10),game,player,-1,3,30)
			if frame==150:
				BlueparrotA(Vector(100,-10),game,player,1,3,30)
			if frame==180:
				BlueparrotA(Vector(400,-10),game,player,-1,3,30)
			if frame==210:
				BlueparrotA(Vector(100,-10),game,player,1,4,30)
			if frame==240:
				BlueparrotA(Vector(200,-10),game,player,-1,4,30)
			if frame==270:
				BlueparrotA(Vector(400,-10),game,player,1,4,30)
			if frame==300:
				BlueparrotA(Vector(200,-10),game,player,-1,4,30)
			if frame==330:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if frame==360:
				BlueparrotA(Vector(100,-10),game,player,-1,4,30)
			if frame==390:
				BlueparrotA(Vector(300,-10),game,player,1,4,30)
			if frame==420:
				BlueparrotA(Vector(500,-10),game,player,-1,3,30)
			if frame==450:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if frame==480:
				BlueparrotA(Vector(200,-10),game,player,-1,3,30)
			if frame==510:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if frame==540:
				BlueparrotA(Vector(400,-10),game,player,-1,3,30)
			if frame==570:
				BlueparrotA(Vector(500,-10),game,player,1,3,30)
			if frame==600:
				BlueparrotA(Vector(200,-10),game,player,-1,4,30)
		
		
		if wave == 16: #Level 3 wave 4
			if frame==30:
				ToucanA(Vector(100,-10),game,player,6,5,15)
				ToucanA(Vector(200,-10),game,player,6,5,15)
				ToucanA(Vector(300,-10),game,player,6,5,15)
				ToucanA(Vector(400,-10),game,player,6,5,15)
				ToucanA(Vector(500,-10),game,player,6,5,15)
			if frame==130:
				ToucanA(Vector(300,-10),game,player,15,5,15)
			if frame==260:
				ToucanB(Vector(100,-10),game,player,10,15)
				ToucanB(Vector(500,-10),game,player,10,15)
			if frame==480:
				ToucanA(Vector(200,-10),game,player,7,5,15)
				ToucanA(Vector(400,-10),game,player,7,5,15)
				BlueparrotA(Vector(300,-10),game,player,1,4,30)
			if frame==540:
				BlueparrotA(Vector(500,-10),game,player,-1,5,30)
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
			if frame==570:
				BlueparrotA(Vector(200,-10),game,player,1,5,30)
				BlueparrotA(Vector(400,-10),game,player,1,5,30)
			if frame==600:
				BlueparrotA(Vector(300,-10),game,player,-1,5,30)
		
		
		if wave == 17:  #Level 3 wave 5
			if frame==30:
				BlueparrotB(Vector(300,-10),game,player,1,30,7)
			if frame==60:
				BlueparrotB(Vector(500,-10),game,player,-1,30,7)
			if frame==90:
				BlueparrotB(Vector(100,-10),game,player,1,30,7)
			if frame==120:
				BlueparrotB(Vector(400,-10),game,player,-1,30,7)
			if frame==150:
				BlueparrotB(Vector(200,-10),game,player,1,30,7)
			if frame==180:
				BlueparrotA(Vector(300,-10),game,player,-1,5,30)
			if frame==210:
				BlueparrotA(Vector(300,-10),game,player,1,5,30)
			if frame==240:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if frame==270:
				BlueparrotA(Vector(500,-10),game,player,1,5,30)
			if frame==300:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if frame==330:
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if frame==360:
				BlueparrotB(Vector(400,-10),game,player,-1,30,7)
			if frame==390:
				BlueparrotA(Vector(500,-10),game,player,1,5,30)
			if frame==420:
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
			if frame==450:
				BlueparrotA(Vector(300,-10),game,player,1,5,30)
			if frame==480:
				BlueparrotA(Vector(200,-10),game,player,-1,5,30)
			if frame==510:
				BlueparrotA(Vector(400,-10),game,player,1,5,30)
			if frame==540:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if frame==570:
				BlueparrotA(Vector(300,-10),game,player,1,5,30)
			if frame==600:
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
		
		
		if wave == 18: #Level 3 wave 6
			if frame==30:
				ToucanA(Vector(100,-10),game,player,5,4,30)  #For some reason that 4 needs to be a 4 to spawn 3 bucks. don't ask why. I don't know  --Nick
			if frame==50:
				BlueparrotB(Vector(400,-10),game,player,1,30,7)
			if frame==90:
				ToucanA(Vector(200,-10),game,player,5,4,30)
			if frame==150:
				ToucanA(Vector(400,-10),game,player,5,4,30)
				BlueparrotB(Vector(300,-10),game,player,-1,30,7)
			if frame==210:
				ToucanA(Vector(100,-10),game,player,5,4,30)
			if frame==250:
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if frame==270:
				ToucanA(Vector(400,-10),game,player,5,4,30)
			if frame==330:
				ToucanA(Vector(500,-10),game,player,5,4,30)
			if frame==350:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if frame==390:
				ToucanA(Vector(400,-10),game,player,5,4,30)
			if frame==450:
				ToucanA(Vector(100,-10),game,player,5,4,30)
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if frame==510:
				ToucanA(Vector(300,-10),game,player,5,4,30)
			if frame==550:
				BlueparrotB(Vector(200,-10),game,player,-1,30,7)
			if frame==570:
				ToucanA(Vector(100,-10),game,player,5,4,30)
				
			
		#update 
		game.update()
		#collision
		
		#draw
		game.draw()
		sidebar.draw(screen)
		pygame.display.flip()
		frame+=1

def mainMenuEvents(currentMenuScreen, mainMenuNewGame, mainMenuHighScores, mainMenuExit):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			
			if event.key == pygame.K_RETURN:
				if screenSelect[0] == True:
					frame = 0
					mainGameProcess(frame)
					
				elif screenSelect[1] == True:
					# High Score selected
					a = 5
					
				elif screenSelect[2] == True:
					sys.exit()
					
			if event.key == pygame.K_UP:
				if screenSelect[0] == True: #New Game Selected
					#print 'switching from new game to exit'
					screenSelect[0] = False
					screenSelect[2] = True
					currentMenuScreen = mainMenuExit
					
				elif screenSelect[1] == True: #High Scores Selected
					#print 'switching from high scores to new game'
					screenSelect[1] = False
					screenSelect[0] = True
					currentMenuScreen = mainMenuNewGame
					
				elif screenSelect[2] == True: #Exit Selected
					#print 'switching from exit to high scores'
					screenSelect[2] = False
					screenSelect[1] = True
					currentMenuScreen = mainMenuHighScores
					
			if event.key == pygame.K_DOWN:
				if screenSelect[0] == True: #New Game Selected
					screenSelect[0] = False
					screenSelect[1] = True
					currentMenuScreen = mainMenuHighScores
					
				elif screenSelect[1] == True: #High Scores Selected
					screenSelect[1] = False
					screenSelect[2] = True
					currentMenuScreen = mainMenuExit
					
				elif screenSelect[2] == True: #Exit Selected
					screenSelect[2] = False
					screenSelect[0] = True
					currentMenuScreen = mainMenuNewGame
		
	return currentMenuScreen	
	
	
while gameOpen:
	clock.tick(60)
	screen.blit(currentMenuScreen, currentMenuScreen.get_rect(), [0, 0, 800, 800])
	currentMenuScreen = mainMenuEvents(currentMenuScreen, mainMenuNewGame, mainMenuHighScores, mainMenuExit)
	pygame.display.flip()
	
