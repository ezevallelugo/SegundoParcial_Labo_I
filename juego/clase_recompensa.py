import pygame
from clase_item import Item

class Recompensa (Item):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones: dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._puntaje = 10
        self._salud_extra = 10
    