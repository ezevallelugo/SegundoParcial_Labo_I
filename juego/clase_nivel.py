import pygame
from configuraciones import *


class Nivel:
    def __init__(self, pantalla, personaje, lista_plataformas, lista_plataformas_lados, lista_enemigos, lista_recompensas, lista_trampas, lista_pociones, lista_llaves, tiempo, audio_historia, imagen_fondo) -> None:
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
        self._historia = audio_historia
        self._game_over = False
        self._stop = False

    def actualizar_pantalla(self):
        self._jugador.verificar_colision_plataforma(self._plataformas_lados)
        self._jugador.verificar_colision_proyectil_plataforma(self._plataformas_lados)
        self._jugador.verificar_colision_enemigo(self._enemigos)
        self._jugador.verificar_colision_item(self._recompensas,"Recompensa")
        self._jugador.verificar_colision_item(self._trampas,"Trampa")
        self._jugador.verificar_colision_item(self._pociones,"Salud")
        self._jugador.verificar_colision_item(self._llaves,"Llave")

        for llave in self._llaves:
            llave.animar_movimiento(llave.get_diccionario_acciones()["idle"])
        for trampa in self._trampas:
            trampa.animar_movimiento(trampa.get_diccionario_acciones()["idle"])
        for recompensa in self._recompensas:
            recompensa.animar_movimiento(recompensa.get_diccionario_acciones()["idle"])
        for pocion in self._pociones:
            pocion.animar_movimiento(pocion.get_diccionario_acciones()["idle"])
        self._jugador.verificar_eventos_personaje() 
        self._jugador.verificar_accion()
        for enemigo in self._enemigos:    
            enemigo.verificar_colision_proyectil_plataforma(self._plataformas_lados)
            enemigo.verificar_colision_plataforma(self._plataformas_lados)
            enemigo.realizar_comportamiento(self._plataformas_lados)
            enemigo.atacar()


        self._slave.blit(self._imagen_fondo,(0, 0))
        self._jugador.update(self._slave)
        for plataforma in self._plataformas: 
            plataforma.update(self._slave)
        for enemigo in self._enemigos:
            enemigo.update(self._slave)
        for recompensa in self._recompensas:
            recompensa.update(self._slave)
        for llave in self._llaves:
            llave.update(self._slave)
        for trampa in self._trampas:
            trampa.update(self._slave)
        for pocion in self._pociones:
            pocion.update(self._slave)

        puntaje = self._fuente.render("Puntaje: {0}".format(self._jugador._puntaje), True, BLANCO)
        salud = self._fuente.render("Salud: {0}".format(self._jugador._salud), True, BLANCO)
        tiempo_actual = pygame.time.get_ticks()
        tiempo_restante = max(0, self._tiempo_final - tiempo_actual)
        segundos_restantes = tiempo_restante // 1000
        tiempo = self._fuente.render("Tiempo: {0}".format(segundos_restantes), True, BLANCO) 
        if self._jugador._puntaje <= 0:
            self._jugador._puntaje = 0
        if segundos_restantes == 0 or self._jugador._salud <= 0 or len(self._llaves) == 0:
            self._game_over = True
            segundos_restantes = 0   
        self._slave.blit(tiempo,(1100,0))
        self._slave.blit(puntaje,(50,0))
        self._slave.blit(salud,(ANCHO/2-200,0))            


    def dibujar_rectangulos(self):
        if get_mode(): 
            for plataforma in self._plataformas:
                plataforma.draw(AZUL,self._slave)
            self._jugador.draw(ROJO,self._slave)
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

    def verificar_game_over(self):
        if self._game_over:
            if len(self._llaves) == 0:
                pygame.mixer.music.load(self._historia)
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play()
            puntaje_final = self._jugador._puntaje * 100
            game_over_cartel = self._fuente.render("GAME OVER", True, BLANCO)
            puntaje = self._fuente.render("Puntaje final: {0}".format(puntaje_final), True, BLANCO)
            self._slave.blit(game_over_cartel, (ANCHO/2-200, LARGO/2-350))
            self._slave.blit(puntaje, (ANCHO/2-250, LARGO/2-250))
            self._game_over = False
            self._stop = True

    def update(self, lista_eventos):
        for evento in lista_eventos: 
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()     
        if not self._stop:
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
        self.verificar_game_over()



