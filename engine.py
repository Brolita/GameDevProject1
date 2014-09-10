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
						collisionDetected = i.get_rect().colliderect(j.get_rect())
						if collisionDetected == True:
							if i.name == 'Player' and j.name == 'Bullet':
								print 'Player has been hit!'
							
							elif j.name == 'Player' and i.name == 'Bullet':
								print 'Player has been hit!'
						
	def draw(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
		while self.flags:
			self.gameObjects.remove(self.flags.pop())
		
	def flag(self, obj):
		self.flags.append(obj)