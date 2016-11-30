from Cargar import *

def textos1(A,H,Vidas,Puntaje,Ventana):
    txt1,txt1_rect =crear_texto(A+70,H/4, 30 , 'Vidas:')
    txt2,txt2_rect =crear_texto(A+70,H/4+50, 30 , str(Vidas))
    txt3,txt3_rect =crear_texto(A+70,H/4+100, 30, 'Puntaje :')
    txt4,txt4_rect =crear_texto(A+70,H/4+150, 30, str(Puntaje))

    Ventana.blit(txt1,txt1_rect)
    Ventana.blit(txt2,txt2_rect)
    Ventana.blit(txt3,txt3_rect)
    Ventana.blit(txt4,txt4_rect)
    
 
def textos2(A2,H,Vidas,Puntaje,Ventana):
    if Vidas !=0:
        txt5,txt5_rect =crear_texto(A2/2,H/4, 38, 'Felicidades, Has Ganado!')
    else :
        txt5,txt5_rect =crear_texto(A2/2,H/4, 38, 'Has Perdido :(')
    txt6,txt6_rect =crear_texto(A2/2,H/4+50, 38, 'Tu Puntaje Fue:')
    txt7,txt7_rect =crear_texto(A2/2,H/4+100, 38, str(Puntaje))
    txt8,txt8_rect =crear_texto(A2*8/10-10,H*19/20, 20, str('Pulsa Escape para salir'))
			
    Ventana.blit(txt5,txt5_rect)
    Ventana.blit(txt6,txt6_rect)
    Ventana.blit(txt7,txt7_rect)
    Ventana.blit(txt8,txt8_rect)
    
def textos0 (A2,H,Ventana):

    txt9, txt9_rect  =crear_texto(A2/2,H/4, 38, 'BreakOut : Instrucciones')
    txt10,txt10_rect =crear_texto(A2/2,H/4+50, 38, 'Cada bloque tiene un puntaje especifico')
    txt11,txt11_rect =crear_texto(A2/2,H/4+100, 38, 'Se comienza con 3 Vidas y se juega con el mouse')
    txt12,txt12_rect =crear_texto(A2/2,H/4+150, 38, 'Si se toca el borde inferior, se pierde una vida')
    txt13,txt13_rect =crear_texto(A2/2,H/4+200, 38, 'Para Iniciar, Pulsa 2 veces Espacio!')

    Ventana.blit(txt9,txt9_rect)
    Ventana.blit(txt10,txt10_rect)
    Ventana.blit(txt11,txt11_rect)
    Ventana.blit(txt12,txt12_rect)
    Ventana.blit(txt13,txt13_rect)
			

