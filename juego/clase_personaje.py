import pygame
from clase_objeto_juego import Objeto
from clase_item import Item
from clase_proyectil import Proyectil


class Personaje (Objeto):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones:dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._velocidad_x = 0
        self._velocidad_y = 0
        self._esta_en_el_aire = False
        self._orientacion = True
        self._colision_derecha = False
        self._colision_izquierda = False
        self._colision_cabeza = False
        self._esta_disparando = False
        self._lista_proyectiles = []
        self._cadencia_disparo = 200
        self._ultimo_disparo = pygame.time.get_ticks()

    def set_velocidad(self, velocidad):
        self._velocidad_x = velocidad
    def get_velocidad(self):
        return self._velocidad_x
    
    def set_velocidad(self, velocidad):
        self._velocidad_y = velocidad
    def get_velocidad(self):
        return self._velocidad_y

    def set_esta_en_el_aire(self, salto):
        self._esta_en_el_aire = salto
    def get_esta_en_el_aire(self):
        return self._esta_en_el_aire
    
    def caer_gravedad(self):
        '''
        Crea el efecto de estar cayendo con una gravedad simulada
        '''
        if self._esta_en_el_aire:
            if self._velocidad_y < 15:
                self._velocidad_y += 0.5 #Gravedad           
            for lado in self._rectangulo_lados:
                self._rectangulo_lados[lado].y += self._velocidad_y    

    def saltar(self):
        self._velocidad_y = -15

    def verificar_colision_plataforma(self, lista_plataformas:list):
        '''
        Verifica cada colision que hace con cualquier plataforma segun la ubicacion del personaje,
        si llega a estar en el piso se mantiene en el, si colisiona con la derecha o izquierda, se levanta
        una bandera, y si la cabeza colisiona con la base el impulso del salto se detiene con velocidad 0
        '''
        self.caer_gravedad()
        self._esta_en_el_aire = True
        self._colision_derecha = False
        self._colision_izquierda = False
        self._colision_cabeza = False
        for plataforma in lista_plataformas:
            #Colision con el piso
            if self._rectangulo_lados["bottom"].colliderect(plataforma["top"]):
                self._esta_en_el_aire = False
                self._velocidad_y = 0
                self._rectangulo_lados["main"].bottom = plataforma["main"].top + 1
                self._rectangulo_lados["left"].bottom = self._rectangulo_lados["main"].bottom
                self._rectangulo_lados["right"].bottom = self._rectangulo_lados["main"].bottom
                self._rectangulo_lados["bottom"].bottom = self._rectangulo_lados["main"].bottom
                self._rectangulo_lados["top"].top = self._rectangulo_lados["main"].top
            #Colision con la derecha
            elif self._rectangulo_lados["right"].colliderect(plataforma["left"]):
                self._colision_derecha = True
            #Colision con la izquierda
            elif self._rectangulo_lados["left"].colliderect(plataforma["right"]):
                self._colision_izquierda = True
            #Colision con la base
            elif self._rectangulo_lados["top"].colliderect(plataforma["bottom"]):
                self._colision_cabeza = True
                self._velocidad_y = 0

    def crear_proyectil(self, ruta_imagen, escala):
        '''
        Se crea un proyectil y se agrega a la lista de proyectiles segun la 
        orientacion del personaje
        '''

        superficie = pygame.transform.scale(pygame.image.load(ruta_imagen),escala)
        if self._orientacion:
            proyectil = Proyectil(superficie, (self._rectangulo.right,self._rectangulo.centery - 10), None)
            proyectil._velocidad = 10
        else:
            superficie = pygame.transform.flip(superficie, True, False)
            proyectil = Proyectil(superficie, (self._rectangulo.left,self._rectangulo.centery - 10), None)
            proyectil._velocidad = -10
        self._lista_proyectiles.append(proyectil)

    def verificar_colision_proyectil_plataforma(self, lista_plataformas: list):
        '''
        Verifica que cada proyectil, si es que colisiona contra un objeto,
        la bandera colision se levante
        '''
        for proyectil in self._lista_proyectiles:
            for plataforma in lista_plataformas:
                if proyectil._rectangulo.colliderect(plataforma["main"]):
                    proyectil._colision = True

    def actualizar_y_eliminar_proyectiles(self, screen):
        '''
        Verifica que cada proyectil de la lista de proyectiles tenga la bandera 
        de colision levantada para eliminarlo de la pantalla
        '''
        i = 0
        while i < len(self._lista_proyectiles):
            self._lista_proyectiles[i].update(screen)
            if self._lista_proyectiles[i]._colision:
                self._lista_proyectiles.remove(self._lista_proyectiles[i])
                i -= 1
            i += 1

    def mover_en_ejex(self, velocidad):  
        '''
        Permite la movilidad en el eje x segun la velocidad y si el personaje 
        colisiona con el lado derecho o izquierdo, evitando pasarlo de lado
        '''      
        if velocidad > 0 and not self._colision_derecha:
            super().mover_en_ejex(velocidad)
        elif velocidad < 0 and not self._colision_izquierda: 
            super().mover_en_ejex(velocidad)
        elif velocidad == 0:
            super().mover_en_ejex(velocidad)


    def update(self, screen):
        self.actualizar_y_eliminar_proyectiles(screen)                
        super().update(screen)


        