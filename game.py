import pygame, sys, random, fileinput, math
from player import *
from snowball import Snowball
from Vector import Vector
from engine import Engine
from sidebar import Sidebar
from bullet import *
from enemy import *

levelOneBackground = pygame.image.load('Art Stuff\level one background.png')
mainMenuNewGame = pygame.image.load('Art Stuff\MenuNewGame.png')
mainMenuHighScores = pygame.image.load('Art Stuff\MenuHighScores.png')
mainMenuExit = pygame.image.load('Art Stuff\MenuExit.png')
pauseMenuResume = pygame.image.load('Art Stuff\PauseMenuResume.png')
pauseMenuRestart = pygame.image.load('Art Stuff\PauseMenuRestart.png')
pauseMenuExit = pygame.image.load('Art Stuff\PauseMenuExit.png')

pygame.init()
screen = pygame.display.set_mode((800, 800))
sidebar = Sidebar()
game = Engine(screen, sidebar)
Enemy.setSidebar(sidebar)
player = Player(game)

clock = pygame.time.Clock()
game.frame = 0
gameOpen = True
currentMenuScreen = mainMenuNewGame
currentPauseScreen = pauseMenuResume
screenSelect = [True, False, False]
pauseSelect = [True, False, False]

def gameOverScreen():
	print "Game Over"
	#its too shocking to just go to gameover from 
	#last death so do something here as well
	while True:
		processGameOverEvents(None, None)
		
	#if you call game.restart('soft')
	#and then exit this function with 
	#return True the game will restart 
	#to the last level or boss return 
	#False will return to main menu

def pauseScreen():
	currentPauseScreen = pauseMenuResume
	keepPlaying = True # Conditional for when the player quits the current game via the pause menu
	paused = True
	pauseSelect[0] = True
	pauseSelect[1] = False
	pauseSelect[2] = False
	while paused:
		clock.tick(60)
		screen.blit(currentPauseScreen, (250, 325)) #[250, 325, 550, 475]
		currentPauseScreen, paused, keepPlaying = processPauseEvents(currentPauseScreen, pauseMenuResume, pauseMenuRestart, pauseMenuExit)
		pygame.display.flip()
	
	if keepPlaying == 1:
		return True
	
	elif keepPlaying == 0:
		return False
		
	else:
		game.restart()
		return True

def processGameOverEvents(gameOverRestartScreen, gameOverExitScreen):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
				
def processPauseEvents(currentPauseScreen, pauseMenuResume, pauseMenuRestart, pauseMenuExit):
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			#Ignore it because this game is being a fuck right now
			#print 'lalalala i am a dummy'
			a = 5
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				return currentPauseScreen, False, 1
			
			elif event.key == pygame.K_RETURN:
				if pauseSelect[0] == True:
					return currentPauseScreen, False, 1
					
				elif pauseSelect[1] == True:
					return currentPauseScreen, False, 2
					
				elif pauseSelect[2] == True:
					return currentPauseScreen, False, 0
					
			elif event.key == pygame.K_UP:
				if pauseSelect[0] == True: #Resume Selected
					pauseSelect[0] = False
					pauseSelect[2] = True
					currentPauseScreen = pauseMenuExit
				
				elif pauseSelect[1] == True: #Restart Selected
					pauseSelect[1] = False
					pauseSelect[0] = True
					currentPauseScreen = pauseMenuResume
					
				elif pauseSelect[2] == True: #Exit Selected
					pauseSelect[2] = False
					pauseSelect[1] = True
					currentPauseScreen = pauseMenuRestart
					
			elif event.key == pygame.K_DOWN:
				print 'Turn down for what'
				if pauseSelect[0] == True: #Resume Selected
					pauseSelect[0] = False
					pauseSelect[1] = True
					currentPauseScreen = pauseMenuRestart
						
				elif pauseSelect[1] == True: #Restart Selected
					pauseSelect[1] = False
					pauseSelect[2] = True
					currentPauseScreen = pauseMenuExit
					
				elif pauseSelect[2] == True: #Exit Selected
					pauseSelect[2] = False
					pauseSelect[0] = True
					currentPauseScreen = pauseMenuResume
		
	return currentPauseScreen, True, True

def processPlayerEvents(player, gameRunning):
	gameRunning = True
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			#print pygame.key.name(event.key)
			if event.key == pygame.K_ESCAPE:
				gameRunning = False
				gameRunning = pauseScreen()
				
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
				
