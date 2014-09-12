import pygame
import math

class Engine:
	def __init__(self, screen, sidebar):
		self.gameObjects = []
		self.flags = set([])	
		self.screen = screen
		self.sidebar = sidebar
		
	def playerHit(self, i):
		i.invinsibility = 30
		for j in self.gameObjects:
			if j.name == 'Bullet':
				collisionDetected = j.get_rect().colliderect(pygame.Rect(i.getPosition().x - 100, i.getPosition().y - 100, 200, 200))
				if collisionDetected:
					j.flag()
		self.sidebar.lives -= 1
		
	def update(self):
		if len(self.gameObjects) > 500:
			print "Warning! over 500 gameobject to be rendered, expect slow down. # of gameObjects", len(self.gameObjects)
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
							print 'Player has been hit!'
							
					# check if Player has shot an enemy
					if i.name == 'Snowball' and j.name == 'Enemy':
						collisionDetected = j.get_rect().colliderect(i.get_rect())
						if collisionDetected == True:
							print 'Player shot an enemy!'
							i.flag()
							j.flag()
																	   
					# check if Player has collided with an enemy
					if i.name == 'Player' and j.name == 'Enemy':
						collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
						if collisionDetected == True:
							print 'Player has collided with an enemy!'
						
	def draw(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
		if self.flags:
			while self.flags:
				self.gameObjects.remove(self.flags.pop())
		
	def flag(self, obj):
		self.flags.add(obj)