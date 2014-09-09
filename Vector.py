class Vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def Difference(self, pos):
		#calculates the difference between a this vector and another
		if type(pos) is Vector:
			return math.sqrt((self.x-pos.x)**2 + (self.y-pos.y)**2)
		elif type(pos) is tuple or type(pos) is list:
			return math.sqrt((self.x-pos[0])**2 + (self.y-pos[1])**2)
			
	def Add(self, delta):
		#move this vector a certain x and y
		if type(pos) is Vector:
			self.x += pos.x
			self.y += pos.y
		elif type(pos) is tuple or type(pos) is list:
			self.x += pos[0]
			self.y += pos[1]
	
	def Dot(self, other):
		return Vector(self.x * other.x, self.y * other.y)
	
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)
		
	def __iadd__(self, other):
		self.Add(other)
		
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y)
		
	def __isub__(self, other):
		self.Add(-other)
		
	def __neq__(self):
		return Vector(-self.x, -self.y)
		
	def __mul__(self, other):
		return self.Dot(other)
	
	def __str__(self):
		print 'Vector(', self.x, ',', self.y, ')'
	
	def Magnitude(self):
		#returns the magnitude of the vector
		return math.sqrt((self.x)**2 + (self.y)**2)
		
	def Unit(self):
		#returns the unit vector (its magnitude will be 1)
		return Vector(self.x/self.Magnitude(), self.y/self.Magnitude())
	
	def MoveToward(self, pos, dis):
		#move this vector towards another point
		if type(pos) is Vector:
			Move( Vector( pos.x * (dis / self.Difference(pos)), pos.y * (dis / self.Difference(pos)) ) )
		elif type(pos) is tuple or type(pos) is list:
			Move( Vector( pos[0] * (dis / self.Difference(pos)), pos[1] * (dis / self.Difference(pos)) ) )
	
	def RotateAround(self, center, rad):
		#rotate this vector around another
		if type(center) is Vector:
			self.x = (self.x - center.x) * math.cos(rad) - (self.y - center.y) * math.sin(rad) + center.x
			self.y = (self.x - center.x) * math.sin(rad) + (self.y - center.y) * math.cos(rad) + center.y
		elif type(pos) is tuple or type(pos) is list:
			self.x = (self.x - center[0]) * math.cos(rad) - (self.y - center[1]) * math.sin(rad) + center[0]
			self.y = (self.x - center[0]) * math.sin(rad) + (self.y - center[1]) * math.cos(rad) + center[1]
	
	def ThirdOrderControl(self, velocity, acceleration):
		#for much more complicated control
		if not type(velocity) is Vector or not type(acceleration) is Vector:
			return
		velocity.x += acceleration.x
		velocity.y += acceleration.y
		self.x += velocity.x
		self.y += velocity.y