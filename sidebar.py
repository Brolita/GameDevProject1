import pygame
from image import Image
	
class Sidebar(object):
	def __init__(self):
		self._lives = 4
		self._dash = 4
		self._refresh()
		
	def _refresh(self):
		print "refresh called", self._lives
		self.image = pygame.image.load('Art Stuff\\side.png').convert_alpha()
		self.__draw_lives()
		self.__draw_dash()
		
	def draw(self, screen):
		screen.blit(self.image, (600,0))
		
	def __draw_lives(self):
		for i in range(self._lives):
			if 18 + 33 * i < 182:
				self.image.blit(Image.get("penguin"), (17 + 33 * i, 470))
			else:
				self.image.blit(Image.get("penguin"), (17 + 33 * (i - 5), 510))
	
	def __draw_dash(self):
		for i in range(self._lives):
			if 18 + 33 * i < 182:
				self.image.blit(Image.get("penguin"), (17 + 33 * i, 610))
			else:
				self.image.blit(Image.get("penguin"), (17 + 33 * (i - 5), 650))
	
	def _get_lives(self):
		print 'returned', self._lives
		return self._lives
		
	def _set_lives(self, lives):
		print 'setting lives to', self._lives
		self._lives = lives
		self._refresh()
		
	def _get_dash(self):
		return self._dash
		
	def _set_dash(self, dash):
		self._dash = dash
		self._refresh()
		
	lives = property(_get_lives, _set_lives)
	dash = property(_get_dash, _set_dash)