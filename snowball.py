import pygame
import math
from image import Image

class Snowball:
	def __init__(self, playerX, playerY, game):
		self.name = 'Snowball'
		self.image = Image.get('snowball')
		self.rect = self.image.get_rect()
		self.rect.x = playerX + 11
		self.rect.y = playerY - 5
		self.yVelocity = -11
		self.game = game
		game.gameObjects.append(self)
		
	def update(self):
		future = self.rect.move(0, self.yVelocity)
		self.rect = future
			
	def draw(self, screen):
		#print 'Snowball is drawing'
		if screen.get_rect().inflate(300,300).colliderect(self.rect):
			screen.blit(self.image, self.rect, [0, 0, 5, 5])
		else:
			self.flag()
		
	def get_rect(self):
		return self.rect
		
	def flag(self):
		self.game.flag(self)