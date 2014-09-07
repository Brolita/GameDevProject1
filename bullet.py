import Vector
import game

class Bullet(pygame.sprite.Sprite):
	def __init__ (self, spriteName, generateAtInstantiation = true):
		self.spriteName = spriteName
		self.isGenerated = generateAtInstantiation
		if(generateAtInstantiation):
			self.Generate()
			
	def Generate (self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png(self.spriteName)
		self.isGenerated = true	
		
		
class LinearBullet(Bullet):
	def __init__(self, init, target, speed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.speed = speed
		pos = self.position
		self.position.MoveToward(self.target, self.speed)
		self.velocity = self.position - pos
		self.game = game
		self.game.bullets.append(self)
		Super(LinearBullet, self).__init__(spriteName, generateAtInstantiation)
		
	def Update(self):
		self.position += self.velocity
		
class CircularBullet(Bullet):
	def __init__(self, init, target, radialSpeed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.radialSpeed = radialSpeed
		self.game = game
		self.game.bullets.append(self)
		Super(CircularBullet, self).__init__(priteName, generateAtInstantiation)
	
	def Update(self):
		self.position.RotateAround(self.target, self.angularSpeed/self.game.framerate)
		
class SpiralBullet(Bullet):
	def __init__(self, init, target, radialSpeed, approachSpeed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.radialSpeed = radialSpeed
		self.approachSpeed = approachSpeed
		self.game = game
		self.game.bullets.append(self)
		Super(CircularBullet, self).__init__(spriteName, generateAtInstantiation)
		
	def Update(self):
		self.position.RotateAround(self.target, self,radialSpeed)
		self.position.MoveToward(self.target, self.approachSpeed)
		
		