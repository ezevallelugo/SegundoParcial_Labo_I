import pygame
from clase_objeto_juego import Objeto

class Plataforma (Objeto):
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones: dict) -> None:
        super().__init__(imagen, posicion_inicial, acciones)
        self._es_visible = True

    def set_es_visible(self, visible):
        self._es_visible = visible

    def get_es_visible(self):
        return self._es_visible
    





