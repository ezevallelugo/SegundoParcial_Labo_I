import pygame

class Objeto:
    def __init__(self, imagen: pygame.Surface, posicion_inicial: tuple, acciones:dict) -> None:
        self._superficie = imagen
        self._rectangulo = self._superficie.get_rect()  
        self._rectangulo.x = posicion_inicial[0]
        self._rectangulo.y = posicion_inicial[1]
        self._rectangulo_lados = self.obtener_rectangulos(self._rectangulo)
        self._diccionario_acciones = acciones
        self._contador_pasos = 0
        self._actualizacion = pygame.time.get_ticks()

    def set_superficie(self, superficie):
        self._superficie = superficie
    def get_superficie(self):
        return self._superficie
    
    def set_rectangulo(self, rectangulo):
        self._rectangulo = rectangulo
    def get_rectangulo(self):
        return self._rectangulo
    
    def set_rectangulo_lados(self, nuevo_diccionario):
        self._rectangulo_lados = nuevo_diccionario
    def get_rectangulo_lados(self):
        return self._rectangulo_lados
    
    def set_diccionario_acciones(self, diccionario):
        self._diccionario_acciones = diccionario
    def get_diccionario_acciones(self):
        return self._diccionario_acciones

    def mover_en_ejex(self, velocidad):
        '''
        Permite la movilidad del objeto en el eje x segun la velocidad asignada
        '''
        for lado in self._rectangulo_lados:
            self._rectangulo_lados[lado].x += velocidad

    def animar_movimiento(self, lista_imagenes):
        '''
        Realiza una impresion de cada imagen creando una animacion segun el movimiento indicado
        del diccionario de acciones 
        '''
        largo = len(lista_imagenes)
        if self._contador_pasos >= largo:
            self._contador_pasos = 0
        self._superficie = lista_imagenes[self._contador_pasos]
        self._contador_pasos += 1            

    def draw(self,color,screen):
        '''
        Dibuja el rectnagulo principal y los lados del objeto en la pantalla
        '''
        pygame.draw.rect(screen,color,self._rectangulo,4)
        for i in self._rectangulo_lados:
            pygame.draw.rect(screen, (255,255,255), self._rectangulo_lados[i],1)

    def update(self, screen):
        screen.blit(self._superficie, self._rectangulo)
        
    def obtener_rectangulos(self, principal: pygame.Rect):
        '''
        Obtiene los rectangulos en forma de lados de cada objeto y los guarda en un diccionario
        '''
        diccionario = {}
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
        diccionario["right"] = pygame.Rect(principal.right - 10, principal.top, 10, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
        return diccionario

