import Vector
import game
import bullet

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
	t = target
	t.RotateAround(enemy.position, spread * (count - 1)/ 2
	for n in range(count):
		b = LinearBullet(enemy.position, t, speed, game, spriteName)
		t.RotateAround(enemy.position, -spread)

def BuckDown(game, enemy, count, spread, speed, spriteName):
	BuckTarget(game, enemy, Vector(10000, enemy.y) ,count, spread, speed, spriteName

'''
class SeagullA:
	def __init__(self, init, game, player):
		self.game = game
		game.gameObjects.append(self)
		self.frame = 0
		self.position = init
	
	def update(self):
		if frame < 20 
			self.init += Vector(0, 2)
		elif frame == 20
			BuckTarget(self.game, self, player.getPosition(), '''