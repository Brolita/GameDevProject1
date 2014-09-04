class Vector:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	
	def Distance(pos):
		if type(pos) is Vector:
			return math.sqrt((self.x-pos.x)**2 + (self.y-pos.y)**2))
		elif type(pos) is tuple or type(pos) is list:
			return math.sqrt((self.x-pos[0])**2 + (self.y-pos[1])**2))
			
	def Move(pos):
		if type(pos) is Vector:
			self.x += pos.x
			self.y += pos.y
		elif type(pos) is tuple or type(pos) is list:
			self.x += pos[0]
			self.y += pos[1]
	
	def MoveToward(pos, dis):
		if type(pos) is Vector:
			Move( Vector( pos.x * (dis / Distance(pos)), pos.y * (dis / Distance(pos)) ) )
		elif type(pos) is tuple or type(pos) is list:
			Move( Vector( pos[0] * (dis / Distance(pos)), pos[1] * (dis / Distance(pos)) ) )
	
	def RotateAround(center, dis):
		if type(center) is Vector:
			self.x = (self.x - center.x) * math.cos(dis / Distance(center)) - (self.y - center.y) * math.sin(dis / Distance(center)) + center.x
			self.y = (self.x - center.x) * math.sin(dis / Distance(center)) + (self.y - center.y) * math.cos(dis / Distance(center)) + center.y
		elif type(pos) is tuple or type(pos) is list:
			self.x = (self.x - center[0]) * math.cos(dis / Distance(center)) - (self.y - center[1]) * math.sin(dis / Distance(center)) + center[0]
			self.y = (self.x - center[0]) * math.sin(dis / Distance(center)) + (self.y - center[1]) * math.cos(dis / Distance(center)) + center[1]
	
	def RotateAroundElipse(center, a, b, dis):
		if type(center) is Vector:
			self.x = (self.x - center.x) * a * math.cos(dis / Distance(center)) - (self.y - center.y) * b * math.sin(dis / Distance(center)) + center.x
			self.y = (self.x - center.x) * b * math.sin(dis / Distance(center)) + (self.y - center.y) * a * math.cos(dis / Distance(center)) + center.y
		elif type(pos) is tuple or type(pos) is list:
			self.x = (self.x - center[0]) * a * math.cos(dis / Distance(center)) - (self.y - center[1]) * b * math.sin(dis / Distance(center)) + center[0]
			self.y = (self.x - center[0]) * b * math.sin(dis / Distance(center)) + (self.y - center[1]) * a * math.cos(dis / Distance(center)) + center[1]
	