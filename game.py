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

mainMenuNewGame = Image.get('MenuNewGame')
mainMenuHighScores = Image.get('MenuHighScores')
mainMenuExit = Image.get('MenuExit')
pauseMenuResume = Image.get('PauseMenuResume')
pauseMenuRestart = Image.get('PauseMenuRestart')
pauseMenuExit = Image.get('PauseMenuExit')
gameOverRetry = Image.get('GameOverRetry')
gameOverExit = Image.get('GameOverExit')
highScoreBackground = Image.get('HighScoreBackground')
highScoresFile = open('scores.txt', 'r+')
sidebar = Sidebar()
game = Engine(screen, sidebar)
Enemy.setSidebar(sidebar)
player = Player(game)


# Initializing stuff on boot
clock = pygame.time.Clock()
game.frame = 0
gameOpen = True
currentMenuScreen = mainMenuNewGame
currentPauseScreen = pauseMenuResume
currentQuitScreen = gameOverRetry
screenSelect = [True, False, False]
pauseSelect = [True, False, False]
quitSelect = [True, False]
highScores = []
for score in highScoresFile:
	highScores.append(score)
	
scoresFont = pygame.font.SysFont("monospace", 18)

def gameOverScreen():
	currentQuitScreen = gameOverRetry
	retry = False
	quit = False
	while True:
		if retry:
			game.restart('soft')
			sidebar.lives = 4
			return True
		elif quit:
			sidebar.lives = 4
			return False
		clock.tick(60)
		screen.blit(currentQuitScreen, (250,325))
		currentQuitScreen, retry, quit = processGameOverEvents(currentQuitScreen, gameOverRetry, gameOverExit)
		pygame.display.flip()

def processGameOverEvents(currentQuitScreen, gameOverRetry, gameOverExit):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
				
			elif event.key == pygame.K_RETURN:
				if quitSelect[0] == True:
					# retry level
					return currentQuitScreen, True, False
					
				elif quitSelect[1] == True:
					# quit to main menu
					return currentQuitScreen, False, True
					
					
			elif event.key == pygame.K_UP:
				if quitSelect[0] == True:
					quitSelect[0] = False
					quitSelect[1] = True
					currentQuitScreen = gameOverExit
					
				elif quitSelect[1] == True:
					quitSelect[1] = False
					quitSelect[0] = True
					currentQuitScreen = gameOverRetry
					
			elif event.key == pygame.K_DOWN:
				if quitSelect[0] == True:
					quitSelect[0] = False
					quitSelect[1] = True
					currentQuitScreen = gameOverExit
					
				elif quitSelect[1] == True:
					quitSelect[1] = False
					quitSelect[0] = True
					currentQuitScreen = gameOverRetry
					
	return currentQuitScreen, False, False

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
				
			if event.key == pygame.K_z:
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

			if event.key == pygame.K_z:
				player.firing = False
				
			if event.key == pygame.K_LSHIFT:
				player.focus = False
	
	return gameRunning
				
