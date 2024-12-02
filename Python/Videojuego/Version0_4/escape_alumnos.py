import sys
import pygame
import Game_functionalities
from Config import Config
from Alumno import Alumno



# Función para inicializar el juego
def run_game():
    # inicializar la pantalla
    pygame.init()
    esc_alumnos_config = Config()
    screen_size = (esc_alumnos_config.screen_witdh, esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    game_title = esc_alumnos_config.game_title
    # Muestra el titulo en la pantalla
    pygame.display.set_caption(game_title)
    # Accion que realiza el usuario ( teclado)

    # Se crea un objeto de tipo alumno
    alumno = Alumno(screen)

    running = True
    while running:
        #for event in pygame.event.get():
        #Meter en una funcion
        Game_functionalities.game_events(alumno)
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
