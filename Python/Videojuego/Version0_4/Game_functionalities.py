import sys
import pygame


def game_events(alumno):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Verificar si presionó una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = True
            # Verificar si se presiona la tecla izquierda
            # elif event.key == pygame.K_LEFT:
            #       alumno.is_moving_left = True
        elif event.type == pygame.KEYUP:
                # Verificar si se suelta la tecla derecha
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = False


'''
  elif event.type == pygame.KEYUP:
                # Verificar si se suelta la tecla derecha
                if event.key == pygame.K_RIGHT:
                    alumno.is_moving_right = False
                # Verificar si se suelta la tecla izquierda
                elif event.key == pygame.K_LEFT:
                    alumno.is_moving_left = False

'''
