import pygame, sys	
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from numpy import asarray, savetxt

class Game():

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((560, 560))
		self.m_pos = pygame.mouse.get_pos()
		self.color = (255, 255, 255)
		self.draw_window()

	def draw_window(self):
		self.screen.fill((0, 0, 0))
		pygame.display.flip()

	def drawing(self):
		if pygame.mouse.get_pressed()[0]:
			x = pygame.mouse.get_pos()[0] - pygame.mouse.get_pos()[0]%20
			y = pygame.mouse.get_pos()[1] - pygame.mouse.get_pos()[1]%20
			pygame.draw.rect(self.screen, self.color, (x, y, 40, 40))
			pygame.display.flip()




def main():
	game = Game()
	amount = 1;
	number = 0
	img = []
	d = []
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				for y in range(28):
					for x in range(28):
						if game.screen.get_at((20*x,20*y))[0]==0:
							d.append(0)
						else:
							d.append(1)
					img.append(d)
					d = []
				data = asarray(img)
				savetxt('images/{}/data_{}.csv'.format(number, amount), data, delimiter=',')
				amount += 1
				if amount%21 == 0:
					number += 1
					amount = 1
					print(number)
				img = []
				Game.draw_window(game)
		Game.m_pos = pygame.mouse.get_pos()
		Game.drawing(game)

main()