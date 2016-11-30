#Funciones Auxiliares : 

import pygame,sys
from pygame.locals import *

#Carga una imagen y la convierte a un rect:

def cargar_imagen(Archivo, transparent=True):
        try :
                image = pygame.image.load(Archivo)
	except pygame.error, message : 
		raise SystemExit,message
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color,pygame.RLEACCEL)
	return image 

#Crea un texto y lo conviertde a rect:

def crear_texto(x,y,tamano,texto):
	
	fuente = pygame.font.Font('Archivos/replay.ttf',tamano)
	texto = pygame.font.Font.render(fuente,texto,1,(255,255,255))
	texto_rect = texto.get_rect()
	texto_rect.centerx = x
	texto_rect.centery = y
	return texto,texto_rect

def cargar_sonido ():
        channell = pygame.mixer.Channel(0)
        channell.set_volume(0.5)
        sonido = pygame.mixer.Sound('Archivos/Musica.wav')
        channell.play(sonido)
        

	
