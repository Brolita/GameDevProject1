import math

class Vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def Difference(self, pos):
		#calculates the difference between a this vector and another
		if isinstance(pos, Vector):
			return math.sqrt((self.x-pos.x)**2 + (self.y-pos.y)**2)
		elif type(pos) is tuple or type(pos) is list:
			return math.sqrt((self.x-pos[0])**2 + (self.y-pos[1])**2)
		else:
			print "type mismatch Vector.py, line 66:", center.__class__, "type given"
			
	def Add(self, delta):
		#move this vector a certain x and y
		if isinstance(delta, Vector):
			self.x += delta.x
			self.y += delta.y
		elif type(delta) is tuple or type(delta) is list:
			self.x += delta[0]
			self.y += delta[1]
	
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
		return Vector(self.x * other, self.y * other)
	
	def __str__(self):
		return 'Vector(' + self.x.__str__() + ',' + self.y.__str__() + ')'
		
	def copy(self):
		return Vector(self.x, self.y)
	
	def Magnitude(self):
		#returns the magnitude of the vector
		return math.sqrt((self.x)**2 + (self.y)**2)
		
	def Unit(self):
		#returns the unit vector (its magnitude will be 1)
		return Vector(self.x/self.Magnitude(), self.y/self.Magnitude())
	
	def MoveToward(self, pos, dis):
		#move this vector towards another point
		Vector( (self.x - pos.x) * (dis / self.Difference(pos)), (self.y - pos.y) * (dis / self.Difference(pos)) )
		if isinstance(pos, Vector):
			self.Add( Vector( (pos.x - self.x) * (dis / self.Difference(pos)), (pos.y - self.y) * (dis / self.Difference(pos)) ) )
		elif type(pos) is tuple or type(pos) is list:
			self.Add( Vector( (pos[0] - self.x) * (dis / self.Difference(pos)), (pos[1] - self.y) * (dis / self.Difference(pos)) ) )
		else:
			print "type mismatch Vector.py, line 66:", center.__class__, "type given"
	
	def RotateAround(self, center, rad):
		#rotate this vector around another
		if isinstance(center, Vector):
			ax = (self.x - center.x) * math.cos(rad) - (self.y - center.y) * math.sin(rad) + center.x
			ay = (self.x - center.x) * math.sin(rad) + (self.y - center.y) * math.cos(rad) + center.y
			self.x = ax
			self.y = ay
		elif type(center) is tuple or type(center) is list:
			ax = (self.x - center[0]) * math.cos(rad) - (self.y - center[1]) * math.sin(rad) + center[0]
			ay = (self.x - center[0]) * math.sin(rad) + (self.y - center[1]) * math.cos(rad) + center[1]
			self.x = ax
			self.y = ay
		else:
			print "type mismatch Vector.py, line 66:", center.__class__, "type given"
	
	def ThirdOrderControl(self, velocity, acceleration):
		#for much more complicated control
		if not isinstance(velocity, Vector) or not isinstance(acceleration, Vector):
			return
		velocity.x += acceleration.x
		velocity.y += acceleration.y
		self.x += velocity.x
		self.y += velocity.y