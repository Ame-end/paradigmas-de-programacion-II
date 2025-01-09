import pygame
import time

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
    def __init__(self, images, screen_width, screen_height):
        # Redimensiona las imágenes al tamaño de la pantalla
        self.images = [
            pygame.transform.scale(pygame.image.load(img).convert_alpha(), (screen_width, screen_height))
            for img in images
        ]
        self.screen_width = screen_width

    def draw(self, screen, scroll):
        for x in range(5):  # Repite 5 veces para cubrir la pantalla
            speed = 1
            for image in self.images:
                screen.blit(image, ((x * self.screen_width) - scroll * speed, 0))
                speed += 0.2

# Clase para manejar el suelo
class Ground:
    def __init__(self, image_path, screen_width, screen_height):
        # Redimensiona la imagen del suelo al ancho de la pantalla
        self.image = pygame.transform.scale(
            pygame.image.load(image_path).convert_alpha(),
            (screen_width, screen_height // 4)  # Ajusta el alto relativo al tamaño de la ventana
        )
        self.ground_width = self.image.get_width()
        self.ground_height = self.image.get_height()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen, scroll):
        for x in range(15):  # Repite para cubrir la pantalla con el suelo
            screen.blit(self.image, ((x * self.ground_width) - scroll * 2.5, self.screen_height - self.ground_height))

# Inicializa los objetos principales
background = Background([f"plx-{i}.png" for i in range(1, 6)], SCREEN_WIDTH, SCREEN_HEIGHT)
ground = Ground("ground.png", SCREEN_WIDTH, SCREEN_HEIGHT)

# Variables del juego
scroll = 0  # Desplazamiento inicial de la pantalla
clock = pygame.time.Clock()  # Reloj para controlar FPS
run = True  # Controla el bucle principal del juego

# Cargar la imagen 'trof.png' para mostrar después de 10 segundos de scroll
reveal_image = pygame.transform.scale(
    pygame.image.load("trof.png").convert_alpha(),
    (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 5)  # Redimensiona la imagen a un cuarto del tamaño de la pantalla
)
image_displayed = False  # Variable para controlar si la imagen ya ha sido mostrada
scroll_start_time = None  # Tiempo de inicio del scroll

# Bucle principal del juego
while run:
    clock.tick(FPS)  # Controla la velocidad de fotogramas

    # Dibuja el fondo y el suelo
    background.draw(screen, scroll)
    ground.draw(screen, scroll)

    # Maneja las teclas de movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and scroll < 3000:
        if scroll_start_time is None:  # Inicia el temporizador de scroll
            scroll_start_time = time.time()
        scroll += 5
    elif keys[pygame.K_LEFT] and scroll > 0:
        scroll -= 5

    # Verifica si han pasado 10 segundos de scroll
    if scroll_start_time and (time.time() - scroll_start_time >= 10):
        screen.blit(reveal_image, (SCREEN_WIDTH // 2 - reveal_image.get_width() // 2, SCREEN_HEIGHT // 2 - reveal_image.get_height() // 2))
        image_displayed = True  # Marca que la imagen ha sido mostrada

    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Actualiza la pantalla
    pygame.display.update()

# Finaliza pygame
pygame.quit()

