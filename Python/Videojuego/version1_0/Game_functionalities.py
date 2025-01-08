import sys
import pygame

# Función que administra los eventos del juego.
def game_events(alumno):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Verificar si se presiona una tecla.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = True
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = True
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = True

        # Verificar si se suelta una tecla.
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = False
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = False

# Función que actualiza y refresca la pantalla.
def screen_refresh(esc_alumnos_config, screen, alumno, laptop):
    # Rellenar el fondo de la pantalla con el color definido.
    background = esc_alumnos_config.background_color
    screen.fill(background)

    # Actualizar la posición del alumno y la laptop.
    alumno.update_pos()
    laptop.update_pos()

    # Mostrar el alumno y la laptop en la pantalla.
    alumno.blitme()
    laptop.blitme()

    # Actualización de la pantalla.
    pygame.display.flip()
