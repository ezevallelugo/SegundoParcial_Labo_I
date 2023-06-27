import pygame

#Constantes
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)
WIDTH = 100
HEIGHT = 100
ANCHO = 1600
LARGO = 900
TAMAÑO_PERSONAJE = (WIDTH, HEIGHT)
TAMAÑO_PANTALLA = (ANCHO, LARGO)
flag = True
DEBUG = False

#Animaciones
personaje_quieto = [pygame.image.load("RECURSOS/Jugador/Postura/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/0.png"),                    
                    pygame.image.load("RECURSOS/Jugador/Postura/1.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/1.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/1.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/2.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/2.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/2.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/3.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/3.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/3.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/4.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/4.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/4.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/5.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/5.png"),
                    pygame.image.load("RECURSOS/Jugador/Postura/5.png")]

personaje_camina_derecha = [pygame.image.load("RECURSOS/Jugador/Correr/1.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/1.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/1.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/2.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/2.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/2.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/3.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/3.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/3.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/4.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/4.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/4.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/5.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/5.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/5.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/6.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/6.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/6.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/7.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/7.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/7.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/8.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/8.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/8.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/9.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/9.png"),
                            pygame.image.load("RECURSOS/Jugador/Correr/9.png")]

personaje_salta = [pygame.image.load("RECURSOS/Jugador/Saltar/0.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/0.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/0.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/1.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/1.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/1.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/2.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/2.png"),
                   pygame.image.load("RECURSOS/Jugador/Saltar/2.png")]

personaje_cae = [pygame.image.load("RECURSOS/Jugador/Caer/0.png")]

personaje_herido = [pygame.image.load("RECURSOS/Jugador/Herido/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Herido/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Herido/0.png")]

personaje_ataque = [pygame.image.load("RECURSOS/Jugador/Ataque_suelo/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/0.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/1.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/1.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/1.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/2.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/2.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/2.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/3.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/3.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/3.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/4.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/4.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/4.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/5.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/5.png"),
                    pygame.image.load("RECURSOS/Jugador/Ataque_suelo/5.png")]

enemigo_uno_camina = [pygame.image.load("RECURSOS/Enemigo/Camina/0.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/0.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/0.png"),                    
                      pygame.image.load("RECURSOS/Enemigo/Camina/1.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/1.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/1.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/2.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/2.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/2.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/3.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/3.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/3.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/4.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/4.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/4.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/5.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/5.png"),
                      pygame.image.load("RECURSOS/Enemigo/Camina/5.png")]

enemigo_uno_ataque = [pygame.image.load("RECURSOS/Enemigo/Ataque/0.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/0.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/0.png"),                    
                      pygame.image.load("RECURSOS/Enemigo/Ataque/1.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/1.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/1.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/2.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/2.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/2.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/3.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/3.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/3.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/4.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/4.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/4.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/5.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/5.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/5.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/6.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/6.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/6.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/7.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/7.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/7.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/8.png"),
                      pygame.image.load("RECURSOS/Enemigo/Ataque/8.png")]

enemigo_uno_herido = [pygame.image.load("RECURSOS/Enemigo/Herido/0.png")]

jefe_camina_izquierda = [pygame.image.load("RECURSOS/Jefe/Camina/0.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/0.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/0.png"),                    
               pygame.image.load("RECURSOS/Jefe/Camina/1.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/1.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/1.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/2.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/2.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/2.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/3.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/3.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/3.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/4.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/4.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/4.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/5.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/5.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/5.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/6.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/6.png"),
               pygame.image.load("RECURSOS/Jefe/Camina/6.png")]

jefe_ataque = [pygame.image.load("RECURSOS/Jefe/Ataque/1.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/1.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/1.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/2.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/2.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/2.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/3.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/3.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/3.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/4.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/4.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/4.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/5.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/5.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/5.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/6.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/6.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/6.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/7.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/7.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/7.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/8.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/8.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/8.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/9.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/9.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/9.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/10.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/10.png"),
               pygame.image.load("RECURSOS/Jefe/Ataque/10.png")]

