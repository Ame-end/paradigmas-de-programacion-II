import pygame


# Clase para manipular al alumno
class Alumno:
    # Constructor-screen es lo que recibe
    def __init__(self, screen, esc_alumnos_config):
        self.screen = screen
        self.esc_alumnos_config = esc_alumnos_config

        # Cargar la imagen y obtener su Rect
        self.image = pygame.image.load("../media/estudianteb.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializar la posición del alumno
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

        # Convertir posiciones a valores flotantes para mayor precisión en el movimiento
        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)

        # Velocidad del alumno
        self.alumno_speed = self.esc_alumnos_config.alumnos_speed

        # Bandera para el movimiento
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def dibujar(self):
        """Dibuja al alumno en su posición actual."""
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        """Actualiza la posición del alumno basado en las teclas presionadas."""
        # Movimiento hacia la derecha
        if self.is_moving_right and (self.image_rect.right < self.screen_rect.right):
            self.image_rect_centerx += self.alumno_speed

        # Movimiento hacia la izquierda
        if self.is_moving_left and (self.image_rect.left > self.screen_rect.left):
            self.image_rect_centerx -= self.alumno_speed

        # Movimiento hacia arriba
        if self.is_moving_up and (self.image_rect.top > self.screen_rect.top):
            self.image_rect_centery -= self.alumno_speed

        # Movimiento hacia abajo
        if self.is_moving_down and (self.image_rect.bottom < self.screen_rect.bottom):
            self.image_rect_centery += self.alumno_speed

        # Actualizar la posición del rectángulo basado en las nuevas coordenadas
        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

    def blitme(self):

        self.screen.blit(self.image, self.image_rect)

