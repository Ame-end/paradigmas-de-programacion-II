import sys
import pygame
from Config import Config

#Función para inicializar el juego
def run_game():
    #inicializar la pantalla
    pygame.init()
    esc_alumnos_config=Config()
    screen=(esc_alumnos_config.screen_witdh, esc_alumnos_config.screen_height)
    display=pygame.display.set_mode(screen)

    game_title=esc_alumnos_config.game_title
    #Muestra el titulo en la pantalla
    pygame.display.set_caption(game_title)
    #Accion que realiza el usuario ( teclado)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.quit:
                sys.exit()
            background_color=esc_alumnos_config.backgroundcolor
            display.fill(background_color)
            #Actualiza la pantalla con los cambios realizados (ilusión de movimiento)
            pygame.display.flip()

#Codigo a nivel de modulo
run_game()