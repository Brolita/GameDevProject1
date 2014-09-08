from Vector import Vector
from engine import engine

class Bullet(pygame.sprite.Sprite):
	def __init__ (self, game, spriteName, generateAtInstantiation = true):
		self.spriteName = spriteName
		self.isGenerated = generateAtInstantiation
		game.gameObjects.append(self)
		self.game = game
		self._id_ = len(game.gameObjects)
		if(generateAtInstantiation):
			self.Generate()
			
	def generate (self):
		if(!self.isGenerated):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load('Art Stuff\\' + spriteName + '.png')
			self.isGenerated = true	
			
	def draw (self):
		screen.blit(self.image, (self.position.x, self.position.y))
		
	def __del__ (self):
		game.gameObjects.pop(self._id_)
		
class LinearBullet(Bullet):
	def __init__(self, init, target, speed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.speed = speed
		pos = self.position
		self.position.MoveToward(self.target, self.speed)
		self.velocity = self.position - pos
		Super(LinearBullet, self).__init__(game, spriteName, generateAtInstantiation)
		
	def update(self):
		self.position += self.velocityh
		
	def draw(self):
		Super(LinearBullet, self).draw()
	
	def __del__(self):
		Super(LinearBullet, self).__del__()
		
class CircularBullet(Bullet):
	def __init__(self, init, target, radialSpeed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.radialSpeed = radialSpeed
		Super(CircularBullet, self).__init__(game, spriteName, generateAtInstantiation)
	
	def update(self):
		self.position.RotateAround(self.target, self.angularSpeed/self.game.framerate)
	
	def draw(self):
		Super(LinearBullet, self).draw()
	
	def __del__(self):
		Super(LinearBullet, self).__del__()
		
class SpiralBullet(Bullet):
	def __init__(self, init, target, radialSpeed, approachSpeed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.radialSpeed = radialSpeed
		self.approachSpeed = approachSpeed
		Super(CircularBullet, self).__init__(game, spriteName, generateAtInstantiation)
		
	def update(self):
		self.position.RotateAround(self.target, self,radialSpeed)
		self.position.MoveToward(self.target, self.approachSpeed)
	
	def draw(self):
		Super(LinearBullet, self).draw()
	
	def __del__(self):
		Super(LinearBullet, self).__del__()