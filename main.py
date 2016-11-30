# ----------- CONTROLADOR ------------- #

from vista import *

#------ Propiedades de la Ventana -----

A= 640      #Ancho del area de Juego
A2 = 780    #Ancho del area de juego y del HUD
H= 480      #Alto5
FPS = 60    #Imagenes por segundo

#--------- Programa Principal ----------
        
def main():

    #Creacion de la ventana:
    Ventana = pygame.display.set_mode((A2,H))
    pygame.display.set_caption('BREIKAUT')
    
    #Reloj:
    reloj = pygame.time.Clock()
    
    #Imagen de Fondo:
    fondo = cargar_imagen('Archivos/fondo2.png',True)
    #Sonido:
    cargar_sonido()


    #Creacion de los objetos a utilizar:
    bola = Bola(A,H)
    Matriz = MatrizBloques()
    barra = Barra(A/2,H*19/20,'negra',A)
    eventos = Eventos(False)
    
    #Iteracion en la Ventana:
    while True:

	#Actualiza el fondo de pantalla:
        Ventana.blit(fondo, (0,0))
        
        #Condicion : Inicio del Juego
        if eventos.inicio == False :
            textos0(A2,H,Ventana)
            eventos.CicloInicial()
            pygame.display.flip()
            continue
        
	#Condicion : Fin del Juego 
        if bola.Vidas == 0 or bola.Bloques <= 0:
            textos2(A2,H,bola.Vidas,bola.Puntaje,Ventana)
            Matriz = MatrizBloques() 
            eventos.CicloFinal()
            pygame.display.flip()
            continue
            
        #Reloj:
        tiempo =reloj.tick(FPS)
        #Eventos del Input:
        eventos.Ciclo(bola,barra,A,H)
        
        #Actualizar Bola:
        bola.actualizarBola(tiempo,barra,Matriz.M)
        Ventana.blit(bola.image,bola.rect)
        
        #Actualizar Barra:
        barra.actualizarBarra(eventos.mouse)
        Ventana.blit(barra.image,barra.rect)

        #Actualizar Bloques:
        for i in range (0,len(Matriz.M)):
            for j in range (0,len(Matriz.M[i])):
                if Matriz.M[i][j] == 0:
                    continue
                else:
                    Ventana.blit(Matriz.M[i][j].image,Matriz.M[i][j].rect)
                    
	#Actualizar Puntaje y Vidas:
        textos1(A,H,bola.Vidas,bola.Puntaje,Ventana)
        
        pygame.display.flip()
        


if __name__=='__main__':
    pygame.init()
    main()



