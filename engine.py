import pygame
import math

class Engine:
	def __init__(self, screen):
		self.gameObjects = []
		self.flags = []
		self.screen = screen
		
	def update(self):
		for i in self.gameObjects:
			i.update()	
			if i.name != 'Tracers' and i.name != 'TracersOffset':
				for j in self.gameObjects:
					if i != j and j.name != 'Tracers' and j.name != 'TracersOffset':	
						if i.name == 'Player' and j.name == 'Bullet':
						# check if Player has been hit by a bullet
							collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
							if collisionDetected == True:
								self.gameObjects.remove(j)
								print 'Player has been hit!'
								
						# check if Player has shot an enemy
						if i.name == 'Snowball' and j.name == 'Enemy':
							collisionDetected = j.get_rect().colliderect(i.get_rect())
							if collisionDetected == True:
								print 'Player shot an enemy!'
								self.gameObjects.remove(i)
								self.gameObjects.remove(j)
																		   
						# check if Player has collided with an enemy
						if i.name == 'Player' and j.name == 'Enemy':
							collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
							if collisionDetected == True:
								print 'Player has collided with an enemy!'
						
	def draw(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
		while self.flags:
			self.gameObjects.remove(self.flags.pop())
		
	def flag(self, obj):
		self.flags.append(obj)