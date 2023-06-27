import pygame
from pygame.locals import *
from Gui.GUI_button import *
from Gui.GUI_button_image import *
from Gui.GUI_form import *
from Gui.GUI_label import *
from Gui.GUI_slider import *
from Gui.GUI_textbox import *
from Gui.GUI_form_menu_score import *
from Gui.GUI_form_menu_play import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        imagen_aux = pygame.image.load(path_image)
        imagen_aux = pygame.transform.scale(imagen_aux, (w, h))
        fondo_aux= pygame.image.load("RECURSOS/UI/menu_fondo.jpg")
        self._fondo_menu = pygame.transform.scale(fondo_aux,(1600,900))
        self._slave = imagen_aux
        self.volumen = 0.2
        self.flag_play = True

        #Controles
        self.txtbox = TextBox(self._slave, x, y, w/2-90, 200, 150, 30, "Gray", "White", "Black", "Blue", 2, "Arial", 15, "Black")
        self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "RECURSOS/UI/Leaderboard.png", self.btn_tabla_click, "la")
        self.btn_jugar = Button_Image(self._slave, x, y, 455, 100, 50, 50, "RECURSOS/UI/Levels.png", self.btn_jugar_click, "la")

        #Agrego los controles
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)

    def btn_tabla_click(self, texto):
        dict_score = [{"Jugador": "Uno", "Score": 1000},
                      {"Jugador": "Dos", "Score": 5000},
                      {"Jugador": "Tres", "Score": 2000}]

        form_puntaje = FormMenuScore(self._master, self._master.get_width()/2-250, self._master.get_height()/2-250, 500, 600, "White", "Cyan", True, "API FORMS/Window.png", dict_score, 100, 10, 10)
        self.show_dialog(form_puntaje)

    def btn_jugar_click(self, texto):
        form_jugar = FormMenuPlay(screen=self._master, x=self._master.get_width()/2-250, y=self._master.get_height()/2-250, w =500, h=500, color_background=(220, 0, 220), color_border=(0,0,0), active=True, path_image="RECURSOS/UI/tabla1.png")
        self.show_dialog(form_jugar)
    
    def update(self, lista_eventos):
        self._master.blit(self._fondo_menu,(0,0))
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                #self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
