import pygame
import math

class Engine:
	def __init__(self, screen, sidebar):
		self.gameObjects = []
		self.flags = set([])	
		self.screen = screen
		self.sidebar = sidebar
		self.frame = 0
		self.wave = 0
		self.d =  None
		
	def restart(self, s = False):
		for i in self.gameObjects:
			i.flag()
		if s:
			if wave <= 6:
				wave = 0
			elif wave <= 9:
				wave = 7
			elif wave <= 15:
				wave = 10
			elif wave <= 18:
				wave = 16
			elif wave <= 24:
				wave = 19
			else:
				wave = 25
		else:
			self.frame = 0
			self.wave = 0
			
		self.d =  None
		self.sidebar.points = 0
		self.sidebar.lives =4
		
	def playerHit(self, i):
		i.invinsibility = 120
		for j in self.gameObjects:
			if j.name == 'Bullet':
				collisionDetected = j.get_rect().colliderect(pygame.Rect(i.getPosition().x - 200, i.getPosition().y - 200, 400, 400))
				if collisionDetected:
					j.flag()
		self.sidebar.lives -= 1			
		
	def update(self):
		if len(self.gameObjects) > 500:
			print "Warning! over 500 gameobject to be rendered, expect slow down. # of gameObjects", len(self.gameObjects)
		
		for i in self.gameObjects:
			if i.name == "Dialouge":
				i.update()
				
		
		for i in self.gameObjects:
			i.update()
			if i.name == 'Player' or i.name == 'Snowball':
				for j in self.gameObjects:	
					if i.name == 'Player' and j.name == 'Bullet' and i.invinsibility == 0:
					# check if Player has been hit by a bullet
						collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
						if collisionDetected == True:
							j.flag()
							self.playerHit(i)
														   
					# check if Player has collided with an enemy
					if i.name == 'Player' and j.name == 'Enemy':
						collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
						if collisionDetected == True:
							self.playerHit(i)
							j.flag()

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
		if self.flags:
			while self.flags:
				self.gameObjects.remove(self.flags.pop())
		
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
	def flag(self, obj):
		self.flags.add(obj)