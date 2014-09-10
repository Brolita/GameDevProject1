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
							collisionDetected = j.get_rect().collidepoint((i.getPosition().x, i.getPosition().y))
							if collisionDetected == True:
								print 'Player has been hit!'
						
	def draw(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
		if self.flags:
			while self.flags:
				self.gameObjects.remove(self.flags.pop())
		
	def flag(self, obj):
		self.flags.append(obj)