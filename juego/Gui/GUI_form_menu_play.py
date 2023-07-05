import pygame
import sqlite3
from funciones_db import (extraer_permiso)
from pygame.locals import *
from Gui.GUI_button_image import *
from Gui.GUI_form import *
from Gui.GUI_form_contenedor_nivel import *
from clase_manejador_niveles import ManejadorNiveles

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, path_image):
        super().__init__(screen, x, y, w, h)
        self.manejador_niveles = ManejadorNiveles(self._master)
        imagen_aux = pygame.image.load(path_image)
        imagen_aux = pygame.transform.scale(imagen_aux, (w, h))
        self._slave = imagen_aux
        self.puntos = 0
        self.datos_jugador = {}

        extraer_permiso(self.datos_jugador)    

        self.btn_nivel_uno = Button_Image(screen=self._slave, x=100, y=100, master_x=x, master_y=y, w=60, h=80, onclick=self.verificar_permiso, onclick_param="nivel_uno",path_image="RECURSOS/UI/uno.png")
        self.btn_nivel_dos = Button_Image(screen=self._slave, x=100, y=200, master_x=x, master_y=y, w=60, h=80, onclick=self.verificar_permiso, onclick_param="nivel_dos",path_image="RECURSOS/UI/dos.png")
        self.btn_nivel_tres = Button_Image(screen=self._slave, x=200, y=100, master_x=x, master_y=y, w=60, h=80, onclick=self.verificar_permiso, onclick_param="nivel_tres",path_image="RECURSOS/UI/tres.png")
        self.btn_nivel_cuatro = Button_Image(screen=self._slave, x=200, y=200, master_x=x, master_y=y, w=60, h=80, onclick=self.verificar_permiso, onclick_param="nivel_cuatro",path_image="RECURSOS/UI/cuatro.png")
        self.btn_nivel_cinco = Button_Image(screen=self._slave, x=300, y=100, master_x=x, master_y=y, w=60, h=80, onclick=self.verificar_permiso, onclick_param="nivel_cinco",path_image="RECURSOS/UI/cinco.png")
        self.btn_home = Button_Image(screen=self._slave, x=400, y=400, master_x=x, master_y=y, w=50, h=50, onclick=self.btn_home_click, onclick_param="",path_image="RECURSOS/UI/Previous.png")

        self.lista_widgets.append(self.btn_nivel_uno)
        self.lista_widgets.append(self.btn_nivel_dos)
        self.lista_widgets.append(self.btn_nivel_tres)
        self.lista_widgets.append(self.btn_nivel_cuatro)
        self.lista_widgets.append(self.btn_nivel_cinco)
        self.lista_widgets.append(self.btn_home)

    def verificar_permiso(self, nivel_nombre):
        if self.datos_jugador["Permiso"] >= 1 and nivel_nombre == "nivel_uno":
            self.entrar_nivel(nivel_nombre)
        elif self.datos_jugador["Permiso"] >= 2 and nivel_nombre == "nivel_dos":
            self.entrar_nivel(nivel_nombre)
        elif self.datos_jugador["Permiso"] >= 3 and nivel_nombre == "nivel_tres":
            self.entrar_nivel(nivel_nombre)
        elif self.datos_jugador["Permiso"] >= 4 and nivel_nombre == "nivel_cuatro":
            self.entrar_nivel(nivel_nombre)
        elif self.datos_jugador["Permiso"] >= 5 and nivel_nombre == "nivel_cinco":
            self.entrar_nivel(nivel_nombre)

    def entrar_nivel(self,nivel_nombre):
        nivel = self.manejador_niveles.get_nivel(nivel_nombre)
        form_contenedor_nivel = FormContenedorNivel(self._master, nivel)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self, texto):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

        