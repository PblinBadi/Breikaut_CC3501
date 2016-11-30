#Modulos
import pygame
from pygame.locals import *

from Cargar import *

#Objeto : Barra

class Barra(pygame.sprite.Sprite):
    def __init__(self,x,y,Color,A):
        #Crea el objeto Barra :
        
        #Variables
        self.A = A

        #Importar el Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("Archivos/Sprites/Bats/barranegra3.png", True)

        #Creacion del Rect    
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


    def actualizarBarra(self,mouse):
        #Actualiza la posicion de la barra utilizando las coordenadas del mouse.
        #Verificamos si esta dentro del area de juego:
        if not(mouse >= self.A-47 or mouse <= 47):
            self.rect.centerx = mouse
                
            
        
            
        


