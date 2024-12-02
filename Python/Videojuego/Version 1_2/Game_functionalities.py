import sys
import pygame
from Laptop import Laptop

#FUNCION
def game_events(esc_alumnos_config,screen,alumno,laptops_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



        # Verificar si presionó una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = True
            # Verificar si se presiona la tecla izquierda
            elif event.key == pygame.K_LEFT:
               alumno.is_moving_left = True
            elif event.key ==pygame.K_UP:
                alumno.is_moving_up=True
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down=True

        elif event.type == pygame.KEYUP:
                # Verificar si se suelta la tecla derecha
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = False
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = False

        elif event.key ==pygame.K_SPACE:
            new laptop = Laptop(esc_alumnos_config,screen,alumno)

            laptops_group.add(new_laptop)

def screen_refresh(esc_alumnos_config,screen, alumno,laptop):
    background=esc_alumnos_config.background_color
    screen.fill(background)

    #Actualiza la posición del alumno y la laptop
    alumno.update_pos()
    laptop.update_pos()
    #Se muestra el objeto del alumno y la laptop en la pantalla
    alumno.blitme()
    laptop.blitme()

    #Actualización de la pantalla
    pygame.display.flip()