import pygame


# Clase para manipular al alumno
class Alumno:
    # Constructor-screen es lo que recibe
    def __init__(self, screen):
        self.screen = screen
        # Se encarga la imagen y se obtiene el RECT
        # Se utiliza para representar coordenadas rectangulares
        self.image = pygame.image.load("../media/estudianteb.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom  # Alineación
        #Bandera
        self.is_moving_right = False
        #self.is_moving_left = False
    def update(self):
        if self.is_moving_right:
            self.image_rect.centerx += 1
    '''
        def update(self):
        if self.is_moving_left:
            self.image_rect.centerx -=1
    '''



        # Méto.do que dibuja al alumno en su ubicación

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
