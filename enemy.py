import pygame
import math
from Vector import Vector
from bullet import *

class Tracers:
	def __init__(self, game, enemy, player, count, frameOffset, speed, spriteName):
		self.name = 'Tracers'
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
		if self.enemy == None:
			self.flag()
	
	def draw(self, screen):
		return
		
	def flag(self):
		self.game.flag(self)

class TracersOffset:
	def __init__(self, game, enemy, player, offset, count, frameOffset, speed, spriteName):
		self.name = 'TracersOffset'
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
		if self.enemy == None:
			self.flag()
	
	def draw(self, screen):
		return
		
	def flag(self):
		self.game.flag(self)
	
def BuckTarget(game, enemy, target, count, spread, speed, spriteName):
	t = target.copy()
	t.RotateAround(enemy.position, spread * (count - 1)/ 2)
	for n in range(count):
		b = LinearBullet(enemy.position, t, speed, game, spriteName)
		t.RotateAround(enemy.position, -spread)

def BuckDown(game, enemy, count, spread, speed, spriteName):
	BuckTarget(game, enemy, Vector(enemy.position.x, 10000) ,count, spread, speed, spriteName)

class Explosion:
	def __init__(self, init, game, name):
		self.game = game
		game.gameObjects.append(self)
		self.frame = 0
		self.name = name
		self.image = Image.get(name+"_explode1")
		self.position = init.copy()
	
	def update(self):
		if self.frame > 4:
			self.image = Image.get(self.name+"_explode2")
		if self.frame > 8:
			self.flag()
		self.frame += 1
			
	def draw(self, screen):
		if screen.get_rect().move(-100, 0).inflate(100,100).collidepoint(self.position.x, self.position.y):
			screen.blit(self.image, (self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2))
		else:
			self.flag()
			
	def flag(self):
		self.game.flag(self)
		
	
class Enemy:
	sidebar = None
	@staticmethod
	def setSidebar(sidebar):
		Enemy.sidebar = sidebar

	def __init__(self, init, game, player, points):
		self.name = 'Enemy'
		self.game = game
		game.gameObjects.append(self)
		self.player = player
		self.frame = 0
		self.position = init.copy()
		self.points = points

	def draw(self, screen):
		if screen.get_rect().move(-100, 0).inflate(self.image.get_width()*2 + 10,self.image.get_height()*2 + 10).collidepoint(self.position.x, self.position.y):
			screen.blit(self.image, (self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2))
		else:
			self.flag()
			
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		self.game.sidebar.points += self.points
		self.flag()
		
	def flag(self):
		self.game.flag(self)
	
class SeagullA(Enemy):
	def __init__(self, init, game, player,count):
		Enemy.__init__(self, init, game, player, 100)
		self.image = Image.get("seagull")
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
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
	
	def flag(self):
		Explosion(self.position, self.game, "seagull")
		Enemy.flag(self)
		
class SeagullB(Enemy):
	def __init__(self, init, game, player,count):
		Enemy.__init__(self, init, game, player, 100)
		self.image = Image.get("seagull")
		self.count=count
	def update(self):
		if self.frame < 20:
			self.position.Add((0, -2))
		elif self.frame == 25:
			BuckTarget(self.game, self, self.player.getPosition(), self.count, math.radians(7.5), 5, "seashell")
		elif self.frame > 40:
			self.position.Add((0, 2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
			
	def flag(self):
		Explosion(self.position, self.game, "seagull")
		Enemy.flag(self)
	
class PelicanA(Enemy):
	def __init__(self, init, game, player,timebetween,speed):
		Enemy.__init__(self, init, game, player, 50)
		self.image = Image.get("pelican")
		self.t = None
		self.timebetween=timebetween
		self.speed=speed
	def update(self):
		self.position.Add((0, 5))
		if self.frame == 25:
			self.t = Tracers(self.game, self, self.player, 40, self.timebetween, self.speed, "rock")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
	
	def hit(self):
		Enemy.hit(self)
	
	def flag(self):
		Explosion(self.position, self.game, "pelican")
		Enemy.flag(self)
		if self.t != None:
			self.t.flag()
			
class PelicanB(Enemy):
	def __init__(self, init, game, player,timebetween,speed):
		Enemy.__init__(self, init, game, player, 50)
		self.image = Image.get("pelican")
		self.t = None
		self.timebetween=timebetween
		self.speed=speed
	def update(self):
		self.position.Add((0, -5))
		if self.frame == 25:
			self.t = Tracers(self.game, self, self.player, 40, self.timebetween, self.speed, "rock")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "pelican")
		Enemy.flag(self)
		if self.t != None:
			self.t.flag()
						
class PelicanC(Enemy):
	def __init__(self, init, game, player,timebetween,speed):
		Enemy.__init__(self, init, game, player, 50)
		self.image = Image.get("pelican")
		self.timebetween=timebetween
		self.speed=speed;
	def update(self):
		self.position.Add((0, 5))
		if self.frame%self.timebetween==0:
			LinearBullet(self.position,Vector(400-self.position.x,self.position.y),self.speed,self.game,"rock");
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "pelican")
		Enemy.flag(self)

class HummingbirdA(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player, 100)
		self.image=Image.get("hummingbird")
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,0))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,Vector(self.position.x,99999),self.buck,math.radians(7.5),3,"seashell")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
		
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "hummingbird")
		Enemy.flag(self)
		
class HummingbirdB(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player,100)
		self.image=Image.get("hummingbird")
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,0))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,self.player.getPosition(),self.buck,math.radians(7.5),5,"seashell")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)

	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "hummingbird")
		Enemy.flag(self)
		
