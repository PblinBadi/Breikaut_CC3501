# ---- EVENTOS DEL INPUT ---- #

#Modulos y Librerias
import pygame,sys
import random
from pygame.locals import *
from Bloque import *


#Objeto Controlador del input
class Eventos:
    #Contructor:
    def __init__(self,inicio):

	#Inicio
        self.mouse = 0
        self.inicio = inicio
        
    #Ciclo del Juego
    def Ciclo(self,bola,barra,A,H):

	#Ciclo que controla los eventos
        for event in pygame.event.get():
            
            #Salida del programa 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            #Inicio / Reinicio al perder una vida
            if bola.velocidad==[0,0]:
                
                if event.type == KEYUP:

                    #Salida del Juego
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit    
		    
                    elif event.key == K_SPACE :
                        
                        barra.rect.centerx =A/2
                        barra.rect.centery =H*19/20
                        bola.rect.centerx =A/2
                        bola.rect.centery = H*19/20-20
                        
                        # Velocidad de inicio (Aleatoria)
                        Random = random.uniform(-0.5,0.5)
                        while abs(Random)<0.3:
                            Random = random.uniform(-0.5,0.5)
                            
                        bola.velocidad =bola.velocidad = [Random,-abs(Random)]
                            
            # Mientras Esta Jugando
            else:	
                #Movimiento del Mouse    
                if event.type == MOUSEMOTION:
                    self.mouse = event.pos[0]

                    #Acciones Con las Teclas:
                elif event.type == KEYUP:

                #Salir del Juego
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
    
    def CicloInicial(self):
        
        # Controla el Ciclo Inicial (Instrucciones y Partida):
        
        for event in pygame.event.get():
                    
        #Salida del programa 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYUP:
                
                #Salida del Juego
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit    
                #Inicio del Juego
                elif event.key == K_SPACE :
                    self.inicio = True

    
    def CicloFinal(self):
        
        # Controla el Ciclo Final(Salida):
        
        for event in pygame.event.get():
                    
        #Salida del programa 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYUP:
                #Salida del Juego
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit    

                
            


