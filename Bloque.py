#Modulos
import pygame
from pygame.locals import *

from Cargar import *

#Objeto : Bloques

#Bloque Verde
class Bloque(pygame.sprite.Sprite):
    def __init__(self,posx,posy,Color):
        pygame.sprite.Sprite.__init__(self)
        self.puntaje = 0
        #Color del Sprite del Bloque
        if Color == 'verde':
            self.image = cargar_imagen("Archivos/Sprites/Bricks/verde.png", True)
            self. puntaje = 50
        elif Color == 'azul':
            self.image = cargar_imagen("Archivos/Sprites/Bricks/azul.png", True)
            self.puntaje = 25
        elif Color == 'violeta':
            self.image = cargar_imagen("Archivos/Sprites/Bricks/violeta.png", True)
            self.puntaje = 15
        elif Color == 'rosado':
            self.image = cargar_imagen("Archivos/Sprites/Bricks/rosado.png", True)
            self.puntaje = 15
        else:
            self.image = cargar_imagen("Archivos/Sprites/Bricks/amarillo.png", True)
            self.puntaje = 5

        #Creacion del Rect    
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy

class MatrizBloques :
    def __init__ (self) :

        self.M = []
        self.colores = ['verde','azul','violeta','amarillo']
        for i in range (0,12):
            self.M.append([])
            for j in range(0,4):
                self.M[i].append(Bloque(56+48*i,71+j*22,self.colores[j]))	
				


				
		
				
	
				


