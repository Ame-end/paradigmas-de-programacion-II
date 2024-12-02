import pygame
from pygame.sprite import Sprite
#De la clase pygame se importa el Sprite-herencia

class Laptop(Sprite):

    def __init__(self,esc_alumnos_config,alumno,screen):
        super(Laptop,self).__init__()#Se llama al constructor
        self.esc_alumnos_config = esc_alumnos_config
        self.screen=screen
        self.alumno=alumno

        self.image = pygame.image.load("../media/back.png")
        self.lap_rect = self.image.get_rect() #rectangulo para la laptop

        #Se crea un rectangulo para el alumno
        self.alumno_rect = self.alumno.get_rect()

        self.lap_rect.centerx=self.alumno_rect.centerx
        self.lap_rect.bottom=self.alumno_rect.top

        #Velocidad
        self.image_rect_centerx = float(self.lap_rect.centerx)#obtiene el centro de la imagen
        self.image_rect_centery = float(self.lap_rect.centery)

        #Declara la velocidad y asignarle
        self.laptop_speed = self.esc_alumnos_config.laptop_speed

