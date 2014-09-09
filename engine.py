import pygame

class Engine:
	def __init__(self, screen):
		self.gameObjects = []
		self.screen = screen
		
	def update(self):
		for i in range(len(self.gameObjects)):
			try:
				self.gameObjects[i].update()
			except(AttributeError):
				print self.gameObjects[i].__class__, "is listed as a gameobject but has no update function"
	
	def draw(self):
		for i in range(len(self.gameObjects)):
			try:
				self.gameObjects[i].draw(self.screen)
			except(AttributeError):
				print self.gameObjects[i].__class__, "is listed as a gameobject but has no draw function"
	