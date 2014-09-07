import pygame

class Player:
	def __init__ (self):
		self.image = pygame.image.load("Art Stuff\player sprite.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.x_velocity = 5
		self.y_velocity = 5
		self.moving = [False, False, False, False] #up, down, left, right
	
	def update(self):
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
		print 'Player is currently at', self.rect.x + 16, ', ', self.rect.y + 48
		return (self.rect.x + 16, self.rect.y + 48)
	
	def draw(self, screen):
		screen.blit(self.image, self.rect, [0, 0, 32, 48])