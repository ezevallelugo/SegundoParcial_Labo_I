import pygame
import sqlite3
from configuraciones import *
from clase_nivel import Nivel
from clase_jugador_enemigo import Jugador, Enemigo
from clase_plataforma import Plataforma
from clase_item import Item
from clase_recompensa import Recompensa


class NivelCinco (Nivel):
    def __init__(self, pantalla: pygame.Surface) -> None:
        #2 - Config inicial de la pantalla
        W = pantalla.get_width()
        H = pantalla.get_height()
        #Fondo
        fondo = pygame.image.load("RECURSOS/Entorno/culto.jpg")
        fondo_escalado = pygame.transform.scale(fondo, (W,H))
        x = 0
        pantalla.blit(fondo_escalado, (x, 0))
        #Sonido
        pygame.mixer.init()
        pygame.mixer.music.load("RECURSOS/Sonidos/musica_jefe.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

        #3 - Genero un evento propio
        tick = pygame.USEREVENT + 0 #Evento propio
        pygame.time.set_timer(tick, 100) #Que se dispara cada 10 milisegundos

        #4 - Creo el entorno
        piso_superficie = pygame.image.load("RECURSOS/Entorno/piso.png")
        piso_superficie = pygame.transform.scale(piso_superficie, (1600,50))
        piso = Plataforma(piso_superficie, (0,850), None)

        plataforma_superficie = pygame.image.load("RECURSOS/Entorno/plataforma2.png")
        plataforma_superficie = pygame.transform.scale(plataforma_superficie, (300,50))
        plataforma_uno = Plataforma(plataforma_superficie, (piso.get_rectangulo().left,piso.get_rectangulo().top - 150), None)
        plataforma_dos = Plataforma(plataforma_superficie, (piso.get_rectangulo().right - 300,piso.get_rectangulo().top - 150), None)

        lista_plataformas = [piso, 
                            plataforma_uno,
                            plataforma_dos]

        lista_plataformas_lados = []
        for i in lista_plataformas:
            lista_plataformas_lados.append(i.get_rectangulo_lados())

        #5 - Los items y trampas
        item_calavera = {}
        item_calavera["idle"] = cargar_imagenes_por_lista(calavera_uno, (50,50))
        llave_uno = Item(item_calavera["idle"][0],(plataforma_dos.get_rectangulo().centerx - 20, plataforma_dos.get_rectangulo().top - 70), item_calavera)

        lista_llaves = [llave_uno]
            
        dict_trampa = {}
        dict_trampa["idle"] = cargar_imagenes_por_lista(trampa_fuego,(50,50))
        trampa_uno = Item(dict_trampa["idle"][0],(piso.get_rectangulo().centerx - 200, piso.get_rectangulo().top - 50), dict_trampa)
        trampa_dos = Item(dict_trampa["idle"][0],(piso.get_rectangulo().centerx + 200, piso.get_rectangulo().top - 50), dict_trampa)

        lista_trampas = [trampa_uno,trampa_dos]

        dict_diamante = {}
        dict_diamante["idle"] = cargar_imagenes_por_lista(diamante_azul, (50,50))
        diamante_uno = Recompensa(dict_diamante["idle"][0],(plataforma_uno.get_rectangulo().left + 10, plataforma_uno.get_rectangulo().top - 50), dict_diamante)
        diamante_dos = Recompensa(dict_diamante["idle"][0],(plataforma_uno.get_rectangulo().right - 60, plataforma_uno.get_rectangulo().top - 50), dict_diamante)
        diamante_tres = Recompensa(dict_diamante["idle"][0],(plataforma_dos.get_rectangulo().left + 10, plataforma_dos.get_rectangulo().top - 50), dict_diamante)
        diamante_cuatro = Recompensa(dict_diamante["idle"][0],(plataforma_dos.get_rectangulo().right - 60, plataforma_dos.get_rectangulo().top - 50), dict_diamante)

        lista_recompensas = [diamante_uno,diamante_dos,diamante_tres,diamante_cuatro]

        dict_pocion_salud = {}
        dict_pocion_salud["idle"] = cargar_imagenes_por_lista(pocion_salud, (50,50))
        pocion_uno = Recompensa(dict_pocion_salud["idle"][0],(plataforma_uno.get_rectangulo().centerx,plataforma_uno.get_rectangulo().top - 60),dict_pocion_salud)
        pocion_dos = Recompensa(dict_pocion_salud["idle"][0],(piso.get_rectangulo().right - 100,piso.get_rectangulo().top - 60),dict_pocion_salud)
        
        lista_pociones = [pocion_uno, pocion_dos]

        #6 - El personaje, en este caso jugador
        dict_per = cargar_listas_de_imagenes_jugador(TAMAÑO_PERSONAJE)
        personaje = Jugador(dict_per["quieto"][0],(100, piso.get_rectangulo().top - TAMAÑO_PERSONAJE[1]), dict_per)

        #7 - El enemigo
        dict_ene = {}
        dict_ene["caminar_izquierda"] = cargar_imagenes_por_lista(jefe_camina_izquierda,(120,150))
        dict_ene["caminar_derecha"] = girar_imagenes(dict_ene["caminar_izquierda"], True, False )
        dict_ene["ataque"] = cargar_imagenes_por_lista(jefe_ataque,(200,200))
        dict_ene["herido"] = cargar_imagenes_por_lista(jefe_herido,(200,200))
        jefe = Enemigo(dict_ene["caminar_derecha"][0], (piso.get_rectangulo().centerx,piso.get_rectangulo().top - 200), dict_ene)
        jefe.set_vida(300)

        lista_enemigos = [jefe]
        
        tiempo_duracion_segundos = 60
        tiempo_comienzo = pygame.time.get_ticks()
        tiempo_final = tiempo_comienzo + (tiempo_duracion_segundos * 1000)


        datos_jugador = {}
        with sqlite3.connect("juego_pygame.db") as conexion:
            try: 
                sentencia = '''
                            SELECT Nombre,Nivel_cuatro,Puntaje_actual,Permiso FROM Jugadores WHERE Id = 1
                            '''
                coleccion = conexion.execute(sentencia)
                for fila in coleccion:
                    datos_jugador["Nombre"] = fila[0]
                    datos_jugador["Puntaje_anterior"] = fila[1]
                    datos_jugador["Puntaje_actual"] = fila[2]
                    datos_jugador["Permiso"] = fila[3]
                print("Datos extraidos con exito") 
            except Exception as e:
                print(f"Error. No se pudo extraer los datos.\nRazon: {e}")

        super().__init__(pantalla, personaje, lista_plataformas, lista_plataformas_lados, lista_enemigos, lista_recompensas, lista_trampas, lista_pociones, lista_llaves, tiempo_final, datos_jugador, 5, fondo_escalado)