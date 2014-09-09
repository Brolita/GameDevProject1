import pygame
import math
from Vector import Vector
from bullet import *

class Tracers:
	def __init__(game, enemy, player, count, frameOffset, speed, spriteName):
		self.game = game
		game.gameObjects.append(self)
		self._id_ = len(game.gameObjects)
		self.enemy = enemy
		self.player = player
		self.count = count
		self.frameOffset = frameOffset
		self.speed = speed
		self.spriteName = spriteName
		self.frame = 0
		
	def update(self):
		if(frame%frameOffset == 0):
			LinearBullet(enemy.position, player.getPosition(), self.speed, self.game)
			self.count-= 1
			if(self.count == 0):
				del self
		self.frame+=1
	
	def draw(self):
		return
		
	def __del__ (self):
		game.gameObjects.pop(self._id_)

class TracersOffset:
	def __init__(game, enemy, player, offset, count, frameOffset, speed, spriteName):
		self.game = game
		game.gameObjects.append(self)
		self._id_ = len(game.gameObjects)
		self.enemy = enemy
		self.player = player
		self.count = count
		self.frameOffset = frameOffset
		self.speed = speed
		self.spriteName = spriteName
		self.frame = 0
		self.offset = offset
		
	def update(self):
		if(frame%frameOffset == 0):
			LinearBullet(enemy.position, player.getPosition() + self.offset, self.speed, self.game)
			self.count-=1
			if(self.count == 0):
				del self
		self.frame+=1
	
	def draw(self):
		return
		
	def __del__ (self):
		game.gameObjects.pop(self._id_)
	
def BuckTarget(game, enemy, target, count, spread, speed, spriteName):
	t = target.copy()
	t.RotateAround(enemy.position, spread * (count - 1)/ 2)
	for n in range(count):
		b = LinearBullet(enemy.position, t, speed, game, spriteName)
		t.RotateAround(enemy.position, -spread)

def BuckDown(game, enemy, count, spread, speed, spriteName):
	BuckTarget(game, enemy, Vector(10000, enemy.y) ,count, spread, speed, spriteName)


class Enemy:
	def __init__(self, init, game, player):
		self.game = game
		game.gameObjects.append(self)
		self._id_ = len(game.gameObjects) - 1
		self.player = player
		self.frame = 0
		self.position = init.copy()

	def draw(self, screen):
		if screen.get_rect().inflate(80,80).collidepoint(self.position.x, self.position.y):
			screen.blit(self.image, (self.position.x, self.position.y))
		else:
			self.__del__()
			
	def __del__ (self):
		self.game.flag(self._id_)
	
class SeagullA(Enemy):
	def __init__(self, init, game, player):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\test.png").convert_alpha()
	
	def update(self):
		if self.frame < 20:
			self.position.Add((0, 2))
		elif self.frame == 25:
			BuckTarget(self.game, self, self.player.getPosition(), 5, math.radians(7.5), 5, "seashell")
		elif self.frame > 40:
			self.position.Add((0, -2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
			
	def __del__ (self):
		Enemy.__del__(self)