jefe_herido = [pygame.image.load("RECURSOS/Jefe/Herido/0.png")]

calavera_uno = [pygame.image.load("RECURSOS/Item/Calavera_dorada/01.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/01.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/01.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/02.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/02.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/02.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/03.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/03.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/03.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/04.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/04.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/04.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/05.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/05.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/05.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/06.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/06.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/06.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/07.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/07.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/07.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/08.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/08.png"),
            pygame.image.load("RECURSOS/Item/Calavera_dorada/08.png")]

trampa_fuego = [pygame.image.load("RECURSOS/Item/Trampa/0.png"),
              pygame.image.load("RECURSOS/Item/Trampa/0.png"),
              pygame.image.load("RECURSOS/Item/Trampa/0.png"),
              pygame.image.load("RECURSOS/Item/Trampa/1.png"),
              pygame.image.load("RECURSOS/Item/Trampa/1.png"),
              pygame.image.load("RECURSOS/Item/Trampa/1.png"),
              pygame.image.load("RECURSOS/Item/Trampa/2.png"),
              pygame.image.load("RECURSOS/Item/Trampa/2.png"),
              pygame.image.load("RECURSOS/Item/Trampa/2.png"),
              pygame.image.load("RECURSOS/Item/Trampa/3.png"),
              pygame.image.load("RECURSOS/Item/Trampa/3.png"),
              pygame.image.load("RECURSOS/Item/Trampa/3.png"),
              pygame.image.load("RECURSOS/Item/Trampa/4.png"),
              pygame.image.load("RECURSOS/Item/Trampa/4.png"),
              pygame.image.load("RECURSOS/Item/Trampa/4.png")]

diamante_azul = [pygame.image.load("RECURSOS/Item/Diamante_azul/01.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/01.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/01.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/02.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/02.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/02.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/03.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/03.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/03.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/04.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/04.png"),
                 pygame.image.load("RECURSOS/Item/Diamante_azul/04.png"),]

pocion_salud = [pygame.image.load("RECURSOS/Item/Pocion_rojo/01.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/01.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/01.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/02.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/02.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/02.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/03.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/03.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/03.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/04.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/04.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/04.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/05.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/05.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/05.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/06.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/06.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/06.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/07.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/07.png"),
                pygame.image.load("RECURSOS/Item/Pocion_rojo/07.png"),]


#Funciones generales
def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG

def get_mode():
    return DEBUG

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista_animaciones, escala):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, escala)

def cargar_listas_de_imagenes_jugador(escala):
    diccionario = {}
    diccionario["quieto"] = cargar_imagenes_por_lista(personaje_quieto, escala)
    diccionario["quieto_izq"] = girar_imagenes(diccionario["quieto"], True, False)
    diccionario["caminar_derecha"] = cargar_imagenes_por_lista(personaje_camina_derecha, escala)
    diccionario["caminar_izquierda"] = girar_imagenes(diccionario["caminar_derecha"], True, False)
    diccionario["saltar"] = cargar_imagenes_por_lista(personaje_salta, escala)
    diccionario["saltar_izq"] = girar_imagenes(diccionario["saltar"], True, False)   
    diccionario["caida"] = cargar_imagenes_por_lista(personaje_cae, escala)
    diccionario["caida_izq"] = girar_imagenes(diccionario["caida"],True,False)
    diccionario["herido"] = cargar_imagenes_por_lista(personaje_herido, escala)
    diccionario["ataque_suelo"] = cargar_imagenes_por_lista(personaje_ataque, escala)
    diccionario["ataque_suelo_izq"] = girar_imagenes(diccionario["ataque_suelo"], True, False)
    return diccionario 

def cargar_imagenes_por_lista(lista: list,escala: tuple):
    nueva_lista = []
    for i in lista:        
        imagen = pygame.transform.scale(i,escala)
        nueva_lista.append(imagen)
    return nueva_lista


