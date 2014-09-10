import pygame
import math
from Vector import Vector
from engine import Engine

class Bullet(pygame.sprite.Sprite):
	def __init__ (self, game, spriteName):
		self.spriteName = spriteName	
		self.game = game
		game.gameObjects.append(self)
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Art Stuff\\' + spriteName + '.png')
	
	def draw (self, screen):
		if screen.get_rect().copy().inflate(40,40).collidepoint(self.position.x, self.position.y):
			screen.blit(self.image, (self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2))
		else:
			self.__del()
			
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
		
	def __del (self):
		self.game.flag(self)
		
class LinearBullet(Bullet):
	def __init__(self, init, target, speed, game, spriteName):
		self.position = init.copy()
		self.target = target.copy()
		self.speed = speed
		pos = self.position.copy()
		pos.MoveToward(self.target, self.speed)
		self.velocity = pos - self.position
		super(LinearBullet, self).__init__(game, spriteName)
		
	def update(self):
		self.position.Add(self.velocity)
		
	def draw(self, screen):
		super(LinearBullet, self).draw(screen)
		
	def get_rect(self):
		super(LinearBullet, self).get_rect()
	
	def __del(self):
		super(LinearBullet, self).__del()
		
class CircularBullet(Bullet):
	def __init__(self, init, target, radialSpeed, game, spriteName):
		self.position = init.copy()
		self.target = target.copy()
		self.radialSpeed = radialSpeed
		super(CircularBullet, self).__init__(game, spriteName)
	
	def update(self):
		self.position.RotateAround(self.target, self.angularSpeed/self.game.framerate)
	
	def draw(self, screen):
		super(LinearBullet, self).draw(screen)
		
	def get_rect(self):
		super(LinearBullet, self).get_rect()
	
	def __del(self):
		super(LinearBullet, self).__del()
		
class SpiralBullet(Bullet):
	def __init__(self, init, target, radialSpeed, approachSpeed, game, spriteName):
		self.position = init.copy()
		self.target = target.copy()
		self.radialSpeed = radialSpeed
		self.approachSpeed = approachSpeed
		super(CircularBullet, self).__init__(game, spriteName)
		
	def update(self):
		self.position.RotateAround(self.target, self,radialSpeed)
		self.position.MoveToward(self.target, self.approachSpeed)
	
	def draw(self, screen):
		super(LinearBullet, self).draw(screen)
		
	def get_rect(self):
		super(LinearBullet, self).get_rect()
	
	def __del(self):
		super(LinearBullet, self).__del()