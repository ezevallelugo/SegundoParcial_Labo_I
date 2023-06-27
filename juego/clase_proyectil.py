import pygame
from clase_item import Item


class Proyectil (Item):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones: dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._velocidad = 0

    def verificar_objetivo(self, personaje):
        if self._rectangulo.colliderect(personaje._rectangulo):
            self._colision = True
            print("impacto")

    def update(self, screen):
        self._rectangulo.x += self._velocidad
        if self._rectangulo.x > 1550 or self._rectangulo.x < 0:
            self._colision = True
        super().update(screen)