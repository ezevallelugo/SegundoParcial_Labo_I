import pygame
import sys
from configuraciones import *
from Gui.GUI_form_principal import *

#1 - Inicio de pygame
pygame.init()
RELOJ = pygame.time.Clock()

#2 - Config inicial de la pantalla
#Ventana
screen = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("LAS PRUEBAS")
icono = pygame.image.load("RECURSOS/icon.png")
pygame.display.set_icon(icono)
form_prueba = FormPrueba(screen,400,100,800,600,"Gold","Blue",True,"RECURSOS/UI/tabla2.png")


while True:
    RELOJ.tick(60)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos: 
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    form_prueba.update(lista_eventos)



    pygame.display.flip()