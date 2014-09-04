class Game:
	def __init__ (self):
		self.pygame = pygame.init()
		self.bullets = list()
		
	def Update(self):
		for i in range(len(self.bullets)):
			self.bullets[i].Update()
	
	def Draw(self):
		for i in range(len(self.bullets)):
			self.bullets[i].Draw()