def mainGameProcess():
	gameRunning = True
	for i in game.gameObjects:
		i.flag() 
	game.wave = 0
	game.frame = 0
	game.d = None	
	
	while gameRunning:
		clock.tick(60)
		gameRunning = processPlayerEvents(player, gameRunning)
		if sidebar.lives == 0:
			gameRunning = gameOverScreen()
		screen.blit(levelOneBackground, levelOneBackground.get_rect(), [0, 0, 600, 800])
		
		if game.wave == 0:
			if game.d not in game.gameObjects or game.d is None:
				if game.d is None:
					game.d = Dialogue("penguin_ava1", "Bleh", (200,255,255), game, player, 1)
				elif game.d.ref == 1:
					game.d = Dialogue("penguin_ava1", "Meh", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 2:
					game.d = Dialogue("penguin_ava1", "Bleh", (200,255,255), game, player, game.d.ref + 1, 4)
				else:
					game.frame = 0
					game.wave += 1
		
		if game.wave == 5: #level 1 game.wave 5
			if game.frame==30:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==60:
				SeagullA(Vector(100,-10),game,player,7)
			if game.frame==90:
				SeagullA(Vector(400,-10),game,player,6)
			if game.frame==100:
				SeagullA(Vector(200,-10),game,player,5)
			if game.frame==110:
				SeagullA(Vector(300,-10),game,player,8)
			if game.frame==120:
				SeagullA(Vector(500,-10),game,player,9)
			if game.frame==130:
				SeagullA(Vector(100,-10),game,player,10)
			if game.frame==170:
				PelicanA(Vector(100,-10),game,player,10,7)
			if game.frame==200:
				PelicanA(Vector(100,-10),game,player,10,7)
			if game.frame==240:
				PelicanA(Vector(100,-10),game,player,10,7)
			if game.frame==270:
				PelicanA(Vector(100,-10),game,player,10,7)
			if game.frame==250:
				SeagullA(Vector(300,-10),game,player,15)
			if game.frame==300:
				PelicanA(Vector(100,-10),game,player,10,7)
			if game.frame==300:
				SeagullA(Vector(200,-10),game,player,15)
			if game.frame==350:
				SeagullA(Vector(300,-10),game,player,10)
			if game.frame==400:
				SeagullA(Vector(500,-10),game,player,11)
			if game.frame==450:
				SeagullA(Vector(200,-10),game,player,13)
			if game.frame==470:
				PelicanB(Vector(500,780),game,player,10,7)
			if game.frame==500:
				PelicanB(Vector(500,780),game,player,10,7)
			if game.frame==500:
				SeagullA(Vector(400,-10),game,player,12)
			if game.frame==530:
				PelicanB(Vector(500,780),game,player,10,7)
			if game.frame==550:
				SeagullA(Vector(100,-10),game,player,15)
			if game.frame==560:
				PelicanB(Vector(500,780),game,player,10,7)
			if game.frame==600:
				SeagullA(Vector(500,-10),game,player,12)
			if game.frame==590:
				PelicanB(Vector(500,780),game,player,10,7)
			if game.frame==620:
				PelicanB(Vector(500,780),game,player,10,7)
			if game.frame==800:
				game.wave += 1
				game.frame = 0
		
		
		if game.wave == 6: #level 1 game.wave 6
			if game.frame==30:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==50:
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,5)
				SeagullA(Vector(500,-10),game,player,5)
			if game.frame==90:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==150:
				PelicanC(Vector(500,-10),game,player,20,7)
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,5)
				SeagullA(Vector(500,-10),game,player,5)
			if game.frame==210:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==240:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==250:
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,5)
				SeagullA(Vector(500,-10),game,player,5)
			if game.frame==270:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==300:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==330:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==350:
				SeagullA(Vector(100,-10),game,player,5)
				SeagullA(Vector(200,-10),game,player,6)
				SeagullA(Vector(300,-10),game,player,5)
				SeagullA(Vector(400,-10),game,player,4)
				SeagullA(Vector(500,-10),game,player,5)
			if game.frame==360:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==390:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==420:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==450:
				PelicanC(Vector(500,-10),game,player,20,7)
				SeagullA(Vector(100,-10),game,player,8)
				SeagullA(Vector(200,-10),game,player,5)
				SeagullA(Vector(300,-10),game,player,9)
				SeagullA(Vector(400,-10),game,player,2)
				SeagullA(Vector(500,-10),game,player,5)
			if game.frame==480:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==510:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==540:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==550:
				SeagullA(Vector(100,-10),game,player,5)
			if game.frame==556:
				SeagullA(Vector(200,-10),game,player,5)
			if game.frame==560:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==552:
				SeagullA(Vector(400,-10),game,player,5)
			if game.frame==558:
				SeagullA(Vector(500,-10),game,player,5)
			if game.frame==570:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==600:
				PelicanC(Vector(500,-10),game,player,20,7)
			if game.frame==656:
				SeagullA(Vector(100,-10),game,player,7)
			if game.frame==650:
				SeagullA(Vector(200,-10),game,player,9)
			if game.frame==658:
				SeagullA(Vector(300,-10),game,player,6)
			if game.frame==654:
				SeagullA(Vector(400,-10),game,player,5)
			if game.frame==652:
				SeagullA(Vector(500,-10),game,player,8)
			if game.frame==800:
				game.wave += 1
				game.frame = 0
		
		
		if game.wave == 2: #level 1 game.wave 2
			if game.frame==40:
				SeagullA(Vector(300,-10),game,player,9)
			if game.frame==80:
				SeagullB(Vector(400,790),game,player,9)
			if game.frame==120:
				SeagullA(Vector(200,-10),game,player,8)
			if game.frame==160:
				SeagullA(Vector(300,-10),game,player,9)
			if game.frame==200:
				SeagullB(Vector(200,790),game,player,8)
			if game.frame==240:
				SeagullA(Vector(500,-10),game,player,9)
			if game.frame==280:
				SeagullB(Vector(400,790),game,player,8)
			if game.frame==320:
				SeagullA(Vector(100,-10),game,player,9)
			if game.frame==360:
				SeagullB(Vector(100,790),game,player,8)
			if game.frame==400:
				SeagullA(Vector(500,-10),game,player,9)
			if game.frame==440:
				SeagullB(Vector(300,790),game,player,9)
			if game.frame==480:
				SeagullA(Vector(200,-10),game,player,8)
			if game.frame==520:
				SeagullB(Vector(500,790),game,player,9)
			if game.frame==560:
				SeagullA(Vector(100,-10),game,player,9)
			if game.frame==600:
				SeagullB(Vector(400,790),game,player,9)
			if game.frame==800:
				game.wave += 1
				game.frame = 0
		
		
		if game.wave == 1: #level 1 game.wave 1
			if game.frame==50:
				SeagullA(Vector(100,-10),game,player,3)
			if game.frame==100:
				SeagullA(Vector(400,-10),game,player,4)
			if game.frame==150:
				SeagullA(Vector(200,-10),game,player,3)
			if game.frame==200:
				SeagullA(Vector(400,-10),game,player,4)
			if game.frame==250:
				SeagullA(Vector(100,-10),game,player,3)
			if game.frame==300:
				SeagullA(Vector(500,-10),game,player,4)
			if game.frame==350:
				SeagullA(Vector(300,-10),game,player,4)
			if game.frame==400:
				SeagullA(Vector(500,-10),game,player,4)
			if game.frame==450:
				SeagullA(Vector(300,-10),game,player,4)
			if game.frame==500:
				SeagullA(Vector(100,-10),game,player,5)
			if game.frame==550:
				SeagullA(Vector(500,-10),game,player,4)
			if game.frame==600:
				SeagullA(Vector(400,-10),game,player,5)
			if game.frame==650:
				SeagullA(Vector(100,-10),game,player,6)
			if game.frame==800:
				game.wave += 1
				game.frame = 0
		
		
		if game.wave == 3: #level 1 game.wave 3
			if game.frame==30:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==50:
				PelicanA(Vector(100,-10),game,player,20,7)
			if game.frame==90:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==150:
				PelicanA(Vector(100,-10),game,player,20,7)
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==210:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==250:
				PelicanA(Vector(100,-10),game,player,20,7)
			if game.frame==270:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==330:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==350:
				PelicanA(Vector(100,-10),game,player,20,7)
			if game.frame==390:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==450:
				PelicanA(Vector(100,-10),game,player,20,7)
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==510:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==550:
				PelicanA(Vector(100,-10),game,player,20,7)
			if game.frame==570:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==800:
				game.wave += 1
				game.frame = 0
		
		
		if game.wave == 4: #level 1 game.wave 4
			if game.frame==30:
				SeagullA(Vector(100,-10),game,player,20)
				SeagullA(Vector(200,-10),game,player,20)
				SeagullA(Vector(300,-10),game,player,20)
				SeagullA(Vector(400,-10),game,player,20)
				SeagullA(Vector(500,-10),game,player,20)
				SeagullA(Vector(150,-10),game,player,20)
				SeagullA(Vector(250,-10),game,player,20)
				SeagullA(Vector(350,-10),game,player,20)
				SeagullA(Vector(450,-10),game,player,20)
			if game.frame==100:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if game.frame==130:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==150:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==190:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==200:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if game.frame==250:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==300:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if game.frame==310:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==370:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==400:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if game.frame==430:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==490:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==500:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if game.frame==550:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==600:
				PelicanC(Vector(100,-10),game,player,10,7)
				PelicanC(Vector(500,-10),game,player,10,7)
			if game.frame==610:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==670:
				SeagullA(Vector(300,-10),game,player,5)
			if game.frame==800:
				game.wave += 1
				game.frame = 0
		
		
		if game.wave == 7: #level 1 boss dialogue
			wave += 1
			
			
		if game.wave == 8: #level 1 boss: albatross
			wave += 1
		
		
		if game.wave == 9: #level 1 post boss dialogue
			wave += 1
		
		
		if game.wave == 10: #level 2 game.wave 1
			if game.frame==30:
				HummingbirdA(Vector(300,-10),game,player,1,2,50)
			if game.frame==60:
				HummingbirdA(Vector(400,-10),game,player,1,2,50)
			if game.frame==90:
				HummingbirdA(Vector(500,-10),game,player,1,3,50)
			if game.frame==120:
				HummingbirdA(Vector(200,-10),game,player,1,3,50)
			if game.frame==150:
				HummingbirdA(Vector(500,-10),game,player,1,4,50)
			if game.frame==180:
				HummingbirdA(Vector(100,-10),game,player,1,4,50)
			if game.frame==210:
				HummingbirdA(Vector(200,-10),game,player,1,5,50)
			if game.frame==240:
				HummingbirdA(Vector(300,-10),game,player,1,5,50)
			if game.frame==270:
				HummingbirdA(Vector(400,-10),game,player,1,6,50)
			if game.frame==300:
				HummingbirdA(Vector(300,-10),game,player,1,6,50)
			if game.frame==330:
				HummingbirdA(Vector(500,-10),game,player,1,7,50)
			if game.frame==360:
				HummingbirdA(Vector(100,-10),game,player,1,7,50)
			if game.frame==390:
				HummingbirdA(Vector(200,-10),game,player,1,8,50)
			if game.frame==420:
				HummingbirdA(Vector(400,-10),game,player,1,8,50)
			if game.frame==450:
				HummingbirdA(Vector(300,-10),game,player,1,9,50)
			if game.frame==480:
				HummingbirdA(Vector(200,-10),game,player,1,9,50)
			if game.frame==610:
				HummingbirdA(Vector(500,-10),game,player,1,10,50)
				
				
		if game.wave == 11: #level 2 game.wave 2
			if game.frame==30: 
				HummingbirdC(Vector(300,-10),game,player,1,5,30)
			if game.frame==60:
				HummingbirdC(Vector(100,-10),game,player,-1,4,30)
			if game.frame==100:
				HummingbirdB(Vector(400,-10),game,player,1,8,40)
			if game.frame==110:
				HummingbirdB(Vector(200,-10),game,player,-1,9,40)
			if game.frame==140:
				DoveB(Vector(300,-10),game,player,50,9)
			if game.frame==200:
				DoveA(Vector(300,-10),game,player)
				DoveA(Vector(100,-10),game,player)
				DoveA(Vector(500,-10),game,player)
			if game.frame==250:
				HummingbirdA(Vector(100,-10),game,player,1,5,30)
			if game.frame==300:
				HummingbirdA(Vector(300,-10),game,player,-1,6,30)
			if game.frame==350:
				HummingbirdA(Vector(400,-10),game,player,1,5,30)
			if game.frame==400:
				HummingbirdA(Vector(200,-10),game,player,-1,6,30)
			if game.frame==500:
				DoveA(Vector(300,-10),game,player)
			if game.frame==530:
				DoveB(Vector(300,-10),game,player,50,9)
				DoveA(Vector(200,-10),game,player)
				DoveA(Vecotr(400,-10),game,player)
			if game.frame==560:
				HummingbirdA(Vector(200,-10),game,player,1,6,30)
				HummingbirdA(Vector(400,-10),game,player,-1,6,30)
		
		
		if game.wave == 12: #Level 2 game.wave 3
			if game.frame==30:
				DoveA(Vector(300,-10),game,player)
				DoveA(Vector(200,-10),game,player)
				DoveA(Vector(100,-10),game,player)
				DoveA(Vector(400,-10),game,player)
				DoveA(Vector(500,-10),game,player)
			if game.frame==60:
				HummingbirdA(Vector(200,-10),game,player,1,6,30)
				HummingbirdA(Vector(400,-10),game,player,1,6,30)
			if game.frame==90:
				DoveB(Vector(500,-10),game,player,50,9)
				DoveB(Vector(100,-10),game,player,50,9)
			if game.frame==120:
				HummingbirdC(Vector(200,-10),game,player,1,3,30)
			if game.frame==150:
				HummingbirdC(Vector(400,-10),game,player,-1,4,30)
				DoveB(Vector(500,-10),game,player,50,9)
			if game.frame==180:
				HummingbirdC(Vector(400,-10),game,player,1,3,30)
			if game.frame==200:
				DoveA(Vector(200,-10),game,player)
				DoveA(Vector(400,-10),game,player)
			if game.frame==210:
				HummingbirdC(Vector(100,-10),game,player,-1,4,30)
			if game.frame==240:
				HummingbirdC(Vector(500,-10),game,player,1,3,30)
			if game.frame==250:
				DoveB(Vector(300,-10),game,player,50,9)
			if game.frame==270:
				HummingbirdB(Vector(200,-10),game,player,1,10,60)
				HummingbirdB(Vector(400,-10),game,player,-1,10,60)
			if game.frame==300:
				DoveB(Vector(100,-10),game,player,50,9)
			if game.frame==350:
				DoveB(Vector(400,-10),game,player,50,9)
			if game.frame==400:
				DoveB(Vector(300,-10),game,player,50,9)
			if game.frame==430:
				HummingbirdC(Vector(100,-10),game,player,1,4,30)
			if game.frame==460:
				HummingbirdB(Vector(500,-10),game,player,1,5,30)
			if game.frame==500:
				DoveB(Vector(200,-10),game,player,50,9)
			if game.frame==530:
				HummingbirdA(Vector(200,-10),game,player,1,10,30)
			if game.frame==560:
				HummingbirdA(Vector(300,-10),game,player,-1,11,30)
		
		
		if game.wave == 13: #level 2 game.wave 4
			if game.frame==30:
				HummingbirdA(Vector(200,-10),game,player,1,5,30)
				HummingbirdA(Vector(400,-10),game,player,-1,5,30)
			if game.frame==90:
				HummingbirdA(Vector(100,-10),game,player,1,6,30)
				HummingbirdA(Vector(500,-10),game,player,-1,6,30)
			if game.frame==150:
				HummingbirdA(Vector(200,-10),game,player,1,7,30)
				HummingbirdA(Vector(400,-10),game,player,-1,7,30)
				DoveA(Vector(300,-10),game,player)
			if game.frame==210:
				HummingbirdA(Vector(100,-10),game,player,1,8,30)
				HummingbirdA(Vector(500,-10),game,player,-1,8,30)
				DoveA(Vector(300,-10),game,player)
			if game.frame==270:
				HummingbirdB(Vector(200,-10),game,player,1,7,30)
				HummingbirdB(Vector(400,-10),game,player,1,7,30)
				DoveA(Vector(300,-10),game,player)
			if game.frame==330:
				HummingbirdB(Vector(100,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveA(Vector(300,-10),game,player)
			if game.frame==390:
				HummingbirdB(Vector(200,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveA(Vector(100,-10),game,player)
				DoveA(Vector(500,-10),game,player)
			if game.frame==450:
				HummingbirdB(Vector(100,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveA(Vector(200,-10),game,player)
				DoveA(Vector(300,-10),game,player)
				DoveA(Vector(400,-10),game,player)
			if game.frame==510:
				HummingbirdB(Vector(200,-10),game,player,1,9,30)
				HummingbirdB(Vector(400,-10),game,player,-1,9,30)
				DoveB(Vector(300,-10),game,player, 50,9)
			if game.frame==570:
				HummingbirdB(Vector(100,-10),game,player,1,9,30)
				HummingbirdB(Vector(500,-10),game,player,-1,9,30)
				DoveB(Vector(200,-10),game,player,50,9)
				DoveB(Vector(400,-10),game,player,50,9)
		
		
		if game.wave == 14: #Level 2 game.wave 5
			if game.frame==30:
				DoveC(Vector(300,-10),game,player,5)
			if game.frame==50:
				HummingbirdB(Vector(300,-10),game,player,1,4,30)
			if game.frame==60:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==90:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==100:
				HummingbirdB(Vector(400,-10),game,player,-1,5,30)
			if game.frame==120:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==150:
				DoveC(Vector(100,-10),game,player,5)
				HummingbirdB(Vector(200,-10),game,player,1,5,30)
			if game.frame==180:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==200:
				HummingbirdB(Vector(300,-10),game,player,-1,5,30)
			if game.frame==210:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==240:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==250:
				HummingbirdB(Vector(400,-10),game,player,1,5,30)
			if game.frame==270:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==300:
				DoveC(Vector(400,-10),game,player,5)
				HummingbirdB(Vector(100,-10),game,player,-1,5,30)
			if game.frame==330:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==350:
				HummingbirdB(Vector(500,-10),game,player,1,5,30)
			if game.frame==360:
				DoveC(Vector(100,-10),game,player,5)
			if game.frame==390:
				DoveC(Vector(300,-10),game,player,5)
			if game.frame==400:
				HummingbirdB(Vector(100,-10),game,player,-1,5,30)
			if game.frame==420:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==450:
				DoveC(Vector(400,-10),game,player,5)
				HummingbirdB(Vector(200,-10),game,player,1,5,30)
			if game.frame==480:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==500:
				HummingbirdB(Vector(100,-10),game,player,-1,5,30)
			if game.frame==510:
				DoveC(Vector(300,-10),game,player,5)
			if game.frame==540:
				DoveC(Vector(400,-10),game,player,5)
			if game.frame==550:
				HummingbirdB(Vector(300,-10),game,player,1,5,30)
			if game.frame==570:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==600:
				DoveC(Vector(500,-10),game,player,5)
				HummingbirdB(Vector(200,-10),game,player,1,5,30)
		
		
		if game.wave == 15: #Level 2 game.wave 6
			if game.frame==30:
				DoveA(Vector(100,-10),game,player)
			if game.frame==50:
				DoveC(Vector(200,-10),game,player,4)
			if game.frame==60:
				DoveA(Vector(300,-10),game,player)
			if game.frame==90:
				DoveA(Vector(200,-10),game,player)
			if game.frame==100:
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==120:
				DoveA(Vector(100,-10),game,player)
			if game.frame==150:
				DoveA(Vector(400,-10),game,player)
				DoveC(Vector(500,-10),game,player,5)
			if game.frame==180:
				DoveA(Vector(200,-10),game,player)
			if game.frame==200:
				DoveC(Vector(400,-10),game,player,5)
			if game.frame==210:
				DoveA(Vector(500,-10),game,player)
			if game.frame==240:
				DoveA(Vector(300,-10),game,player)
			if game.frame==250:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==270:
				DoveA(Vector(400,-10),game,player)
			if game.frame==300:
				DoveA(Vector(200,-10),game,player)
				DoveC(Vector(100,-10),game,player,5)
			if game.frame==330:
				DoveA(Vector(500,-10),game,player)
			if game.frame==350:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==360:
				DoveA(Vector(300,-10),game,player)
			if game.frame==390:
				DoveA(Vector(200,-10),game,player)
			if game.frame==400:
				DoveC(Vector(300,-10),game,player,5)
			if game.frame==420:
				DoveA(Vector(100,-10),game,player)
			if game.frame==450:
				DoveA(Vector(400,-10),game,player)
				DoveC(Vector(20,-10),game,player,5)
			if game.frame==480:
				DoveA(Vector(100,-10),game,player)
			if game.frame==500:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==510:
				DoveA(Vector(400,-10),game,player)
			if game.frame==540:
				DoveA(Vector(300,-10),game,player)
			if game.frame==550:
				DoveC(Vector(200,-10),game,player,5)
			if game.frame==570:
				DoveA(Vector(400,-10),game,player)
			if game.frame==600:
				DoveA(Vector(200,-10),game,player)
				DoveC(Vector(500,-10),game,player,5)
		
		
		if game.wave == 16: #level 2 boss dialogue
			wave += 1
			
			
		if game.wave == 17: #level 2 boss: albatross
			wave += 1
		
		
		if game.wave == 18: #level 2 post boss dialogue
			wave += 1
		
		
		if game.wave == 19: #Level 3 game.wave 1
			if game.frame==30:
				ToucanA(Vector(300,-10),game,player,5,5,15)
			if game.frame==60:
				ToucanA(Vector(500,-10),game,player,4,5,15)
			if game.frame==90:
				ToucanA(Vector(100,-10),game,player,4,5,15)
			if game.frame==120:
				ToucanA(Vector(200,-10),game,player,4,5,15)
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if game.frame==150:
				ToucanA(Vector(300,-10),game,player,6,5,15)
			if game.frame==180:
				ToucanA(Vector(100,-10),game,player,5,5,15)
			if game.frame==210:
				ToucanA(Vector(500,-10),game,player,5,5,15)
			if game.frame==240:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if game.frame==270:
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if game.frame==300:
				ToucanA(Vector(200,-10),game,player,6,5,15)
			if game.frame==330:
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if game.frame==360:
				ToucanA(Vector(500,-10),game,player,6,5,15)
			if game.frame==390:
				ToucanA(Vector(300,-10),game,player,6,5,15)
			if game.frame==420:
				ToucanA(Vector(500,-10),game,player,6,5,15)
			if game.frame==450:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if game.frame==480:
				ToucanA(Vector(300,-10),game,player,5,5,15)
			if game.frame==510:
				ToucanA(Vector(400,-10),game,player,6,5,15)
			if game.frame==540:
				ToucanA(Vector(500,-10),game,player,5,5,15)
			if game.frame==570:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if game.frame==600:
				ToucanA(Vector(500,-10),game,player,6,5,15)
		
		
		if game.wave == 20: #Level 3 game.wave 2
			if game.frame==30:
				ToucanB(Vector(300,-10),game,player,5,15)
			if game.frame==90:
				ToucanB(Vector(100,-10),game,player,5,15)
				ToucanB(Vector(500,-10),game,player,5,15)
			if game.frame==150:
				ToucanB(Vector(200,-10),game,player,7,15)
			if game.frame==210:
				ToucanB(Vector(400,-10),game,player,7,15)
			if game.frame==270:
				ToucanB(Vector(200,-10),game,player,6,15)
				ToucanB(Vector(500,-10),game,player,6,15)
			if game.frame==330:
				ToucanB(Vector(300,-10),game,player,8,15)
			if game.frame==390:
				ToucanB(Vector(400,-10),game,player,7,15)
			if game.frame==450:
				ToucanB(Vector(300,-10),game,player,11,15)
			if game.frame==510:
				ToucanB(Vector(500,-10),game,player,11,15)
			if game.frame==570:
				ToucanB(Vector(100,-10),game,player,8,15)
		
		
		if game.wave == 21: #Level 3 game.wave 3
			if game.frame==30:
				BlueparrotA(Vector(300,-10),game,player,1,4,30)
			if game.frame==60:
				BlueparrotA(Vector(100,-10),game,player,-1,3,30)
			if game.frame==90:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if game.frame==120:
				BlueparrotA(Vector(200,-10),game,player,-1,3,30)
			if game.frame==150:
				BlueparrotA(Vector(100,-10),game,player,1,3,30)
			if game.frame==180:
				BlueparrotA(Vector(400,-10),game,player,-1,3,30)
			if game.frame==210:
				BlueparrotA(Vector(100,-10),game,player,1,4,30)
			if game.frame==240:
				BlueparrotA(Vector(200,-10),game,player,-1,4,30)
			if game.frame==270:
				BlueparrotA(Vector(400,-10),game,player,1,4,30)
			if game.frame==300:
				BlueparrotA(Vector(200,-10),game,player,-1,4,30)
			if game.frame==330:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if game.frame==360:
				BlueparrotA(Vector(100,-10),game,player,-1,4,30)
			if game.frame==390:
				BlueparrotA(Vector(300,-10),game,player,1,4,30)
			if game.frame==420:
				BlueparrotA(Vector(500,-10),game,player,-1,3,30)
			if game.frame==450:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if game.frame==480:
				BlueparrotA(Vector(200,-10),game,player,-1,3,30)
			if game.frame==510:
				BlueparrotA(Vector(300,-10),game,player,1,3,30)
			if game.frame==540:
				BlueparrotA(Vector(400,-10),game,player,-1,3,30)
			if game.frame==570:
				BlueparrotA(Vector(500,-10),game,player,1,3,30)
			if game.frame==600:
				BlueparrotA(Vector(200,-10),game,player,-1,4,30)
		
		
		if game.wave == 22: #Level 3 game.wave 4
			if game.frame==30:
				ToucanA(Vector(100,-10),game,player,6,5,15)
				ToucanA(Vector(200,-10),game,player,6,5,15)
				ToucanA(Vector(300,-10),game,player,6,5,15)
				ToucanA(Vector(400,-10),game,player,6,5,15)
				ToucanA(Vector(500,-10),game,player,6,5,15)
			if game.frame==130:
				ToucanA(Vector(300,-10),game,player,15,5,15)
			if game.frame==260:
				ToucanB(Vector(100,-10),game,player,10,15)
				ToucanB(Vector(500,-10),game,player,10,15)
			if game.frame==480:
				ToucanA(Vector(200,-10),game,player,7,5,15)
				ToucanA(Vector(400,-10),game,player,7,5,15)
				BlueparrotA(Vector(300,-10),game,player,1,4,30)
			if game.frame==540:
				BlueparrotA(Vector(500,-10),game,player,-1,5,30)
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
			if game.frame==570:
				BlueparrotA(Vector(200,-10),game,player,1,5,30)
				BlueparrotA(Vector(400,-10),game,player,1,5,30)
			if game.frame==600:
				BlueparrotA(Vector(300,-10),game,player,-1,5,30)
		
		
		if game.wave == 23: #Level 3 game.wave 5
			if game.frame==30:
				BlueparrotB(Vector(300,-10),game,player,1,30,7)
			if game.frame==60:
				BlueparrotB(Vector(500,-10),game,player,-1,30,7)
			if game.frame==90:
				BlueparrotB(Vector(100,-10),game,player,1,30,7)
			if game.frame==120:
				BlueparrotB(Vector(400,-10),game,player,-1,30,7)
			if game.frame==150:
				BlueparrotB(Vector(200,-10),game,player,1,30,7)
			if game.frame==180:
				BlueparrotA(Vector(300,-10),game,player,-1,5,30)
			if game.frame==210:
				BlueparrotA(Vector(300,-10),game,player,1,5,30)
			if game.frame==240:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if game.frame==270:
				BlueparrotA(Vector(500,-10),game,player,1,5,30)
			if game.frame==300:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if game.frame==330:
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if game.frame==360:
				BlueparrotB(Vector(400,-10),game,player,-1,30,7)
			if game.frame==390:
				BlueparrotA(Vector(500,-10),game,player,1,5,30)
			if game.frame==420:
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
			if game.frame==450:
				BlueparrotA(Vector(300,-10),game,player,1,5,30)
			if game.frame==480:
				BlueparrotA(Vector(200,-10),game,player,-1,5,30)
			if game.frame==510:
				BlueparrotA(Vector(400,-10),game,player,1,5,30)
			if game.frame==540:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if game.frame==570:
				BlueparrotA(Vector(300,-10),game,player,1,5,30)
			if game.frame==600:
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
		
		
		if game.wave == 24: #Level 3 game.wave 6
			if game.frame==30:
				ToucanA(Vector(100,-10),game,player,5,4,30)  #For some reason that 4 needs to be a 4 to spawn 3 bucks. don't ask why. I don't know  --Nick
			if game.frame==50:
				BlueparrotB(Vector(400,-10),game,player,1,30,7)
			if game.frame==90:
				ToucanA(Vector(200,-10),game,player,5,4,30)
			if game.frame==150:
				ToucanA(Vector(400,-10),game,player,5,4,30)
				BlueparrotB(Vector(300,-10),game,player,-1,30,7)
			if game.frame==210:
				ToucanA(Vector(100,-10),game,player,5,4,30)
			if game.frame==250:
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if game.frame==270:
				ToucanA(Vector(400,-10),game,player,5,4,30)
			if game.frame==330:
				ToucanA(Vector(500,-10),game,player,5,4,30)
			if game.frame==350:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
			if game.frame==390:
				ToucanA(Vector(400,-10),game,player,5,4,30)
			if game.frame==450:
				ToucanA(Vector(100,-10),game,player,5,4,30)
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if game.frame==510:
				ToucanA(Vector(300,-10),game,player,5,4,30)
			if game.frame==550:
				BlueparrotB(Vector(200,-10),game,player,-1,30,7)
			if game.frame==570:
				ToucanA(Vector(100,-10),game,player,5,4,30)
		
		
		if game.wave == 25: #level 1 boss dialogue
			wave += 1
			
			
		if game.wave == 26: #level 1 boss: albatross
			wave += 1
		
		
		if game.wave == 27: #level 1 post boss dialogue
			wave += 1
			
			
		if game.wave == 28:
			print "GG"
			return
		
		#update 
		game.update()
		#collision
		
		#draw
		game.draw()
		sidebar.draw(screen)
		pygame.display.flip()
		game.frame+=1

def mainMenuEvents(currentMenuScreen, mainMenuNewGame, mainMenuHighScores, mainMenuExit):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			
			if event.key == pygame.K_RETURN:
				if screenSelect[0] == True:
					mainGameProcess()
					
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
	
