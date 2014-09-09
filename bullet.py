import pygame
import math
from Vector import Vector
from engine import Engine

class Bullet(pygame.sprite.Sprite):
	def __init__ (self, game, spriteName):
		self.spriteName = spriteName	
		self.game = game
		game.gameObjects.append(self)
		self._id_ = len(game.gameObjects)
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Art Stuff\\' + spriteName + '.png')
	
	def draw (self, screen):
		if screen.get_rect().copy().inflate(40,40).collidepoint(self.position.x, self.position.y):
			screen.blit(self.image, (self.position.x, self.position.y))
		else:
			del self
			
	def __del__ (self):
		game.gameObjects.pop(self._id_)
		
class LinearBullet(Bullet):
	def __init__(self, init, target, speed, game, spriteName):
		self.position = init.copy()
		self.target = target.copy()
		self.speed = speed
		pos = self.position
		self.position.MoveToward(self.target, self.speed)
		self.velocity = self.position - pos
		super(LinearBullet, self).__init__(game, spriteName)
		
	def update(self):
		self.position.Add(self.velocity)
		
	def draw(self, screen):
		super(LinearBullet, self).draw(screen)
	
	def __del__(self):
		super(LinearBullet, self).__del__()
		
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
	
	def __del__(self):
		super(LinearBullet, self).__del__()
		
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
	
	def __del__(self):
		super(LinearBullet, self).__del__()