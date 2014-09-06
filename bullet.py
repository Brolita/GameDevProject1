class Bullet(pygame.sprite.Sprite):
	self.game = game
	def __init__ (self, game, spriteName, generateAtInstantiation = true):
		self.spriteName = spriteName
		if(generateAtInstantiation):
			self.Generate()
			
	def Generate (self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png(self.spriteName)
		
class LinearBullet:
	def __init__(self, init, target, speed, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.speed = speed
		self.bullet = Bullet(self, game, spriteName, generateAtInstantiation)
	
	def Update(self):
		self.position.MoveToward(self.target, self.speed)
		
class CircularBullet:
	def __init__(self, init, target, radialSpeed, radius, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.radialSpeed = radialSpeed
		self.r = radius
		self.bullet = Bullet(self, game, spriteName, generateAtInstantiation)
	
	def Update(self):
		self.position.RotateAround(self.target, self.angularSpeed/self.game.framerate)
		
class SpiralBullet:
	def __init__(self, init, target, radialSpeed, approachSpeed, radius, game, spriteName, generateAtInstantiation = true):
		self.position = init
		self.target = target
		self.radialSpeed = radialSpeed
		self.approachSpeed = approachSpeed
		self.r = radius
		self.bullet = Bullet(game, spriteName, generateAtInstantiation)
		
	def Update(self):
		self.position.RotateAround(self.target, self,radialSpeed)
		self.position.MoveToward(self.target, self.approachSpeed)
		
		