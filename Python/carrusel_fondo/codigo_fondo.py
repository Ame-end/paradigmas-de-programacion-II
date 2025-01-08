import pygame

# Inicializa todos los módulos de pygame
pygame.init()

# Configuración general
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 432
FPS = 60  # Límite de fotogramas por segundo

# Configuración de la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LapRun")

# Clase para manejar el fondo con efecto de paralaje
class Background:
    def __init__(self, images, screen_width):
        self.images = [pygame.image.load(img).convert_alpha() for img in images]
        self.bg_width = self.images[0].get_width()
        self.screen_width = screen_width

    def draw(self, screen, scroll):
        for x in range(5):  # Repite 5 veces para cubrir la pantalla
            speed = 1
            for image in self.images:
                screen.blit(image, ((x * self.bg_width) - scroll * speed, 0))
                speed += 0.2

# Clase para manejar el suelo
class Ground:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.ground_width = self.image.get_width()
        self.ground_height = self.image.get_height()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen, scroll):
        for x in range(15):  # Repite para cubrir la pantalla con el suelo
            screen.blit(self.image, ((x * self.ground_width) - scroll * 2.5, self.screen_height - self.ground_height))

# Inicializa los objetos principales
background = Background([f"plx-{i}.png" for i in range(1, 6)], SCREEN_WIDTH)
ground = Ground("ground.png", SCREEN_WIDTH, SCREEN_HEIGHT)

# Variables del juego
scroll = 0  # Desplazamiento inicial de la pantalla
clock = pygame.time.Clock()  # Reloj para controlar FPS
run = True  # Controla el bucle principal del juego

# Bucle principal del juego
while run:
    clock.tick(FPS)  # Controla la velocidad de fotogramas

    # Dibuja el fondo y el suelo
    background.draw(screen, scroll)
    ground.draw(screen, scroll)

    # Maneja las teclas de movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and scroll > 0:
        scroll -= 5
    if keys[pygame.K_RIGHT] and scroll < 3000:
        scroll += 5

    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Actualiza la pantalla
    pygame.display.update()

# Finaliza pygame
pygame.quit()
