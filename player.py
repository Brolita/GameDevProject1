import pygame
import math
from Vector import Vector
from snowball import Snowball
from image import Image

class Dialogue:
	font = None
	def __init__(self, image, D, game, player):
		self.name = "Dialogue"
		self.game = game
		game.gameObjects.append(self)
		if Dialogue.font == None:
			Dialogue.font = pygame.font.SysFont("monospace",15)
		self.image = Image.get(image)
		self.s = D
		self.player = player
	
	def update(self):
		if self.player.firing:
			self.flag()
			
	def draw(self, screen):
		screen.blit(self.image, (40, 600))
		screen.blit(Image.get("textbox"), (110, 581))
	
	def flag(self):
		self.game.flag(self)

class Player:
	def __init__ (self, game):
		self.image = pygame.image.load("Art Stuff\penguin.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 400
		self.x_velocity = 5
		self.y_velocity = 5
		self.moving = [False, False, False, False] #up, down, left, right, self.focus
		self.focus = False
		self.firing = False
		self.snowballs = []
		self.fireCooldown = 5
		self.canFire = True
		self.game = game
		self.name = 'Player'
		self.invinsibility = 0
		#self.dash = False
		self.dashLength = 0
		game.gameObjects.append(self)
	
	def update(self):
		self.fireCooldown -= 1
		if self.fireCooldown < 1:
			self.canFire = True
			self.fireCooldown = 0
			
		if (self.firing and self.canFire):
			snowball = Snowball(self.rect.x, self.rect.y, self.game)
			self.snowballs.append(snowball)
			self.fireCooldown = 5
			self.canFire = False
		
		#if self.dash:
		#	a = math.sqrt(2)
		#	if self.moving[0]:
		#		if self.moving[2]:
		#			self.rect = self.rect.move(
		#		elif self.moving[3]:
		#			
		#		else:
					
		#	elif self.moving[1]:
		#		if self.moving[2]:
		#			
		#		elif self.moving[3]:
		#			
		#		else:
					
		#	elif self.moving[2]:
					
		#	elif self.moving[3]:
			
		#	self.dashLength += 1
			
		if self.moving[0]:
			if self.focus:
				future = self.rect.move(0, -self.y_velocity/2.5)
			else:
				future = self.rect.move(0, -self.y_velocity)
			if future.top < 0:
				self.rect.top = 0
				
			else:
				self.rect = future
				
		elif self.moving[1]:
			if self.focus:
				future = self.rect.move(0, self.y_velocity/2.5)
			else:
				future = self.rect.move(0, self.y_velocity)
			if future.bottom > 800:
				self.rect.bottom = 800
				
			else:
				self.rect = future
				
		if self.moving[2]:
			if self.focus:
				future = self.rect.move(-self.x_velocity/2.5, 0)
			else:
				future = self.rect.move(-self.x_velocity, 0)
			if future.left < 0:
				self.rect.left = 0
				
			else:
				self.rect = future
				
		elif self.moving[3]:
			if self.focus:
				future = self.rect.move(self.x_velocity/2.5, 0)
			else:
				future = self.rect.move(self.x_velocity, 0)
			if future.right > 600:
				self.rect.right = 600
				
			else:
				self.rect = future
				
		if self.invinsibility != 0:
			self.invinsibility-= 1
				
	def getPosition(self):
		#print 'Player is currently at', self.rect.x + 16, ', ', self.rect.y + 48
		return Vector(self.rect.x + 15, self.rect.y + 15)
	
	def get_rect(self):
		return self.rect
		
	def draw(self, screen):
		screen.blit(self.image, self.rect, [0, 0, 32, 48])
		
		#for projectile in self.snowballs:
		#	projectile.update(screen)
		#	if projectile.rect.y < -5:
		#		self.snowballs.remove(projectile)
	
	def dash(self, sidebar):
		self.dash = True
		self.dashLength = 0
		sidebar.dash -= 1