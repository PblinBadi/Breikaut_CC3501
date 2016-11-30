#Modulos
import pygame,sys
from pygame.locals import *
from Cargar import *
import math

# Objeto Bola !

class Bola(pygame.sprite.Sprite):
    def __init__(self,A,H):
        pygame.sprite.Sprite.__init__(self)
        self.image = cargar_imagen("Archivos/Sprites/Balls/azul.png", True)
        self.rect = self.image.get_rect()
        
        #Posicion de la Bola
        self.rect.centerx = A/2
        self.rect.centery = H*19/20-20
        
        #Velocidad de lq Bola
        self.velocidad = [0,0]
        
        #Variables de la Ventana 
        self.A = A
        self.H = H
        
        #Puntajes, Vida, Bloques restantes
        self.Puntaje = 0
        self.Vidas = 3
        self.Bloques= 48
        #Auxiliares : Colisiones con los Bloques
        
        self.Cx = False
        self.Cy = False

  
    def actualizarBola(self,tiempo,barra,Matriz):

        #Actualizacion de la Posicion:
        self.rect.centerx +=self.velocidad[0]*tiempo
        self.rect.centery +=self.velocidad[1]*tiempo
        
        #Colisiones con las paredes:

        #Costados:
        if self.rect.left <= 2 or self.rect.right >=self.A-2:
            self.velocidad[0] = -self.velocidad[0]
            self.rect.centerx += self.velocidad[0]*tiempo

            
        #Superior
        if self.rect.top <= 0:
            self.velocidad[1] = -self.velocidad[1]
            self.rect.centery += self.velocidad[1]*tiempo
            
        #Inferior [Caso en el que se descuenta una vida]
        if self.rect.bottom >= self.H:
            self.velocidad[1] = -self.velocidad[1]
            self.rect.centery += self.velocidad[1]*tiempo
            
            
            #Reinicio :
            self.Vidas = self.Vidas - 1
            self.velocidad = [0,0]
            
            self.rect.centerx = self.A/2
            self.rect.centery = self.H*19/20-20
            barra.rect.centerx = self.A/2
            barra.rect.centery = self.H*19/20
            

        #Colisiones con la barra:
        if self.rect.colliderect(barra.rect):
            
            #Colision a la derecha y centro
            d = abs (barra.rect.centerx-self.rect.centerx)
            if self.rect.centerx < barra.rect.centerx:
                self.velocidad[0] = -math.sin(math.radians(d))/1.25
                
            #Colision a la izquierda  
            elif self.rect.centerx > barra.rect.centerx:
                self.velocidad[0] = math.sin(math.radians(d))/1.25

            self.velocidad[1] = -self.velocidad[1]
            self.rect.centery += self.velocidad[1]*tiempo

            
            
        #Colisiones con los Bloques
        else:
            #Reinicio las variables auxiliares
            self.Cx = False
            self.Cy = False
            for i in range(0,len(Matriz)):
                for j in range(0,len(Matriz[i])):
                    #Verificamos si ya fue golpeado el bloque
                    if Matriz[i][j] == 0:
                        continue
                    #Si no, vemos las colisiones :
                    elif self.rect.colliderect(Matriz[i][j].rect):
                        #Colision Superior/Inferior:
                        if self.rect.top <= Matriz[i][j].rect.bottom or self.rect.bottom <= Matriz[i][j].rect.top:
                            self.Puntaje = self.Puntaje+ Matriz[i][j].puntaje
                            self.Cy = True 

                        #Colision Derecha/Izquierda:
                        if self.rect.left <= Matriz[i][j].rect.right or self.rect.right < Matriz[i][j].rect.left:
                            self.Puntaje = self.Puntaje+ Matriz[i][j].puntaje
                            self.Cx = True
                            
                        #Borrar el bloque golpeado y descontar 1 a los bloques restantes
                        Matriz[i][j] = 0
                        self.Bloques = self.Bloques-1
                        
            #Cambio de Velocidad de la bola:
            if self.Cy == True:
                
                self.velocidad[1] = -self.velocidad[1]
                self.rect.centerx += self.velocidad[1]*tiempo

            if self.Cx == True :
                self.velocidad[0]= -self.velocidad[0]
                self.rect.centery += self.velocidad[0]*tiempo
                                 



                        
                        

					
        

        

    
