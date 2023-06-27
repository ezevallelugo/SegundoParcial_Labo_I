import pygame
from clase_objeto_juego import Objeto

class Item (Objeto):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones: dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._colision = False



