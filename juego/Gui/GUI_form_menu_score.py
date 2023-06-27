import pygame
from pygame.locals import *
from Gui.GUI_form import *
from Gui.GUI_label import *
from Gui.GUI_button_image import *

class FormMenuScore (Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, score, margen_y, margen_x, espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)        

        imagen_auxiliar = pygame.image.load(path_image)
        imagen_auxiliar = pygame.transform.scale(imagen_auxiliar, (w,h))
        self._slave = imagen_auxiliar
        self._score = score
        self._margen_y = margen_y

        label_jugador = Label(self._slave, x=margen_x+10, y=20, w=w/2-margen_x-10, h=50, text="Jugador", font="Arial", font_size=30, font_color="White", path_image="API FORMS/bar.png")
        label_puntaje = Label(self._slave, x=margen_x+10 + w/2-margen_x-10, y=20, w=w/2-margen_x-10, h=50, text="Puntaje", font="Arial", font_size=30, font_color="White", path_image="API FORMS/bar.png")

        self.lista_widgets.append(label_jugador)
        self.lista_widgets.append(label_puntaje)

        posicion_inicial_y = margen_y

        for i in self._score:
            posicion_inicial_x = margen_x
            for n,s in i.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, posicion_inicial_x, posicion_inicial_y, w/2-margen_x, 100, cadena, "Arial", 30, "Black", "API FORMS/Table.png")
                self.lista_widgets.append(jugador)
                posicion_inicial_x += (w/2-margen_x)
            posicion_inicial_y += 100 + espacio
        self._boton_home = Button_Image(self._slave, x=w-70, y=h-70, master_x=x, master_y=y, w=50, h=50, color_background= (255,0,0), color_border=(255,0,255), onclick=self.btn_home_click, onclick_param="", text="", font="Arial", font_size=15, font_color=(0,255,0), path_image="RECURSOS/UI/Settings.png")
        self.lista_widgets.append(self._boton_home)

    def btn_home_click(self, texto):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()

