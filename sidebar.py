import pygame
from image import Image
	
class Sidebar(object):
	font = None
	def __init__(self):
		self._lives = 4
		self._points = 0
		if Sidebar.font == None:
			Sidebar.font = pygame.font.SysFont("monospace",22)
		self._refresh()
		
	def _refresh(self):
		self.image = pygame.image.load('Art Stuff\\side.png').convert_alpha()
		self.__draw_lives()
		self.__draw_points()
		
	def draw(self, screen):
		screen.blit(self.image, (600,0))
		
	def __draw_lives(self):
		for i in range(self._lives):
			if 18 + 33 * i < 182:
				self.image.blit(Image.get("penguin"), (17 + 33 * i, 470))
			else:
				self.image.blit(Image.get("penguin"), (17 + 33 * (i - 5), 510))
	
	def __draw_points(self):
		s = ''
		for i in range(len(str(self._points))):
			s += str(self.points)[i]
		
		while len(s) < 8:
			s = '0' + s
			
		self.image.blit(Sidebar.font.render(s, 2, (255, 255, 255)), (22, 100))
	
	def _get_lives(self):
		return self._lives
		
	def _set_lives(self, lives):	
		self._lives = lives
		self._refresh()
		
	def _get_points(self):
		return self._points
		
	def _set_points(self, points):
		p = self._points%5000
		self._points = points
		if self._points%5000 < p:
			self._lives += 1
		self._refresh()
		
	lives = property(_get_lives, _set_lives)
	points = property(_get_points, _set_points)