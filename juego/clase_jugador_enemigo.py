import pygame
import random
from clase_personaje import Personaje


pygame.mixer.init()
flecha_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_flecha.wav")
salto_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_salto.wav")
herido_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_herido.wav")
bola_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_bola.wav")
item_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_item.wav")
pocion_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_pocion.wav")
muerte_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_muerte.wav")
llave_sonido = pygame.mixer.Sound("RECURSOS/Sonidos/sonido_llave.wav")

class Enemigo (Personaje):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones: dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._orientacion = random.choice([True, False])
        self._vida = 30
        self._dano = 10

    def get_vida(self):
        return self._vida
    def set_vida(self, vida):
        self._vida = vida

    def get_dano(self):
        return self._dano
    def set_dano(self, dano):
        self._dano = dano

    def atacar(self):
        '''
        Ejecuta la accion de crear proyectiles en un intervalo de 2 segundos
        '''
        if not self._esta_en_el_aire:
            ahora = pygame.time.get_ticks()       
            if ahora - self._ultimo_disparo > 2000: 
                #self.animar_movimiento(self._diccionario_acciones["ataque"]) 
                self.crear_proyectil("RECURSOS/Enemigo/Ataque/bola.png",(50,50))
                self._ultimo_disparo = ahora

    def realizar_comportamiento(self,lista_plataformas_lados):
        '''
        Realiza el comportamiento autonomo del enemigo, limitandolo a caminar, cambiar de lado y disparar
        '''
        #Establecer limites de las plataformas que pisaron
        for plataforma in lista_plataformas_lados:
            if self._rectangulo_lados["bottom"].colliderect(plataforma["top"]):
                if self._rectangulo.right >= plataforma["main"].right:
                    self._orientacion = False
                elif self._rectangulo.left <= plataforma["main"].left:           
                    self._orientacion = True   
        #Cambios de orientacion 
        if not self._esta_en_el_aire:
            if self._colision_izquierda:
                self._orientacion = True
                self._colision_izquierda = False
            elif self._colision_derecha:
                self._orientacion = False
                self._colision_derecha = False

            if self._orientacion:
                self.animar_movimiento(self._diccionario_acciones["caminar_derecha"])
                self._velocidad_x = 2
            else:
                self.animar_movimiento(self._diccionario_acciones["caminar_izquierda"])
                self._velocidad_x = -2

    def update(self, screen):
        self.mover_en_ejex(self._velocidad_x)
        super().update(screen)


