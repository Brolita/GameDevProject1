import pygame
import math

class Engine:
	def __init__(self, screen):
		self.gameObjects = []
		self.flags = []
		self.screen = screen
		
	def update(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].update()	
			
	def draw(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
		while self.flags:
			self.gameObjects.remove(self.flags.pop())
		
	def flag(self, obj):
		self.flags.append(obj)