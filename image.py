import pygame

class Image(object):
	data = {}
	@staticmethod
	def get(k):
		if k not in Image.data:
			Image.data[k] = pygame.image.load('Art Stuff\\' + k + '.png').convert_alpha()
		return Image.data[k]