def mainGameProcess():
	gameRunning = True
	game.restart()
	game.wave = 20
	game.levelBackground = game.levelThreeBackground
	
	while gameRunning:
		clock.tick(60)
		gameRunning = processPlayerEvents(player, gameRunning)
		if sidebar.lives == 0:
			gameRunning = gameOverScreen()
		
		if game.wave == 0:
			if game.d not in game.gameObjects or game.d is None:
				if game.d is None:
					game.d = Dialogue("penguin_avi1", "(Hmmm... this jetpack handles better than I thought it would)", (200,255,255), game, player, 1)
				elif game.d.ref == 1:
					game.d = Dialogue("penguin_avi1", "(At this speed it will take me no time to get to the Caribbean! I'll be there in 5 minutes)", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 2:
					game.d = Dialogue("penguin_avi1", "(But why are the seagulls are throwing things at me?)", (200,255,255), game, player, game.d.ref + 1, 30)
				elif game.d.ref == 3:
					game.d = Dialogue("penguin_avi1", "(This might be more difficult that I thought...)", (200,255,255), game, player, game.d.ref + 1, 4)
				else:
					game.d = None
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
				SeagullA(Vector(300,-10),game,player,7)
			if game.frame==80:
				SeagullA(Vector(400,-10),game,player,7)
			if game.frame==120:
				SeagullA(Vector(200,-10),game,player,7)
			if game.frame==160:
				SeagullA(Vector(300,-10),game,player,7)
			if game.frame==200:
				SeagullB(Vector(200,790),game,player,7)
			if game.frame==240:
				SeagullA(Vector(500,-10),game,player,7)
			if game.frame==280:
				SeagullA(Vector(400,-10),game,player,7)
			if game.frame==320:
				SeagullB(Vector(100,790),game,player,7)
			if game.frame==360:
				SeagullA(Vector(100,-10),game,player,7)
			if game.frame==400:
				SeagullA(Vector(500,-10),game,player,7)
			if game.frame==440:
				SeagullB(Vector(300,790),game,player,7)
			if game.frame==480:
				SeagullA(Vector(200,-10),game,player,7)
			if game.frame==520:
				SeagullB(Vector(500,790),game,player,7)
			if game.frame==560:
				SeagullA(Vector(100,-10),game,player,7)
			if game.frame==600:
				SeagullA(Vector(400,-10),game,player,7)
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
				PelifcanC(Vector(500,-10),game,player,10,7)
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
			if game.d not in game.gameObjects or game.d is None and len([x for x in game.gameObjects if x.name == 'Bullet']) == 0:
				if game.d is None:
					game.boss = Albatross(Vector(300,-10),game,player)
					game.d = Dialogue("penguin_avi1", "(Darn...I think I'm lost. Hey there's an Albatros, maybe he will help me)", (200,255,255), game, player, 1)
				elif game.d.ref == 1:
					game.d = Dialogue("penguin_avi3", "Hey. Hey...HEY!!.. HEY!!!!! HELLO!!", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 2:
					game.d = Dialogue("albatross_avi1", "What? What could you possibly want?", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 3:
					game.d = Dialogue("penguin_avi3", "I need to go to the Caribbean and I might be a little lost... Can you help me?", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 4:
					game.d = Dialogue("albatross_avi1", "No.", (200,255,255), game, player, game.d.ref + 1, 30)
				elif game.d.ref == 5:
					game.d = Dialogue("penguin_avi3", "Please?", (200,255,255), game, player, game.d.ref + 1, 45)
				elif game.d.ref == 6:
					game.d = Dialogue("albatross_avi1", "...", (200,255,255), game, player, game.d.ref + 1, 100)
				elif game.d.ref == 7:
					game.d = Dialogue("penguin_avi1", "Do you not know where it is? Because if you don't thats okay. I don't really either.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 8:
					game.d = Dialogue("albatross_avi1", "...", (200,255,255), game, player, game.d.ref + 1, 100)
				elif game.d.ref == 9:
					game.d = Dialogue("penguin_avi1", "I need to get to the Caribbean. If you don't know how to get there, maybe you can-", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 10:
					game.d = Dialogue("albatross_avi4", "CRAWWWWWW. I've had enough of your incessant chattering.", (200,255,255), game, player, game.d.ref + 1, 4)
				else:
					game.d = None
					game.frame = 0
					game.wave += 1
			
			
		if game.wave == 8: #level 1 boss: albatross
			if game.boss not in game.gameObjects:
				game.boss = None
				game.wave += 1
		
		
		if game.wave == 9: #level 1 post boss dialogue
			if not game.levelFade and len([x for x in game.gameObjects if x.name == 'Bullet']) == 0:
				if game.d not in game.gameObjects or game.d is None:
					if game.d is None:
						game.d = Dialogue("penguin_avi1", "(I guess he really didn't know where the Caribbean was)", (200,255,255), game, player, 1)
					elif game.d.ref == 1:
						game.d = Dialogue("penguin_avi1", "(Maybe if I keep going in this direction someone else will help me)", (200,255,255), game, player, game.d.ref + 1, 4)
					else:
						game.d = None
						game.frame = 0
						game.levelFade = True
		
		
		if game.wave == 11: #level 2 game.wave 2
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
			if game.frame==800:
				game.frame=0
				game.wave+=1
				
				
		if game.wave == 12: #level 2 game.wave 3
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
				DoveA(Vector(400,-10),game,player)
			if game.frame==560:
				HummingbirdA(Vector(200,-10),game,player,1,6,30)
				HummingbirdA(Vector(400,-10),game,player,-1,6,30)
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 14: #Level 2 game.wave 5
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
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 15: #level 2 game.wave 4
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
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 13: #Level 2 game.wave 6
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
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 10: #Level 2 game.wave 1
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
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 16: #level 2 boss dialogue
			if game.d not in game.gameObjects or game.d is None and len([x for x in game.gameObjects if x.name == 'Bullet']) == 0:
				if game.d is None:
					game.boss = Flamingo(Vector(300,-10),game,player)
					game.d = Dialogue("flamingo_avi1", "What are you? I've never seen something like you in the sky before.", (200,255,255), game, player, 1)
				elif game.d.ref == 1:
					game.d = Dialogue("penguin_avi1", "I'm a Penguin.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 2:
					game.d = Dialogue("flamingo_avi1", "A Penguin?! In the sky?! Now that's unheard of.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 3:
					game.d = Dialogue("penguin_avi1", "I built a jet-pack.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 4:
					game.d = Dialogue("flamingo_avi2", "Do you think you are special?", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 5:
					game.d = Dialogue("penguin_avi1", "Umm.... What?", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 6:
					game.d = Dialogue("flamingo_avi3", "Insolence! Trying to upstage me! Me, the most beautiful Flamingo in the world!", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 7:
					game.d = Dialogue("penguin_avi1", "I'm not trying to upstage anyone.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 8:
					game.d = Dialogue("flamingo_avi3", "Of course you are. That's why you've come to challange me to see who the most graceful creature in the sky is!", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 9:
					game.d = Dialogue("penguin_avi1", "I didn't challenge anyone.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 10:
					game.d = Dialogue("flamingo_avi4", "LET THE CHALLENGE BEGIN!", (200,255,255), game, player, game.d.ref + 1, 4)
				else:
					game.d = None
					game.frame = 0
					game.wave += 1
			
			
		if game.wave == 17: #level 2 boss: flamingo
			if game.boss not in game.gameObjects:
				game.boss = None
				game.wave += 1
		
		
		if game.wave == 18: #level 2 post boss dialogue
			if not game.levelFade and len([x for x in game.gameObjects if x.name == 'Bullet']) == 0:
				if game.d not in game.gameObjects or game.d is None:
					if game.d is None:
						game.d = Dialogue("penguin_avi1", "(I really didn't challenge him)", (200,255,255), game, player, 1)
					elif game.d.ref == 1:
						game.d = Dialogue("penguin_avi1", "(I mean, I don't think I'm that graceful)", (200,255,255), game, player, game.d.ref + 1, 4)
					else:
						game.d = None
						game.frame = 0
						game.levelFade = True
		
		
		if game.wave == 19: #level 3 opening dialogue
			if not game.levelFade and game.d not in game.gameObjects or game.d is None:
				if game.d is None:
					MacawA(Vector(300,-10),game,player)
					game.d = Dialogue("macaw_avi1", "Now... what do we have here? I've never seen your kind before.", (200,255,255), game, player, 1)
				elif game.d.ref == 1:
					game.d = Dialogue("penguin_avi3", "I'm a penguin. I'm going to the Caribbean.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 2:
					game.d = Dialogue("macaw_avi1", "I'd recommend you find an alternate route. My boys here don't like strangers on our turf.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 3:
					game.d = Dialogue("penguin_avi1", "But the fastest way there is over the Jungle.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 4:
					game.d = Dialogue("macaw_avi3", "Look kid. I admire your spirit, but you're in the wrong neighborhood. Find a new route.", (200,255,255), game, player, game.d.ref + 1, 4)
				else:
					game.d = None
					game.frame = 0
					game.wave += 1
			
		
		if game.wave == 20: #Level 3 game.wave 1
			if game.frame==30:
				ToucanA(Vector(300,-10),game,player,5,5,15)
			if game.frame==60:
				ToucanA(Vector(500,-10),game,player,4,5,15)
				ToucanA(Vector(200,-10),game,player,5,5,15)
			if game.frame==90:
				ToucanA(Vector(100,-10),game,player,4,5,15)
			if game.frame==120:
				ToucanA(Vector(200,-10),game,player,4,5,15)
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if game.frame==150:
				ToucanA(Vector(300,-10),game,player,6,5,15)
			if game.frame==180:
				ToucanA(Vector(100,-10),game,player,5,5,15)
				ToucanA(Vector(400,-10),game,player,4,5,15)
			if game.frame==210:
				ToucanA(Vector(500,-10),game,player,5,5,15)
			if game.frame==240:
				ToucanA(Vector(100,-10),game,player,6,5,15)
				ToucanA(Vector(300,-10),game,player,5,5,15)
			if game.frame==270:
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if game.frame==300:
				ToucanA(Vector(200,-10),game,player,6,5,15)
				ToucanA(Vector(100,-10),game,player,5,5,15)
			if game.frame==330:
				ToucanA(Vector(400,-10),game,player,5,5,15)
			if game.frame==360:
				ToucanA(Vector(500,-10),game,player,6,5,15)
				ToucanA(Vector(200,-10),game,player,7,6,15)
			if game.frame==390:
				ToucanA(Vector(300,-10),game,player,6,5,15)
			if game.frame==420:
				ToucanA(Vector(500,-10),game,player,6,5,15)
				ToucanA(Vector(200,-10),game,player,7,5,15)
			if game.frame==450:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if game.frame==480:
				ToucanA(Vector(300,-10),game,player,5,5,15)
				ToucanA(Vector(200,-10),game,player,6,5,15)
			if game.frame==510:
				ToucanA(Vector(400,-10),game,player,6,5,15)
			if game.frame==540:
				ToucanA(Vector(500,-10),game,player,5,5,15)
				ToucanA(Vector(200,-10),game,player,6,5,15)
			if game.frame==570:
				ToucanA(Vector(100,-10),game,player,6,5,15)
			if game.frame==600:
				ToucanA(Vector(500,-10),game,player,6,5,15)
				ToucanA(Vector(200,-10),game,player,7,5,15)
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 21: #Level 3 game.wave 2
			if game.frame==30:
				ToucanB(Vector(300,-10),game,player,5,15)
			if game.frame==60:
				ToucanB(Vector(200,-10),game,player,5,15)
			if game.frame==90:
				ToucanB(Vector(100,-10),game,player,5,15)
				ToucanB(Vector(500,-10),game,player,5,15)
			if game.frame==120:
				ToucanB(Vector(300,-10),game,player,5,15)
			if game.frame==150:
				ToucanB(Vector(200,-10),game,player,7,15)
			if game.frame==180:
				ToucanB(Vector(100,-10),game,player,7,15)
			if game.frame==210:
				ToucanB(Vector(400,-10),game,player,7,15)
			if game.frame==240:
				ToucanB(Vector(100,-10),game,player,6,15)
			if game.frame==270:
				ToucanB(Vector(200,-10),game,player,6,15)
				ToucanB(Vector(500,-10),game,player,6,15)
			if game.frame==300:
				ToucanB(Vector(100,-10),game,player,7,15)
			if game.frame==330:
				ToucanB(Vector(300,-10),game,player,8,15)
			if game.frame==360:
				ToucanB(Vector(100,-10),game,player,8,15)
			if game.frame==390:
				ToucanB(Vector(400,-10),game,player,7,15)
			if game.frame==420:
				ToucanB(Vector(100,-10),game,player,10,15)
			if game.frame==450:
				ToucanB(Vector(300,-10),game,player,11,15)
			if game.frame==480:
				ToucanB(Vector(100,-10),game,player,11,15)
			if game.frame==510:
				ToucanB(Vector(500,-10),game,player,11,15)
			if game.frame==560:
				ToucanB(Vector(300,-10),game,player,10,15)
			if game.frame==570:
				ToucanB(Vector(100,-10),game,player,8,15)
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 22: #Level 3 game.wave 3
			if game.frame==30:
				BlueparrotA(Vector(300,-10),game,player,1,6,10)
			if game.frame==50:
				ToucanB(Vector(500,-10),game,player,8,30)
			if game.frame==60:
				BlueparrotA(Vector(100,-10),game,player,-1,5,10)
			if game.frame==90:
				BlueparrotA(Vector(300,-10),game,player,1,5,10)
			if game.frame==100:
				ToucanB(Vector(500,-10),game,player,8,30)
			if game.frame==120:
				BlueparrotA(Vector(200,-10),game,player,-1,5,10)
			if game.frame==150:
				BlueparrotA(Vector(100,-10),game,player,1,5,10)
				ToucanB(Vector(300,-10),game,player,8,30)
			if game.frame==180:
				BlueparrotA(Vector(400,-10),game,player,-1,5,10)
			if game.frame==200:
				ToucanB(Vector(500,-10),game,player,8,30)
			if game.frame==210:
				BlueparrotA(Vector(100,-10),game,player,1,6,10)
			if game.frame==240:
				BlueparrotA(Vector(200,-10),game,player,-1,6,10)
			if game.frame==250:
				ToucanB(Vector(100,-10),game,player,8,30)
			if game.frame==270:
				BlueparrotA(Vector(400,-10),game,player,1,6,10)
			if game.frame==300:
				BlueparrotA(Vector(200,-10),game,player,-1,6,10)
				ToucanB(Vector(500,-10),game,player,8,30)
			if game.frame==330:
				BlueparrotA(Vector(300,-10),game,player,1,5,10)
			if game.frame==350:
				ToucanB(Vector(500,-10),game,player,8,30)
			if game.frame==360:
				BlueparrotA(Vector(100,-10),game,player,-1,6,10)
			if game.frame==390:
				BlueparrotA(Vector(300,-10),game,player,1,6,10)
			if game.frame==400:
				ToucanB(Vector(100,-10),game,player,8,30)
			if game.frame==420:
				BlueparrotA(Vector(500,-10),game,player,-1,5,10)
			if game.frame==450:
				BlueparrotA(Vector(300,-10),game,player,1,5,10)
				ToucanB(Vector(400,-10),game,player,8,30)
			if game.frame==480:
				BlueparrotA(Vector(200,-10),game,player,-1,5,10)
			if game.frame==500:
				ToucanB(Vector(100,-10),game,player,8,30)
			if game.frame==510:
				BlueparrotA(Vector(300,-10),game,player,1,5,10)
			if game.frame==540:
				BlueparrotA(Vector(400,-10),game,player,-1,5,10)
			if game.frame==550:
				ToucanB(Vector(100,-10),game,player,8,30)
			if game.frame==570:
				BlueparrotA(Vector(500,-10),game,player,1,5,10)
			if game.frame==600:
				BlueparrotA(Vector(200,-10),game,player,-1,6,10)
				ToucanB(Vector(100,-10),game,player,8,30)
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 23: #Level 3 game.wave 4
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
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 24: #Level 3 game.wave 5
			if game.frame==30:
				BlueparrotB(Vector(300,-10),game,player,1,15,5)
			if game.frame==60:
				BlueparrotB(Vector(500,-10),game,player,-1,15,5)
				BlueparrotB(Vector(400,-10),game,player,1,15,5)
			if game.frame==90:
				BlueparrotB(Vector(100,-10),game,player,1,15,5)
			if game.frame==120:
				BlueparrotB(Vector(400,-10),game,player,-1,15,5)
				BlueparrotB(Vector(100,-10),game,player,1,15,5)
			if game.frame==150:
				BlueparrotB(Vector(200,-10),game,player,1,15,5)
			if game.frame==180:
				BlueparrotA(Vector(300,-10),game,player,-1,5,15)
				BlueparrotA(Vector(400,-10),game,player,1,5,15)
			if game.frame==210:
				BlueparrotA(Vector(200,-10),game,player,1,5,15)
			if game.frame==240:
				BlueparrotB(Vector(100,-10),game,player,-1,15,5)
				BlueparrotB(Vector(300,-10),game,player,1,15,5)
			if game.frame==270:
				BlueparrotA(Vector(500,-10),game,player,1,5,15)
			if game.frame==300:
				BlueparrotB(Vector(100,-10),game,player,-1,15,5)
				BlueparrotB(Vector(300,-10),game,player,1,15,5)
			if game.frame==330:
				BlueparrotB(Vector(500,-10),game,player,1,15,5)
			if game.frame==360:
				BlueparrotB(Vector(400,-10),game,player,-1,15,5)
				BlueparrotB(Vector(200,-10),game,player,1,15,5)
			if game.frame==390:
				BlueparrotA(Vector(500,-10),game,player,1,5,15)
			if game.frame==420:
				BlueparrotA(Vector(100,-10),game,player,-1,5,15)
				BlueparrotA(Vector(200,-10),game,player,1,5,15)
			if game.frame==450:
				BlueparrotA(Vector(300,-10),game,player,1,5,15)
			if game.frame==480:
				BlueparrotA(Vector(200,-10),game,player,-1,5,15)
				BlueparotA(Vector(500,-10),game,player,1,5,15)
			if game.frame==510:
				BlueparrotA(Vector(400,-10),game,player,1,5,15)
			if game.frame==540:
				BlueparrotB(Vector(100,-10),game,player,-1,15,5)
				BlueparrotB(Vector(200,-10),game,player,1,15,5)
			if game.frame==570:
				BlueparrotA(Vector(300,-10),game,player,1,5,15)
			if game.frame==600:
				BlueparrotA(Vector(100,-10),game,player,-1,5,15)
				BlueparrotA(Vector(100,-10),game,player,-1,5,30)
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 25: #Level 3 game.wave 6
			if game.frame==30:
				ToucanA(Vector(100,-10),game,player,5,4,30)  #For some reason that 4 needs to be a 4 to spawn 3 bucks. don't ask why. I don't know  --Nick
			if game.frame==50:
				BlueparrotB(Vector(400,-10),game,player,1,30,7)
				BlueparrotB(Vector(300,-10),game,player,-1,30,7)
			if game.frame==90:
				ToucanA(Vector(200,-10),game,player,5,4,30)
			if game.frame==150:
				ToucanA(Vector(400,-10),game,player,5,4,30)
				BlueparrotB(Vector(300,-10),game,player,-1,30,7)
				BlueparrotB(Vector(500,-10),game,player,1,39,7)
			if game.frame==210:
				ToucanA(Vector(100,-10),game,player,5,4,30)
			if game.frame==250:
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
				BlueparrotB(Vector(200,-10),game,player,-1,30,7)
			if game.frame==270:
				ToucanA(Vector(400,-10),game,player,5,4,30)
			if game.frame==330:
				ToucanA(Vector(500,-10),game,player,5,4,30)
			if game.frame==350:
				BlueparrotB(Vector(100,-10),game,player,-1,30,7)
				BlueparrotB(Vector(300,-10),game,player,1,30,7)
			if game.frame==390:
				ToucanA(Vector(400,-10),game,player,5,4,30)
			if game.frame==450:
				ToucanA(Vector(100,-10),game,player,5,4,30)
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
				BlueparrotB(Vector(200,-10),game,player,-1,30,7)
			if game.frame==510:
				ToucanA(Vector(300,-10),game,player,5,4,30)
			if game.frame==550:
				BlueparrotB(Vector(200,-10),game,player,-1,30,7)
				BlueparrotB(Vector(500,-10),game,player,1,30,7)
			if game.frame==570:
				ToucanA(Vector(100,-10),game,player,5,4,30)
			if game.frame==800:
				game.frame=0
				game.wave+=1
		
		
		if game.wave == 26: #level 3 boss dialogue
			if game.d not in game.gameObjects or game.d is None and len([x for x in game.gameObjects if x.name == 'Bullet']) == 0:
				if game.d is None:
					game.boss=MacawB(Vector(300,-10),game,player)
					game.d = Dialogue("macaw_avi3", "Look kid. I did you a favour by telling you not to come here. Why do you disrespect me by ignoring my kindness?", (200,255,255), game, player, 1)
				elif game.d.ref == 1:
					game.d = Dialogue("penguin_avi2", "Huh?", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 2:
					game.d = Dialogue("macaw_avi3", "I told you my boys are territorial and you shouldn't be here. Did you think I was kidding? Do I look like a joker?", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 3:
					game.d = Dialogue("penguin_avi2", "I'm just trying to get to the Caribbean. I dont want any trouble.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 4:
					game.d = Dialogue("macaw_avi3", "Well you should have thought of that before you ignored everything I have done for you.", (200,255,255), game, player, game.d.ref + 1, 4)
				elif game.d.ref == 5:
					game.d = Dialogue("macaw_avi4", "Prepare to never fly again you previously flightless freak. ", (200,255,255), game, player, game.d.ref + 1, 4)
				else:
					game.d = None
					game.frame = 0
					game.wave += 1
			
			
		if game.wave == 27: #level 3 boss: Don Macaw
			if game.boss not in game.gameObjects:
				game.boss = None
				game.wave += 1
		
		
		if game.wave == 28: #level 3 post boss dialogue
			game.wave += 1
			
			
		if game.wave == 29:
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

def viewHighScores():
	print 'viewing high scores now'
	scoreString = ""
	for line in highScores:
		scoreString = scoreString + line + '\n'
		
	while True:
		clock.tick(60)
		screen.blit(highScoreBackground, (200, 275))
		scoreRender = scoresFont.render(scoreString, 1, (255,255,255))
		screen.blit(scoreRender, (205, 280))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				return

def mainMenuEvents(currentMenuScreen, mainMenuNewGame, mainMenuHighScores, mainMenuExit):
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			
			if event.key == pygame.K_RETURN:
				if screenSelect[0] == True:
					mainGameProcess()
					
				elif screenSelect[1] == True:
					print 'attempting to view high scores'
					viewHighScores()
					
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
	
