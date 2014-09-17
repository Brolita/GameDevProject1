import pygame
import math
from image import Image

class Engine:
	def __init__(self, screen, sidebar):
		self.gameObjects = []
		self.flags = set([])	
		self.screen = screen
		self.sidebar = sidebar
		self.frame = 0
		self.wave = 0
		self.d =  None
		self.boss = None
		self.levelFade = False
		self.levelBackground = self.levelOneBackground = Image.get('backgrounds\water_background\water1a')
		self.levelTwoBackground = Image.get('backgrounds\cloud_background\clouds1')
		self.levelThreeBackground = Image.get('backgrounds\\rainforest')
		
	def restart(self, s = False):
		for i in self.gameObjects:
			i.flag()
		if s:
			if self.wave <= 6:
				self.wave = 0
				self.levelBackground = self.levelOneBackground
			elif self.wave <= 9:
				self.wave = 7
				self.levelBackground = self.levelOneBackground
			elif self.wave <= 15:
				self.wave = 10
				self.levelBackground = self.levelTwoBackground
			elif self.wave <= 18:
				self.wave = 16
				self.levelBackground = self.levelTwoBackground
			elif self.wave <= 25:
				self.wave = 19
				self.levelBackground = self.levelThreeBackground
			else:
				self.wave = 26
				self.levelBackground = self.levelThreeBackground
		else:
			self.levelBackground = self.levelOneBackground
			self.frame = 0
			self.wave = 0
			
		self.d =  None
		self.sidebar.points = 0
		self.sidebar.lives = 4
		
	def playerHit(self, i):
		i.invinsibility = 120
		for j in self.gameObjects:
			if j.name == 'Bullet':
				collisionDetected = j.get_rect().colliderect(pygame.Rect(i.getPosition().x - 200, i.getPosition().y - 200, 400, 400))
				if collisionDetected:
					j.flag()
		self.sidebar.lives -= 1			
		
	def update(self):
		#if len(self.gameObjects) > 500:
			#print "Warning! over 500 gameobject to be rendered, expect slow down. # of gameObjects", len(self.gameObjects)
		
		for i in self.gameObjects:
			if i.name == "Dialouge":
				i.update()
				
		
		for i in self.gameObjects:
			i.update()
			
		for i in self.gameObjects:
			if i.name == 'Player' or i.name == 'Snowball':
				for j in self.gameObjects:	
					if i.name == 'Player' and j.name == 'Bullet' and i.invinsibility == 0:
					# check if Player has been hit by a bullet
						collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
						if collisionDetected == True:
							j.flag()
							self.playerHit(i)
														   
					# check if Player has collided with an enemy
					if i.name == 'Player' and j.name == 'Enemy' and i.invinsibility == 0:
						collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
						if collisionDetected == True:
							j.hit()
							self.playerHit(i)

					# check if Player has shot an enemy
					if i.name == 'Snowball' and j.name == 'Enemy':
						collisionDetected = j.get_rect().colliderect(i.get_rect())
						if collisionDetected == True:
							i.flag()
							j.hit()
						
					# check if Player has shot an boss
					if i.name == 'Snowball' and j.name == 'Boss':
						collisionDetected = j.get_rect().colliderect(i.get_rect())
						if collisionDetected == True:
							i.flag()
							j.hit()
										
	def draw(self):
		self.screen.blit(self.levelBackground, (0,0))
		
		if self.flags:
			while self.flags:
				self.gameObjects.remove(self.flags.pop())
		
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)	
			
		if self.levelFade and self.frame > 1:
			s = pygame.Surface((600,800), pygame.SRCALPHA)
			s.fill((0,0,0,8*self.frame - 1))
			self.screen.blit(s, (0,0))
			if self.frame == 32:
				self.levelFade = False
				self.frame = 0
				self.wave += 1
				if self.levelBackground == self.levelOneBackground:
					self.levelBackground = self.levelTwoBackground
				elif self.levelBackground == self.levelTwoBackground:
					self.levelBackground = self.levelThreeBackground
				
				
		
	def flag(self, obj):
		self.flags.add(obj)