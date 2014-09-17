import pygame
import math
from Vector import Vector
from snowball import Snowball
from image import Image

class Dialogue:
	def __init__(self, image, d, c, game, player, ref, delay = 0):
		self.name = "Dialogue"
		self.game = game
		game.gameObjects.append(self)
		if Image.font == None:
			Image.font = pygame.font.SysFont("monospace",18)
		self.image = Image.get('avatars\\' + image)
		
		lines = []
		while True:
			if len(d) < 40:
				lines.append(d)
				break
			else:
				char = ''
				i = 40
				while char != ' ':
					i-=1
					char = d[i]
				lines.append(d[:i])
				d = d[i:]
		
		self.value = pygame.image.load("Art stuff\\textbox.png")
		for i in range(len(lines)):
			self.value.blit(Image.font.render(lines[i].strip(), 1, c), (4, 10 + 30 * i))
		self.player = player
		self.lock = player.firing
		self.ref = ref
		self.delay = delay
	
	def update(self):
		if self.lock and not self.player.firing:
			self.lock = False
			
		if self.player.firing and not self.lock:
			self.flag()
			
	def draw(self, screen):
		if self.delay == 0:
			screen.blit(self.image, (40, 600))
			screen.blit(self.value, (110, 581))
		else: 
			self.delay -= 1
	
	def flag(self):
		self.game.flag(self)

class Player:
	def __init__ (self, game):
		self.image = self.center = Image.get("penguin")
		self.left = Image.get("penguin_L")
		self.right = Image.get("penguin_R")
		
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 400
		self.x_velocity = 5
		self.y_velocity = 5
		self.moving = [False, False, False, False] #up, down, left, right, self.focus
		self.focus = False
		self.firing = False
		self.snowballs = []
		self.fireCooldown = 3
		self.canFire = True
		self.game = game
		self.name = 'Player'
		self.invinsibility = 0
		#self.dash = False
		self.dashLength = 0
		game.gameObjects.append(self)
	
	def update(self):
		self.fireCooldown -= 1
		if self.fireCooldown < 1:
			self.canFire = True
			self.fireCooldown = 0
			
		if (self.firing and self.canFire):
			snowball = Snowball(self.rect.x, self.rect.y, self.game)
			self.snowballs.append(snowball)
			self.fireCooldown = 5
			self.canFire = False
			
		if self.moving[0]:
			if self.focus:
				future = self.rect.move(0, -self.y_velocity/2.5)
			else:
				future = self.rect.move(0, -self.y_velocity)
			if future.top < 0:
				self.rect.top = 0
				
			else:
				self.rect = future
				
		elif self.moving[1]:
			if self.focus:
				future = self.rect.move(0, self.y_velocity/2.5)
			else:
				future = self.rect.move(0, self.y_velocity)
			if future.bottom > 800:
				self.rect.bottom = 800
				
			else:
				self.rect = future
				
		if self.moving[2]:
			self.image = self.left
			if self.focus:
				future = self.rect.move(-self.x_velocity/2.5, 0)
			else:
				future = self.rect.move(-self.x_velocity, 0)
			if future.left < 0:
				self.rect.left = 0
				
			else:
				self.rect = future
				
		elif self.moving[3]:
			self.image = self.right
			if self.focus:
				future = self.rect.move(self.x_velocity/2.5, 0)
			else:
				future = self.rect.move(self.x_velocity, 0)
			if future.right > 600:
				self.rect.right = 600
				
			else:
				self.rect = future
		else:
			self.image = self.center
				
		if self.invinsibility != 0:
			self.invinsibility -= 1
				
	def getPosition(self):
		#print 'Player is currently at', self.rect.x + 16, ', ', self.rect.y + 48
		return Vector(self.rect.x + 15, self.rect.y + 15)
	
	def get_rect(self):
		return self.rect
		
	def draw(self, screen):
		screen.blit(self.image, self.rect, [0, 0, 32, 48])
		
		#for projectile in self.snowballs:
		#	projectile.update(screen)
		#	if projectile.rect.y < -5:
		#		self.snowballs.remove(projectile)
	
	def dash(self, sidebar):
		self.dash = True
		self.dashLength = 0
		sidebar.dash -= 1
		
	def flag(self):
		self.rect.x = 300
		self.rect.y = 400
		self.x_velocity = 5
		self.y_velocity = 5
		self.moving = [False, False, False, False] #up, down, left, right, self.focus
		self.focus = False
		self.firing = False
		self.snowballs = []
		self.fireCooldown = 5
		self.canFire = True
		self.name = 'Player'
		self.invinsibility = 0
		#self.dash = False
		self.dashLength = 0