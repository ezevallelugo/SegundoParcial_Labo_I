from pygame.locals import *
from clase_nivel_uno import NivelUno
from clase_nivel_dos import NivelDos
from clase_nivel_tres import NivelTres
from clase_nivel_cuatro import NivelCuatro
from clase_nivel_cinco import NivelCinco



class ManejadorNiveles:
    def __init__(self,pantalla) -> None:
        self._slave = pantalla
        self._niveles = {"nivel_uno": NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres, "nivel_cuatro": NivelCuatro, "nivel_cinco": NivelCinco}


    def get_nivel(self, nombre_nivel):
        return self._niveles[nombre_nivel](self._slave)