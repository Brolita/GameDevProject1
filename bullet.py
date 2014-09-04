class Bullet(pygame.sprite.Sprite):
	def __init__ (self, game, spriteName, generateAtInstantiation = true):
		self.spriteName = spriteName
		self.game = game
		if(generateAtInstantiation):
			self.Generate()
			
	def Generate (self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_png(self.spriteName)
		
	def Update (self):
	
	def Draw (self):
		