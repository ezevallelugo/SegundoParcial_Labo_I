import pygame
from pygame.locals import *
from Gui.GUI_form import *
from Gui.GUI_button_image import *
from Gui.GUI_form_menu_music import *

class FormContenedorNivel (Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(),"")
        nivel._slave = self._slave
        self._nivel = nivel
        self.btn_home = Button_Image(screen=self._slave, master_x=self._x, master_y=self._y, x=self._w-100, y=50, w=50, h=50, onclick=self.btn_home_click, onclick_param="",path_image="RECURSOS/UI/Settings.png")
        self.btn_musica = Button_Image(screen=self._slave, master_x=self._x, master_y=self._y, x=self._w-100, y=150, w=50, h=50, onclick=self.btn_music_click, onclick_param="",path_image="RECURSOS/UI/Volume.png")

        self.lista_widgets.append(self.btn_home)
        self.lista_widgets.append(self.btn_musica)

    def btn_home_click(self, texto):
        pygame.mixer.music.stop()
        self.end_dialog()

    def btn_music_click(self, texto):
        form_menu_musica = FormMenuMusic(screen=self._master,x=self._master.get_width()/2-250, y=self._master.get_height()/2-250, w=500, h=500, color_background="White", path_image="RECURSOS/UI/papel2.png")
        self.show_dialog(form_menu_musica)

    def update(self, lista_eventos):
        self._nivel.update(lista_eventos)
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