class HummingbirdC(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player,100)
		self.image=Image.get("hummingbird")
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,2))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,self.player.getPosition(),self.buck,math.radians(7.5),5,"seashell")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
	
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "hummingbird")
		Enemy.flag(self)	
	
class DoveA(Enemy):
	def __init__(self,init,game,player):
		Enemy.__init__(self,init,game,player,50)
		self.image=Image.get("dove")
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			if self.position.x<self.player.rect.x+16:
				self.position.Add((3,0))
			if self.position.x>self.player.rect.x+16:
				self.position.Add((-3,0))
			if self.position.y<self.player.rect.y+24:
				self.position.Add((0,3))
			if self.position.y>self.player.rect.y+24:
				self.position.Add((0,-3))
		self.frame+=1
			
	def draw(self,screen):
		Enemy.draw(self,screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "dove")
		Enemy.flag(self)	

class DoveB(Enemy):
	def __init__(self,init,game,player,timebetween,speed):
		Enemy.__init__(self,init,game,player,50)
		self.image=Image.get("dove")
		self.t=None
		self.timebetween=timebetween
		self.speed=speed
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		if self.frame==25:
			self.t = Tracers(self.game, self, self.player, 40, self.timebetween, self.speed, "rock")
		else:
			if self.position.x<self.player.rect.x+16:
				self.position.Add((3,0))
			if self.position.x>self.player.rect.x+16:
				self.position.Add((-3,0))
			if self.position.y<self.player.rect.y+24:
				self.position.Add((0,3))
			if self.position.y>self.player.rect.y+24:
				self.position.Add((0,-3))
		self.frame+=1
			
	def draw(self,screen):
		Enemy.draw(self,screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
		
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "dove")
		Enemy.flag(self)
		if self.t != None:
			self.t.flag()

class DoveC(Enemy):
	def __init__(self,init,game,player,count):
		Enemy.__init__(self,init,game,player,50)
		self.image=Image.get("dove")
		self.t=None
		self.count=count
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		if self.frame%25==0:
			BuckTarget(self.game, self, self.player.getPosition(), self.count, math.radians(7.5), 5, "seashell")
		else:
			if self.position.x<self.player.rect.x+16:
				self.position.Add((3,0))
			if self.position.x>self.player.rect.x+16:
				self.position.Add((-3,0))
			if self.position.y<self.player.rect.y+24:
				self.position.Add((0,3))
			if self.position.y>self.player.rect.y+24:
				self.position.Add((0,-3))
		self.frame+=1
			
	def draw(self,screen):
		Enemy.draw(self,screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
		
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "dove")
		Enemy.flag(self)	

class ToucanA(Enemy):
	def __init__(self, init, game, player,count,amount,timebetween):
		Enemy.__init__(self, init, game, player, 150)
		self.image = Image.get("toucan")
		self.count=count
		self.amount=amount
		self.i=0
		self.timebetween=timebetween
	def update(self):
		if self.frame < 20:
			self.position.Add((0, 2))
		elif (self.frame>=25) and ((self.frame-5)%self.timebetween==0):
			if self.i<self.amount:
				BuckTarget(self.game, self, self.player.getPosition(), self.count, math.radians(7.5), 5, "blueflower8x8")
				self.i+=1
		elif self.frame > 40+((self.amount-1)*10):
			self.position.Add((0, -2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "toucan")
		Enemy.flag(self)	

class ToucanB(Enemy):
	def __init__(self, init, game, player,amount,timebetween):
		Enemy.__init__(self, init, game, player, 150)
		self.image = Image.get("toucan")
		self.amount=amount
		self.i=0
		self.timebetween=timebetween
	def update(self):
		if self.frame < 20:
			self.position.Add((0, 2))
		elif (self.frame>=25) and ((self.frame-5)%self.timebetween==0):
			if self.i<self.amount:
				BuckTarget(self.game, self, self.player.getPosition(), self.i+1, math.radians(7.5), 5, "redflower10x10")
				self.i+=1
		elif self.frame > 40+((self.amount-1)*10):
			self.position.Add((0, -2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "toucan")
		Enemy.flag(self)

class BlueparrotA(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player, 100)
		self.image=Image.get("blueparrot")
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,4))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,self.player.getPosition(),self.buck,math.radians(7.5),5,"blueflower8x8")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
	
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "blueparrot")
		Enemy.flag(self)	

class BlueparrotB(Enemy):
	def __init__(self, init,game,player,direction,timebetween,speed):
		Enemy.__init__(self,init,game,player, 100)
		self.image=Image.get("blueparrot")
		self.direction=direction
		self.timebetween=timebetween
		self.t=None
		self.speed=speed
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,4))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		self.frame+=1
		if self.frame==25:
			self.t = Tracers(self.game, self, self.player, 40, self.timebetween, self.speed, "redflower10x10")
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
	
	def hit(self):
		Enemy.hit(self)
		
	def flag(self):
		Explosion(self.position, self.game, "blueparrot")
		Enemy.flag(self)	
		if self.t != None:
			self.t.flag()
			
			
class Boss(Enemy):
	def __init__(self, init, game, player, health):
		Enemy.__init__(init, game, player)
		self.name = 'Boss'
		self.health = health
	
	def hit(self):
		health -= 1
		if health == 0:
			self.flag()
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Enemy.flag(self)
		
class ExampleBoss(Boss):
	def __init__(self, init, game, player, health):
		Boss.__init__(init, game, player, health)
		self.image = Image.get("test")
	
	def hit(self):
		Boss.hit(self)
	
	def update(self):
		print "here you go nick, sorry for the delay"
	
	def draw(self, screen):
		Boss.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Boss.flag(self)