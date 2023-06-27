import pygame
from clase_item import Item

class Trampa (Item):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones: dict = None) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._daño = 10

    def nivel_daño(self):
        pass