class Jugador (Personaje):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones:dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._puntaje = 0
        self._accion = None
        self._colision_enemigo = False
        self._salud = 100
        self._invencible = False
        self._invencible_duracion = 1000
        self._tiempo_colision_enemigo = 0
        self._saltos = 2

    def set_puntaje(self, puntaje):
        self._puntaje = puntaje
    def get_puntaje(self):
        return self._puntaje
    
    def set_accion(self, accion):
        self._accion = accion
    def get_accion(self):
        return self._accion
    
    def verificar_eventos_personaje(self):
        '''
        Verifica los eventos del jugador segun la tecla que haya pulsado, 
        cambiando el estado de la accion
        '''
        evento = pygame.key.get_pressed()
        if evento[pygame.K_LEFT]:
            self._accion = "Izquierda"
        elif evento[pygame.K_RIGHT]:
            self._accion = "Derecha"
        elif evento[pygame.K_UP] and not self._esta_en_el_aire:
            self._accion = "Saltando"
            self._esta_en_el_aire = True
        elif evento[pygame.K_SPACE]:
            self._accion = "Ataque"
        else:
            self._accion = "Quieto"
    
    def verificar_accion(self):
        '''
        Verifica la accion del jugador permitiendole moverse en el eje x o y, ademas 
        de disparar proyectiles y una animacion de herido y quieto
        '''
        match self._accion:
            case "Quieto":
                self._velocidad_x = 0
                if not self._esta_en_el_aire:
                    if self._orientacion:
                        self.animar_movimiento(self._diccionario_acciones["quieto"])
                    else:
                        self.animar_movimiento(self._diccionario_acciones["quieto_izq"])
                else:
                    if self._velocidad_y > 0 and self._orientacion:
                        self.animar_movimiento(self._diccionario_acciones["caida"]) 
                    elif self._velocidad_y > 0 and not self._orientacion:
                        self.animar_movimiento(self._diccionario_acciones["caida_izq"])
            case "Derecha":
                self._orientacion = True
                if not self._esta_en_el_aire:
                    self.animar_movimiento(self._diccionario_acciones["caminar_derecha"])
                self._velocidad_x = 10
            case "Izquierda":
                self._orientacion = False
                if not self._esta_en_el_aire:
                    self.animar_movimiento(self._diccionario_acciones["caminar_izquierda"])
                self._velocidad_x = -10
            case "Saltando":
                if self._orientacion:
                    self.animar_movimiento(self._diccionario_acciones["saltar"])
                else:
                    self.animar_movimiento(self._diccionario_acciones["saltar_izq"])
                self.saltar()
                salto_sonido.play()
            case "Ataque":
                ahora = pygame.time.get_ticks()                             
                if self._orientacion:
                    self.animar_movimiento(self._diccionario_acciones["ataque_suelo"])     
                else:
                    self.animar_movimiento(self._diccionario_acciones["ataque_suelo_izq"])
                if ahora - self._ultimo_disparo > self._cadencia_disparo: 
                    self.crear_proyectil("RECURSOS/Jugador/Flecha/0.png",(50,20)) 
                    flecha_sonido.play()
                    self._ultimo_disparo = ahora   
            case "Herido":
                self.animar_movimiento(self._diccionario_acciones["herido"])

    def realizar_invencibilidad(self):
        '''
        Se ejecuta un estado de invencibilidad en el que si el jugador resultase herido
        se le resta puntaje y salud, y empieza el conteo del tiempo exacto de colision
        '''
        if not self._invencible:
            if self._salud > 0:
                self._salud -= 10
            if self._puntaje > 0:
                self._puntaje -= 10
            self._invencible = True
            self._tiempo_colision_enemigo = pygame.time.get_ticks()
            herido_sonido.play()
            

    def verificar_colision_trampas(self,lista):
        '''
        Verifica la colision de cada trampa del nivel, en el que de ser el caso
        se realiza la invencibilidad
        '''
        for item in lista:
            if self._rectangulo.colliderect(item._rectangulo):
                self.realizar_invencibilidad() 

    def remover_de_la_lista(self,lista):
        '''
        Verifica que si el estado de colision de un objeto es True, 
        este se elimine de la lista
        '''
        i = 0
        while i < len(lista):
            if lista[i]._colision:
                lista.remove(lista[i])
                i -= 1
            i += 1

    def verificar_colision_recompensas(self,lista:list):
        '''
        Verifica que si el estado de colision de un objeto es True, 
        este se elimine de la lista. Ademas, otorga puntos extra
        '''
        for item in lista:
            if self._rectangulo.colliderect(item._rectangulo):
                self._puntaje += item._puntaje
                item._colision = True
                item_sonido.play()
        self.remover_de_la_lista(lista)

    def verificar_colision_pocion_salud(self,lista:list):
        '''
        Verifica que si el estado de colision de un objeto es True, 
        este se elimine de la lista. Ademas, otorga salud extra
        '''
        for item in lista:
            if self._rectangulo.colliderect(item._rectangulo):
                self._salud += item._salud_extra
                item._colision = True
                pocion_sonido.play()
        self.remover_de_la_lista(lista)

    def verificar_colision_llave(self, lista:list):
        '''
        Verifica que si el estado de colision de un objeto es True, 
        este se elimine de la lista.
        '''
        for item in lista:
            if self._rectangulo.colliderect(item._rectangulo):
                item._colision = True
                llave_sonido.play()
        self.remover_de_la_lista(lista)

    def verificar_colision_item(self, lista_items: list, tipo_item: str):
        '''
        Verifica la colision del item segun el tipo de items asignado como parametro
        '''
        match tipo_item:
            case "Trampa":
                self.verificar_colision_trampas(lista_items)
            case "Recompensa":
                self.verificar_colision_recompensas(lista_items)
            case "Salud":
                self.verificar_colision_pocion_salud(lista_items)
            case "Llave":
                self.verificar_colision_llave(lista_items)
            

    def verificar_colision_enemigo(self,lista_enemigos: list):
        '''
        Verifica la colision del jugador contra el enemigo donde se realizara
        una accion diferente segun la situacion. Si la vida del enemigo es 0,
        se elimina de la pantalla
        '''
        #Por cada enemigo
        for enemigo in lista_enemigos:
            if self._rectangulo.colliderect(enemigo._rectangulo):
                self.realizar_invencibilidad()
                self._accion = "Herido"
            #Por cada proyectil que el enemigo me impacta
            for proyectil in enemigo._lista_proyectiles:
                if proyectil._rectangulo.colliderect(self._rectangulo):
                    self.realizar_invencibilidad()
                self._accion = "Herido"
                proyectil.verificar_objetivo(self)
            #Por cada proyectil que impacto contra el enemigo, bajo la vida del enemigo
            for proyectil in self._lista_proyectiles:
                if proyectil._rectangulo.colliderect(enemigo._rectangulo):
                    enemigo._vida -= 10
                proyectil.verificar_objetivo(enemigo)

        i = 0
        while i < len(lista_enemigos):
            if lista_enemigos[i]._vida == 0:
                muerte_sonido.play()
                lista_enemigos.remove(lista_enemigos[i])
                self._puntaje += 10
                i -= 1
            i += 1

    def verificar_invencibilidad(self):
        '''
        Verifica que una vez que el jugador sea invencible, se calcula un lapso de tiempo
        para que el jugador se reubique desde el momento de la colision con el enemigo.
        Pasado el tiempo, el jugador vuelve a ser vulnerable
        '''
        if self._invencible:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self._tiempo_colision_enemigo >= self._invencible_duracion:
                self._invencible = False

    def update(self, screen):   
        if self._rectangulo.right > 1600:
            self._colision_derecha = True
        if self._rectangulo.left < 0:
            self._colision_izquierda = True
        self.verificar_invencibilidad()
        self.mover_en_ejex(self._velocidad_x)
        super().update(screen)



        
        
         
