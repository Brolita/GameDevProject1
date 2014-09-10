import pygame
import math
from Vector import Vector
from bullet import *

class Tracers:
	def __init__(self, game, enemy, player, count, frameOffset, speed, spriteName):
		self.game = game
		game.gameObjects.append(self)
		self.enemy = enemy
		self.player = player
		self.count = count
		self.frameOffset = frameOffset
		self.speed = speed
		self.spriteName = spriteName
		self.frame = 0
		
	def update(self):
		if(self.frame%self.frameOffset == 0):
			LinearBullet(self.enemy.position, self.player.getPosition(), self.speed, self.game, self.spriteName)
			self.count-= 1
			if(self.count == 0):
				self.__del()
		self.frame+=1
	
	def draw(self, screen):
		return
		
	def __del (self):
		self.game.flag(self)

class TracersOffset:
	def __init__(self, game, enemy, player, offset, count, frameOffset, speed, spriteName):
		self.game = game
		game.gameObjects.append(self)
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
			LinearBullet(self.enemy.position, self.player.getPosition() + self.offset, self.speed, self.game, self.spriteName)
			self.count-=1
			if(self.count == 0):
				self.__del()
		self.frame+=1
	
	def draw(self, screen):
		return
		
	def __del (self):
		self.game.flag(self)
	
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
		self.player = player
		self.frame = 0
		self.position = init.copy()

	def draw(self, screen):
		if screen.get_rect().inflate(80,80).collidepoint(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2):
			screen.blit(self.image, (self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2))
		else:
			self.__del()
			
	def __del (self):
		self.game.flag(self)
	
class SeagullA(Enemy):
	def __init__(self, init, game, player,count):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\test.png").convert_alpha()
		self.count=count
	def update(self):
		if self.frame < 20:
			self.position.Add((0, 2))
		elif self.frame == 25:
			BuckTarget(self.game, self, self.player.getPosition(), self.count, math.radians(7.5), 5, "seashell")
		elif self.frame > 40:
			self.position.Add((0, -2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
			
	def __del (self):
		Enemy.__del(self)
		
class SeagullB(Enemy):
	def __init__(self, init, game, player):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\test.png").convert_alpha()
		self.t = None
	
	def update(self):
		if self.frame < 20:
			self.position.Add((0, 2))
		elif self.frame == 25:
			self.t = Tracers(self.game, self, self.player, 10, 7, 5, "rock")
		elif self.frame > 100:
			self.position.Add((0, -2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
			
	def __del (self):
		Enemy.__del(self)
		if self.t != None:
			self.t.__del()