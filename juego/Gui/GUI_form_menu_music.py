import pygame
from pygame.locals import *
from Gui.GUI_form import *
from Gui.GUI_label import *
from Gui.GUI_slider import *
from Gui.GUI_button import *
from Gui.GUI_button_image import *

class FormMenuMusic(Form):
    def __init__(self, screen, x, y, w, h, color_background, path_image):
        super().__init__(screen, x, y, w, h, color_background)
        imagen_aux = pygame.image.load(path_image)
        imagen_aux = pygame.transform.scale(imagen_aux, (w, h))
        self._slave = imagen_aux
        if pygame.mixer.music.get_busy():
            self._estado = "Reproduciendo"
            self.btn_play = Button(self._slave, x, y, 100, 70, 200, 50, "Green", "Blue", self.btn_play_click, "Nombre", self._estado, "Comic Sans", 25, "Black")
            self.flag_play = True
        else:
            self._estado = "Stop"
            self.btn_play = Button(self._slave, x, y, 100, 70, 200, 50, "Red", "Blue", self.btn_play_click, "Nombre", self._estado, "Comic Sans", 25, "Black")
            self.flag_play = False
        self.volumen = pygame.mixer.music.get_volume()
        
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 300, 10, self.volumen, "Orange", "White")
        self.label_volumen = Label(self._slave, 100, 300, 100, 100, "0%", "Comic Sans", 25, "Black", "RECURSOS/UI/papel1.png")
        self.btn_return = Button_Image(screen=self._slave, x=360, y=360, master_x=x, master_y=y, w=50, h=50, onclick=self.btn_home_click, onclick_param="",path_image="RECURSOS/UI/Back.png")

        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_return)

    def btn_home_click(self, texto):
        self.end_dialog()

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Red"
            self._estado = "Stop"
            self.btn_play.set_text(self._estado)
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Green"
            self._estado = "Reproduciendo"
            self.btn_play.set_text(self._estado)

        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

