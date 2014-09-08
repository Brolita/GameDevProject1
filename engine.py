class Engine:
	def __init__(self):
		self.gameObjects = []
		
	def update(self):
		for i in range(self.gameObjects):
			try:
				self.gameObjects[i].update()
			except(AttributeError):
				print self.gameObject.__class__, "is listed as a gameobject but has no update function"
	
	def draw(self):
		for i in range(self.gameObjects):
			try:
				self.gameObjects[i].update()
			except(AttributeError):
				print self.gameObject.__class__, "is listed as a gameobject but has no draw function"
	