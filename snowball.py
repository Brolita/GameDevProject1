import pygame
import math

class Snowball:
	def __init__(self, playerX, playerY):
		self.image = pygame.image.load("Art Stuff\snowball.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = playerX + 11
		self.rect.y = playerY - 5
		self.yVelocity = -5
		
	def update(self, screen):
		self.draw(screen)
		future = self.rect.move(0, self.yVelocity)
		self.rect = future
			
	def draw(self, screen):
		#print 'Snowball is drawing'
		screen.blit(self.image, self.rect, [0, 0, 5, 5])
		