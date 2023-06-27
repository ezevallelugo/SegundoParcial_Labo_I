import pygame

pygame.init()

# Configurar la ventana
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Párrafo de texto en Pygame")

# Crear una fuente de texto
font = pygame.font.Font(None, 24)

# Texto para el párrafo
paragraph = "Esto es un ejemplo de un párrafo de 10 líneas en Pygame.\n"\
            "Cada línea representa una nueva línea de texto.\n"\
            "Puedes agregar más líneas si lo deseas.\n"\
            "Asegúrate de ajustar el tamaño de la ventana si es necesario.\n"\
            "El texto puede tener diferentes estilos, tamaños y colores.\n"\
            "Juega con las opciones para obtener el resultado deseado.\n"\
            "Pygame es una biblioteca poderosa para crear juegos y aplicaciones interactivas.\n"\
            "Explora sus capacidades y diviértete programando.\n"\
            "¡Buena suerte con tus proyectos en Pygame!\n"\
            "¡Espero que esto te sea útil!"

# Dividir el párrafo en líneas individuales
lines = paragraph.split("\n")

# Calcular el tamaño necesario para mostrar todas las líneas
line_height = font.get_linesize()
text_height = line_height * len(lines)

# Crear una superficie para el texto
text_surface = pygame.Surface((width, text_height))

# Dibujar cada línea de texto en la superficie
for i, line in enumerate(lines):
    text = font.render(line, True, (255, 255, 255))
    text_rect = text.get_rect(topleft=(0, i * line_height))
    text_surface.blit(text, text_rect)

# Calcular las coordenadas para centrar el texto en la ventana
text_rect = text_surface.get_rect(center=(width // 2, height // 2))

# Ejecutar el bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar el texto en la ventana
    window.fill((0, 0, 0))  # Limpiar la ventana
    window.blit(text_surface, text_rect)  # Dibujar el texto en la ventana

    pygame.display.update()

pygame.quit()
