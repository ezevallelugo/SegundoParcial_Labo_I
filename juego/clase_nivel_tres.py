import pygame
import random
from configuraciones import *
from clase_nivel import Nivel
from clase_jugador_enemigo import Jugador, Enemigo
from clase_plataforma import Plataforma
from clase_item import Item
from clase_recompensa import Recompensa


class NivelTres (Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #2 - Config inicial de la pantalla
        W = pantalla.get_width()
        H = pantalla.get_height()
        #Fondo
        fondo = pygame.image.load("RECURSOS/Entorno/jardin.jpg")
        fondo_escalado = pygame.transform.scale(fondo, (W,H))
        x = 0
        pantalla.blit(fondo_escalado, (x, 0))
        #Sonido
        pygame.mixer.init()
        pygame.mixer.music.load("RECURSOS/Sonidos/jardines.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        audio_historia = "RECURSOS/Sonidos/audio3.mp3"
        
        #3 - Genero un evento propio
        tick = pygame.USEREVENT + 0 #Evento propio
        pygame.time.set_timer(tick, 100) #Que se dispara cada 10 milisegundos

        #4 - Creo el entorno
        piso_superficie = pygame.image.load("RECURSOS/Entorno/piso.png")
        piso_superficie = pygame.transform.scale(piso_superficie, (1600,50))
        piso = Plataforma(piso_superficie, (0,850), None)

        columna_superficie = pygame.image.load("RECURSOS/Entorno/columna1.png")
        columna_superficie = pygame.transform.scale(columna_superficie, (100,200))
        columna_uno = Plataforma(columna_superficie,(piso.get_rectangulo().centerx - 50,piso.get_rectangulo().top - 200), None)

        plataforma_superficie = pygame.image.load("RECURSOS/Entorno/plataforma2.png")
        plataforma_superficie = pygame.transform.scale(plataforma_superficie, (300,50))
        plataforma_uno = Plataforma(plataforma_superficie, (columna_uno.get_rectangulo().centerx - 500,columna_uno.get_rectangulo().top - 100), None)
        plataforma_dos = Plataforma(plataforma_superficie, (columna_uno.get_rectangulo().centerx + 200,columna_uno.get_rectangulo().top - 100), None)
        plataforma_tres = Plataforma(plataforma_superficie, (plataforma_uno.get_rectangulo().left - 300,plataforma_uno.get_rectangulo().top - 100), None)
        plataforma_cuatro = Plataforma(plataforma_superficie, (plataforma_dos.get_rectangulo().right,plataforma_dos.get_rectangulo().top - 100), None)
        plataforma_cinco = Plataforma(plataforma_superficie, (plataforma_uno.get_rectangulo().left,plataforma_tres.get_rectangulo().top - 200), None)
        plataforma_seis = Plataforma(plataforma_superficie, (plataforma_dos.get_rectangulo().left,plataforma_cuatro.get_rectangulo().top - 200), None)

        lista_plataformas = [piso, 
                            plataforma_uno, 
                            plataforma_dos, 
                            plataforma_tres,
                            plataforma_cuatro,
                            plataforma_cinco,
                            plataforma_seis,
                            columna_uno]

        lista_plataformas_lados = []
        for i in lista_plataformas:
            lista_plataformas_lados.append(i.get_rectangulo_lados())

        #5 - Los items y trampas
        item_calavera = {}
        item_calavera["idle"] = cargar_imagenes_por_lista(calavera_uno, (50,50))
        llave_uno = Item(item_calavera["idle"][0],(plataforma_cinco.get_rectangulo().centerx, plataforma_cinco.get_rectangulo().top - 70), item_calavera)
        llave_dos = Item(item_calavera["idle"][0],(plataforma_seis.get_rectangulo().centerx, plataforma_seis.get_rectangulo().top - 70), item_calavera)

        lista_llaves = [llave_uno,llave_dos]
            
        dict_trampa = {}
        dict_trampa["idle"] = cargar_imagenes_por_lista(trampa_fuego,(50,50))
        trampa_uno = Item(dict_trampa["idle"][0],(plataforma_dos.get_rectangulo().centerx - 30, plataforma_dos.get_rectangulo().top - 50), dict_trampa)
        trampa_dos = Item(dict_trampa["idle"][0],(plataforma_tres.get_rectangulo().centerx - 30, plataforma_tres.get_rectangulo().top - 50), dict_trampa)

        lista_trampas = [trampa_uno,trampa_dos]

        dict_diamante = {}
        dict_diamante["idle"] = cargar_imagenes_por_lista(diamante_azul, (50,50))
        diamante_uno = Recompensa(dict_diamante["idle"][0],(plataforma_uno.get_rectangulo().left + 10, plataforma_uno.get_rectangulo().top - 50), dict_diamante)
        diamante_dos = Recompensa(dict_diamante["idle"][0],(plataforma_uno.get_rectangulo().right - 60, plataforma_uno.get_rectangulo().top - 50), dict_diamante)
        diamante_tres = Recompensa(dict_diamante["idle"][0],(plataforma_dos.get_rectangulo().left + 10, plataforma_dos.get_rectangulo().top - 50), dict_diamante)
        diamante_cuatro = Recompensa(dict_diamante["idle"][0],(plataforma_dos.get_rectangulo().right - 60, plataforma_dos.get_rectangulo().top - 50), dict_diamante)
        diamante_cinco = Recompensa(dict_diamante["idle"][0],(plataforma_tres.get_rectangulo().left + 10, plataforma_tres.get_rectangulo().top - 50), dict_diamante)
        diamante_seis = Recompensa(dict_diamante["idle"][0],(plataforma_tres.get_rectangulo().right - 60, plataforma_tres.get_rectangulo().top - 50), dict_diamante)
        diamante_siete = Recompensa(dict_diamante["idle"][0],(plataforma_cuatro.get_rectangulo().left + 10, plataforma_cuatro.get_rectangulo().top - 50), dict_diamante)
        diamante_ocho = Recompensa(dict_diamante["idle"][0],(plataforma_cuatro.get_rectangulo().right - 60, plataforma_cuatro.get_rectangulo().top - 50), dict_diamante)

        lista_recompensas = [diamante_uno,diamante_dos,diamante_tres,diamante_cuatro,
                             diamante_cinco,diamante_seis,diamante_siete,diamante_ocho]

        dict_pocion_salud = {}
        dict_pocion_salud["idle"] = cargar_imagenes_por_lista(pocion_salud, (50,50))
        pocion_uno = Recompensa(dict_pocion_salud["idle"][0],(plataforma_uno.get_rectangulo().centerx,plataforma_uno.get_rectangulo().top - 60),dict_pocion_salud)
        
        lista_pociones = [pocion_uno]

        #6 - El personaje, en este caso jugador
        dict_per = cargar_listas_de_imagenes_jugador(TAMAÑO_PERSONAJE)
        personaje = Jugador(dict_per["quieto"][0],(200, 600), dict_per)

        #7 - El enemigo
        dict_ene = {}
        dict_ene["caminar_derecha"] = cargar_imagenes_por_lista(enemigo_uno_camina,(90,90))
        dict_ene["caminar_izquierda"] = girar_imagenes(dict_ene["caminar_derecha"], True, False )
        dict_ene["ataque"] = cargar_imagenes_por_lista(enemigo_uno_ataque,(90,90))
        dict_ene["herido"] = cargar_imagenes_por_lista(enemigo_uno_herido,(90,90))
        bicho_uno = Enemigo(dict_ene["caminar_derecha"][0], (random.randint(1,1500),10), dict_ene) 
        bicho_dos = Enemigo(dict_ene["caminar_derecha"][0], (random.randint(1,1500),10), dict_ene)
        bicho_tres = Enemigo(dict_ene["caminar_derecha"][0], (random.randint(1,1500),10), dict_ene)
        bicho_cuatro = Enemigo(dict_ene["caminar_derecha"][0], (random.randint(1,1500),10), dict_ene)
        bicho_cinco = Enemigo(dict_ene["caminar_derecha"][0], (random.randint(1,1500),10), dict_ene)
        bicho_seis = Enemigo(dict_ene["caminar_derecha"][0], (random.randint(1,1500),10), dict_ene)

        lista_enemigos = [bicho_uno,
                          bicho_dos,
                          bicho_tres,
                          bicho_cuatro,
                          bicho_cinco,
                          bicho_seis]
        
        tiempo_duracion_segundos = 60
        tiempo_comienzo = pygame.time.get_ticks()
        tiempo_final = tiempo_comienzo + (tiempo_duracion_segundos * 1000)

        super().__init__(pantalla, personaje, lista_plataformas, lista_plataformas_lados, lista_enemigos, lista_recompensas, lista_trampas, lista_pociones, lista_llaves, tiempo_final, audio_historia, fondo_escalado)