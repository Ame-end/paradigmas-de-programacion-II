import pygame

# Inicializa todos los módulos de pygame
pygame.init()

# Configura el reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()
FPS = 60  # Establece el límite de fotogramas por segundo

# Crea la ventana del juego
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 432
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Establece el tamaño de la ventana
pygame.display.set_caption("LapRun")  # Título de la ventana

# Define el desplazamiento incial de la pantalla
scroll = 0

# Carga la imagen del suelo y obtiene sus dimensiones
ground_image = pygame.image.load("ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

# Carga las imágenes de fondo para el efecto de paralaje
bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()  # Obtiene el ancho de las imágenes de fondo

# Función para dibujar el fondo con efecto de paralaje
def draw_bg():
    for x in range(5):  # Repite 5 veces para llenar la pantalla
        speed = 1  # Velocidad inicial para el paralaje
        for i in bg_images:  # Itera sobre cada imagen de fondo
            screen.blit(i, ((x * bg_width) - scroll * speed, 0))
            speed += 0.2  # Incrementa la velocidad para cada capa de fondo

# Función para dibujar el suelo
def draw_ground():
    for x in range(15):  # Repite 15 veces para llenar la pantalla con el suelo
        screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))

# Bucle principal del juego
run = True
while run:
    clock.tick(FPS)  # Controla la velocidad de fotogramas

    # Dibuja el mundo del juego
    draw_bg()
    draw_ground()

    # Obtiene las teclas presionadas
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:  # Mueve la pantalla hacia la izquierda si se presiona la tecla y no está en el límite
        scroll -= 5
    if key[pygame.K_RIGHT] and scroll < 3000:  # Mueve la pantalla hacia la derecha si se presiona la tecla y no está en el límite
        scroll += 5

    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Cierra el juego si se presiona la cruz de la ventana
            run = False

    pygame.display.update()  # Actualiza la pantalla

# Finaliza pygame
pygame.quit()
