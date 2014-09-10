import pygame
import math

class Snowball:
	def __init__(self, playerX, playerY, game):
		self.name = 'Snowball'
		self.image = pygame.image.load("Art Stuff\snowball.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = playerX + 11
		self.rect.y = playerY - 5
		self.yVelocity = -5
		self.game = game
		game.gameObjects.append(self)
		
	def update(self):
		future = self.rect.move(0, self.yVelocity)
		self.rect = future
			
	def draw(self, screen):
		#print 'Snowball is drawing'
		screen.blit(self.image, self.rect, [0, 0, 5, 5])
		
	def get_rect(self):
		return self.rect