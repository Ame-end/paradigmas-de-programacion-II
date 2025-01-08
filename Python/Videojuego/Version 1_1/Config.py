# Se crea una clase para las configuraciones
#import pygame


class Config:
    def __init__(self):
        self.screen_witdh = 1080  # Ancho
        self.screen_height = 720  # Altura
        self.game_title = "Escape Alumnos"
        self.backgroundcolor = (11, 8, 101)
        # self.backgroundimage = pygame.image.load("../media/back.png")
        self.alumno_speed = 1

        #Configuraciones para laptop
        self.laptop_speed=0.15
