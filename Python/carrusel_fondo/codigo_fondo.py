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

# Configuración de la música de fondo
pygame.mixer.init()
pygame.mixer.music.load("musica.mp3")  # Reemplaza con la ruta de tu archivo de música
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Clase para manejar el personaje con animaciones
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, sprite_size):
        super().__init__()
        self.scale = scale
        self.sprite_size = sprite_size  # Tamaño de los sprites (ancho, alto)
        self.center_x = x
        self.center_y = y

        # Texturas para animación (9 sprites para cada dirección)
        self.stand_right_textures = [
            pygame.transform.scale(
                pygame.image.load("sp1.png").convert_alpha(), self.sprite_size
            )
        ]
        self.stand_left_textures = [
            pygame.transform.flip(self.stand_right_textures[0], True, False)
        ]

        self.walk_right_textures = [
            pygame.transform.scale(
                pygame.image.load(f"sp{i}.png").convert_alpha(), self.sprite_size
            )
            for i in range(1, 10)
        ]
        self.walk_left_textures = [
            pygame.transform.flip(img, True, False) for img in self.walk_right_textures
        ]

        # Animación de salto (usar solo salt5.png)
        self.jump_right_textures = [
            pygame.transform.scale(
                pygame.image.load("salt5.png").convert_alpha(), self.sprite_size
            )
        ]
        self.jump_left_textures = [
            pygame.transform.flip(self.jump_right_textures[0], True, False)
        ]

        # Imagen estática cuando no se mueve
        self.standing_image = pygame.transform.scale(
            pygame.image.load("estatica.png").convert_alpha(), self.sprite_size
        )

        # Variables para manejar animaciones
        self.current_texture = 0
        self.image = self.walk_right_textures[0]  # Imagen inicial
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        self.direction = "right"
        self.animating = False
        self.is_jumping = False  # Si está saltando
        self.jump_height = 0  # Altura del salto
        self.jump_frame = 0  # Control de la animación del salto

    def update(self):
        # Actualiza la animación según la dirección y si está en movimiento
        if self.is_jumping:
            # Si está saltando, solo mostramos el primer sprite de la animación
            if self.direction == "right":
                self.image = self.jump_right_textures[0]  # Solo muestra el sprite salt5.png
            else:
                self.image = self.jump_left_textures[0]
        elif self.animating:
            self.current_texture += 1
            if self.current_texture >= len(self.walk_right_textures):
                self.current_texture = 0
            if self.direction == "right":
                self.image = self.walk_right_textures[self.current_texture]
            else:
                self.image = self.walk_left_textures[self.current_texture]
        else:  # Si está parado y no presionan teclas
            self.image = self.standing_image  # Muestra la imagen estática

    def move(self, keys):
        self.animating = False  # Por def ecto no se mueve
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
            self.direction = "right"
            self.animating = True
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 1
            self.direction = "left"
            self.animating = True

        # Lógica para saltar
        if keys[pygame.K_SPACE] and not self.is_jumping:  # Solo puede saltar si no está saltando
            self.is_jumping = True
            self.jump_height = 20  # Altura inicial del salto
            self.animating = False  # Detener la animación de caminar

    def update_jump(self):
        if self.is_jumping:
            self.rect.y -= self.jump_height  # Mueve al jugador hacia arriba
            self.jump_height -= 1  # La velocidad del salto disminuye con el tiempo

            if self.jump_height < -20:  # Cuando el jugador comienza a bajar
                self.is_jumping = False  # Termina el salto
                self.rect.y = SCREEN_HEIGHT - 100  # Vuelve al suelo

        # Evitar que el jugador se salga de la ventana
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Garantizar que el personaje no se mueva más allá del suelo
        if self.rect.bottom > SCREEN_HEIGHT - 50:
            self.rect.bottom = SCREEN_HEIGHT - 50

# Clase para manejar el fondo
class Background:
    def __init__(self, images, screen_width):
        self.images = [pygame.image.load(img).convert_alpha() for img in images]
        self.bg_width = self.images[0].get_width()
        self.screen_width = screen_width

    def draw(self, screen, scroll):
        for x in range(-1, 5):  # Ajusta para que el fondo se repita correctamente
            for idx, image in enumerate(self.images):
                speed = 1 + idx * 0.2  # Velocidad de cada capa
                screen.blit(image, ((x * self.bg_width) - (scroll * speed), 0))


# Clase para manejar el suelo
class Ground:
    def __init__(self, image_path, screen_width, screen_height):
        # Escala la imagen al tamaño completo de la ventana
        self.image = pygame.transform.scale(
            pygame.image.load(image_path).convert_alpha(),
            (screen_width, screen_height)  # Ajuste completo al tamaño de la ventana
        )
        self.ground_width = self.image.get_width()
        self.ground_height = self.image.get_height()
        self.screen_height = screen_height

    def draw(self, screen, scroll):
        # Dibuja el suelo en la pantalla desplazándose con el scroll
        for x in range(-1, 15):
            screen.blit(self.image, ((x * self.ground_width) - scroll * 2.5, self.screen_height - self.ground_height))


# Inicialización del juego
background = Background([f"plx-{i}.png" for i in range(1, 6)], SCREEN_WIDTH)
ground = Ground("ground.png", SCREEN_WIDTH, SCREEN_HEIGHT)
sprite_size = (128, 128)  # Tamaño aumentado de los sprites (más grande)
player = Player(100, SCREEN_HEIGHT - 100, 1.0, sprite_size)  # Instancia del jugador con nueva posición X
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

scroll = 0
clock = pygame.time.Clock()
run = True

# Bucle principal del juego
while run:
    clock.tick(FPS)

    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Entrada del teclado
    keys = pygame.key.get_pressed()

    # Actualización de objetos
    player.move(keys)
    player.update_jump()  # Actualiza el salto
    all_sprites.update()

    # Incrementa o disminuye el scroll para mover el fondo
    if keys[pygame.K_RIGHT]:
        scroll += 5
    elif keys[pygame.K_LEFT] and scroll > 0:
        scroll -= 5

    # Dibuja todo
    screen.fill((0, 0, 0))  # Fondo negro
    background.draw(screen, scroll)
    ground.draw(screen, scroll)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()


