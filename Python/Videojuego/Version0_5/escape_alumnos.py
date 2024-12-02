
import pygame

import Game_functionalities
from Config import Config
from Alumno import Alumno
from Python.Videojuego.Version0_5.Game_functionalities import game_events


# Función para inicializar el juego
def run_game():
    # inicializar la pantalla
    pygame.init()
    esc_alumnos_config = Config()

    #Configuración de pantalla
    screen_size = (esc_alumnos_config.screen_witdh, esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    #game_title = esc_alumnos_config.game_title

    #Se crea el objeto de tipo alumno
    pygame.display.set_caption(esc_alumnos_config.game_title)


    # Se crea un objeto de tipo alumno
    alumno = Alumno(screen, esc_alumnos_config)

    running = True
    #IMAGEN DE FONDO->backgrounds_image=pygame.transform.scale(esc_alumnos_config.backgroundimage,screen_size)
    while running:
        #IMAGEN DE FONDO->screen.blit(backgrounds_image,(0,0))

        #for event in pygame.event.get():
        #Meter en una funcion

        #Game_functionalities.game_events(alumno)
        game_events(alumno)
            #if event.type == pygame.quit:
             #   sys.exit()
        background_color = esc_alumnos_config.backgroundcolor
        screen.fill(background_color)
        # Actualiza la pantalla con los cambios realizados (ilusión de movimiento)
        alumno.update()
        alumno.blitme()
        pygame.display.flip()


# Codigo a nivel de modulo
run_game()
