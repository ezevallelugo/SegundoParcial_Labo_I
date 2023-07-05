import pygame
from funciones_db import (actualizar_game_over_db,actualizar_permiso)
from clase_jugador_enemigo import Jugador
from configuraciones import *


class Nivel:
    def __init__(self, pantalla: pygame.Surface, personaje: Jugador, lista_plataformas: list, lista_plataformas_lados: list, 
                 lista_enemigos: list, lista_recompensas: list, lista_trampas: list, lista_pociones: list, 
                 lista_llaves: list, tiempo, datos_jugador: dict, id_nivel: int, imagen_fondo) -> None:
        self._slave = pantalla
        self._jugador = personaje
        self._plataformas = lista_plataformas
        self._plataformas_lados = lista_plataformas_lados
        self._enemigos = lista_enemigos
        self._recompensas = lista_recompensas
        self._trampas = lista_trampas
        self._pociones = lista_pociones
        self._llaves = lista_llaves
        self._tiempo_final = tiempo
        self._imagen_fondo = imagen_fondo
        self._fuente = pygame.font.SysFont("Comic Sans",50)
        self._datos = datos_jugador
        self._id_nivel = id_nivel
        self._game_over = False
        self._nivel_completado = False
        self._puntos_acumulados = 0
        self._segundos_restantes = 0
        self._stop = False

    def actualizar_pantalla(self):
        '''
        Actualiza la pantalla con cada funcion llamada de cada objeto para ejecutar
        la mecanica del nivel que tendra el juego
        '''
        self._jugador.verificar_colision_plataforma(self._plataformas_lados)
        self._jugador.verificar_colision_proyectil_plataforma(self._plataformas_lados)
        self._jugador.verificar_colision_enemigo(self._enemigos)
        self._jugador.verificar_colision_item(self._recompensas,"Recompensa")
        self._jugador.verificar_colision_item(self._trampas,"Trampa")
        self._jugador.verificar_colision_item(self._pociones,"Salud")
        self._jugador.verificar_eventos_personaje() 
        self._jugador.verificar_accion()

        self._slave.blit(self._imagen_fondo,(0, 0))
        self._jugador.update(self._slave)
        for plataforma in self._plataformas: 
            plataforma.update(self._slave)
        for enemigo in self._enemigos:
            enemigo.verificar_colision_proyectil_plataforma(self._plataformas_lados)
            enemigo.verificar_colision_plataforma(self._plataformas_lados)
            enemigo.realizar_comportamiento(self._plataformas_lados)
            enemigo.atacar()
            enemigo.update(self._slave)
        for recompensa in self._recompensas:
            recompensa.animar_movimiento(recompensa.get_diccionario_acciones()["idle"])
            recompensa.update(self._slave)
        for trampa in self._trampas:
            trampa.animar_movimiento(trampa.get_diccionario_acciones()["idle"])
            trampa.update(self._slave)
        for pocion in self._pociones:
            pocion.animar_movimiento(pocion.get_diccionario_acciones()["idle"])
            pocion.update(self._slave)

        if len(self._enemigos) == 0:
            self._jugador.verificar_colision_item(self._llaves,"Llave")
            for llave in self._llaves:
                llave.animar_movimiento(llave.get_diccionario_acciones()["idle"])
            for llave in self._llaves:
                llave.update(self._slave)


        self._puntos_acumulados = self._jugador._puntaje + self._datos["Puntaje_anterior"]
        puntaje_acumulado = self._fuente.render("Puntaje acumulado: {0}".format(self._puntos_acumulados), True, BLANCO)
        puntaje_actual = self._fuente.render("Puntaje del nivel actual: {0}".format(self._jugador._puntaje), True, BLANCO)
        salud = self._fuente.render("Salud: {0}".format(self._jugador._salud), True, BLANCO)
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = max(0, self._tiempo_final - tiempo_actual)
        segundos_restantes = tiempo_restante // 1000
        tiempo = self._fuente.render("Tiempo: {0}".format(segundos_restantes), True, BLANCO) 
        if self._jugador._puntaje <= 0:
            self._jugador._puntaje = 0
        if segundos_restantes == 0 or self._jugador._salud <= 0:
            self._game_over = True
            segundos_restantes = 0   
        if len(self._llaves) == 0:
            self._nivel_completado = True
            self._segundos_restantes = segundos_restantes
        self._slave.blit(tiempo,(1100,0))
        self._slave.blit(puntaje_acumulado,(50,0))
        self._slave.blit(puntaje_actual,(50,50))
        self._slave.blit(salud,(ANCHO/2,0))            


    def dibujar_rectangulos(self):
        '''
        Perimte dibujar los rectangulos de los objetos cuando se ejecute el modo debug
        '''
        if get_mode():
            self._jugador.draw(ROJO,self._slave) 
            for plataforma in self._plataformas:
                plataforma.draw(AZUL,self._slave)
            for enemigo in self._enemigos:
                enemigo.draw(AZUL_CLARO,self._slave)
            for recompensa in self._recompensas:
                recompensa.draw(BLANCO,self._slave)
            for llave in self._llaves:
                llave.draw(AZUL_CLARO,self._slave)
            for trampa in self._trampas:
                trampa.draw(AZUL_CLARO,self._slave)
            for pocion in self._pociones:
                pocion.draw(VERDE,self._slave)

    def actualizar_datos_game_over(self):
        if self._id_nivel == 1:
            nivel = "Nivel_uno"
            actualizar_game_over_db(nivel,self._datos["Puntaje_actual"])
        elif self._id_nivel == 2:
            nivel = "Nivel_dos"
            actualizar_game_over_db(nivel,self._datos["Puntaje_actual"]) 
        elif self._id_nivel == 3:
            nivel = "Nivel_tres"
            actualizar_game_over_db(nivel,self._datos["Puntaje_actual"])
        elif self._id_nivel == 4:
            nivel = "Nivel_cuatro"
            actualizar_game_over_db(nivel,self._datos["Puntaje_actual"])   
        elif self._id_nivel == 5:
            nivel = "Nivel_cinco"
            actualizar_game_over_db(nivel,self._datos["Puntaje_actual"])

    def verificar_game_over(self):
        '''
        Si el juego termina con un game over, se muestra el puntaje total
        '''
        if self._game_over:
            self._datos["Puntaje_actual"] = self._jugador._puntaje * 100
            cartel = self._fuente.render("GAME OVER", True, BLANCO)
            puntaje = self._fuente.render("Puntaje * 100: {0}".format(self._datos["Puntaje_actual"]), True, BLANCO)
            self.actualizar_datos_game_over()
            self._slave.blit(cartel, (ANCHO/2-250, LARGO/2-150))
            self._slave.blit(puntaje, (ANCHO/2-250, LARGO/2-50))
            self._game_over = False
            self._stop = True

    def actualizar_datos_nivel_completado(self):
        if self._id_nivel == 1:
            permiso = self.verificar_permiso(self._id_nivel)
            nivel = "Nivel_uno"
            actualizar_permiso(nivel,self._datos["Puntaje_actual"],permiso)
        elif self._id_nivel == 2:
            permiso = self.verificar_permiso(self._id_nivel)
            nivel = "Nivel_dos"
            actualizar_permiso(nivel,self._datos["Puntaje_actual"],permiso) 
        elif self._id_nivel == 3:
            permiso = self.verificar_permiso(self._id_nivel)
            nivel = "Nivel_tres"
            actualizar_permiso(nivel,self._datos["Puntaje_actual"],permiso)
        elif self._id_nivel == 4:
            permiso = self.verificar_permiso(self._id_nivel)
            nivel = "Nivel_cuatro"
            actualizar_permiso(nivel,self._datos["Puntaje_actual"],permiso)   
        elif self._id_nivel == 5:
            permiso = self.verificar_permiso(self._id_nivel)
            nivel = "Nivel_cinco"
            actualizar_permiso(nivel,self._datos["Puntaje_actual"],permiso)


    def verificar_nivel_completado(self):
        '''
        Si el nivel se completa con exito, se muestra el puntaje total mas 
        un extra por tiempo restante.
        '''
        if self._nivel_completado:
            puntaje_por_cien = self._jugador._puntaje * 100
            puntaje_por_tiempo_restante = self._jugador._puntaje * self._segundos_restantes
            self._datos["Puntaje_actual"] = puntaje_por_cien + puntaje_por_tiempo_restante + self._datos["Puntaje_anterior"]
            cartel = self._fuente.render("NIVEL COMPLETADO", True, BLANCO)
            puntaje_uno = self._fuente.render("Puntaje * 100: {0}".format(puntaje_por_cien), True, BLANCO)
            puntaje_dos = self._fuente.render("Puntaje por segundos restantes: {0}".format(puntaje_por_tiempo_restante), True, BLANCO)
            puntaje_total = self._fuente.render("Puntaje final: {0}".format(self._datos["Puntaje_actual"]), True, BLANCO)
            self.actualizar_datos_nivel_completado()
            self._slave.blit(cartel, (ANCHO/2-250, LARGO/2-150))
            self._slave.blit(puntaje_uno, (ANCHO/2-250, LARGO/2-50))
            self._slave.blit(puntaje_dos, (ANCHO/2-250, LARGO/2+50))
            self._slave.blit(puntaje_total, (ANCHO/2-250, LARGO/2+150))
            self._nivel_completado = False
            self._stop = True
        
    def verificar_permiso(self,id_nivel):
        if self._datos["Permiso"] > id_nivel:
            retorno = self._datos["Permiso"]
        elif self._datos["Permiso"] == id_nivel:
            retorno = id_nivel + 1
        return retorno

    def update(self, lista_eventos):
        for evento in lista_eventos: 
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()     
        if not self._stop:
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
        self.verificar_game_over()
        self.verificar_nivel_completado()



