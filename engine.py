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
			self.gameObjects[i]._id_ = i			
			
	def draw(self):
		for i in range(len(self.gameObjects)):
			self.gameObjects[i].draw(self.screen)
		
		for i in range(len(self.flags)):
			self.gameObjects.pop(self.flags[i])
			for j in range(i, len(self.flags)):
				if self.flags[i] < self.flags[j]:
					self.flags[j]-=1
		self.flags = []
		
	def flag(self, _id_):
		self.flags.append(_id_)