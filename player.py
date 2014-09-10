import pygame
import math
from Vector import Vector
from snowball import Snowball

class Player:
	def __init__ (self, game):
		print 'Made a snowball!'
		self.image = pygame.image.load("Art Stuff\penguin.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 400
		self.x_velocity = 3
		self.y_velocity = 3
		self.moving = [False, False, False, False] #up, down, left, right
		self.firing = False
		self.snowballs = []
		self.fireCooldown = 5
		self.canFire = True
		self.game = game
		game.gameObjects.append(self)
	
	def update(self):
		self.fireCooldown -= 1
		if self.fireCooldown < 1:
			self.canFire = True
			self.fireCooldown = 0
			
		if (self.firing and self.canFire):
			snowball = Snowball(self.rect.x, self.rect.y)
			self.snowballs.append(snowball)
			self.fireCooldown = 5
			self.canFire = False
			
		if self.moving[0]:
			future = self.rect.move(0, -self.y_velocity)
			if future.top < 0:
				self.rect.top = 0
				
			else:
				self.rect = future
				
		elif self.moving[1]:
			future = self.rect.move(0, self.y_velocity)
			if future.bottom > 800:
				self.rect.bottom = 800
				
			else:
				self.rect = future
				
		if self.moving[2]:
			future = self.rect.move(-self.x_velocity, 0)
			if future.left < 0:
				self.rect.left = 0
				
			else:
				self.rect = future
				
		elif self.moving[3]:
			future = self.rect.move(self.x_velocity, 0)
			if future.right > 600:
				self.rect.right = 600
				
			else:
				self.rect = future
				
	def getPosition(self):
		#print 'Player is currently at', self.rect.x + 16, ', ', self.rect.y + 48
		return Vector(self.rect.x + 15, self.rect.y + 35)
	
	def draw(self, screen):
		screen.blit(self.image, self.rect, [0, 0, 32, 48])
		
		for projectile in self.snowballs:
			projectile.update(screen)
			if projectile.rect.y < -5:
				self.snowballs.remove(projectile)
