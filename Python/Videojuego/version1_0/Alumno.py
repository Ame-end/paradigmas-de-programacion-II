import pygame


# Clase para manipular al alumno
class Alumno:
    # Constructor-screen es lo que recibe
    def __init__(self, screen, esc_alumnos_config):
        self.screen = screen
        self.esc_alumnos_config=esc_alumnos_config
        # Se encarga la imagen y se obtiene el RECT
        # Se utiliza para representar coordenadas rectangulares
        self.image = pygame.image.load("../media/estudianteb.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom  # Alineación

        self.alumno_speed= self.esc_alumnos_config.alumnos_speed
        # Bandera
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

        # Velocidad
        self.esc_alumnos_config = esc_alumnos_config  # creacion del objeto
           # Variable para la velocidad
        # self.image_rect_centerx +=self.alumno_speed
        self.image_rect_centerx = float(self.image_rect.centerx)#obtiene el centro de la imagen
        self.image_rect_centery = float(self.image_rect.centery)

    def dibujar(self):
        self.screen.blit(self.image, self.image_rect)

    # DERECHA
    def update(self):
        # DERECHA
        if self.is_moving_right and (self.image_rect.right < self.screen_rect.right):
            self.image_rect_centerx += self.alumno_speed

        # IZQUIERDA
        if self.is_moving_left and (self.image_rect.left > self.screen_rect.left):
            self.image_rect_centerx -= self.alumno_speed

        # ARRIBA
        if self.is_moving_up and (self.image_rect.top > self.screen_rect.top):
            self.image_rect_centery -= self.alumno_speed

        # ABAJO
        if self.is_moving_down and (self.image_rect.bottom < self.screen_rect.bottom):
            self.image_rect_centery += self.alumno_speed

        #DIAGONAL

        # Actualizar la posición del rectángulo basado en las nuevas coordenadas
        self.image_rect.centerx = self.image_rect_centerx
        self.image_rect.centery = self.image_rect_centery

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)


