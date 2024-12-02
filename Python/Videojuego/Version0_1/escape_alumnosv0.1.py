import sys
import pygame


#Función para inicializar el juego
def run_game():

    #Siempre se requerira
    #----Inicializar la pantalla------
    pygame.init()
    screen=(1080,720)#configuración
    display=pygame.display.set_mode(screen) #Le mandamos la pantalla

    #Mandar el titulo del juego a la pantalla
    game_title = "Escape de alumnos"
    pygame.display.set_caption(game_title)

    #Ciclo infinito- debemos de verificar que es lo que pasa
    running = True
    #Lo que realizará el usuario
    #Cosas del rato o el teclado
    while running: #Para buscar eventos del teclado o ratón
        for event in pygame.event.get():
            #Vemos que evento realizo
            if event.type==pygame.QUIT: #Se verifica un primer evento
                sys.exit()
            #Cambiar el color
            background_color=(186, 230, 243 )
            display.fill(background_color) #rellenar
            #Actualiza la pantalla con los cambios realizados, ilusión de mouse
            pygame.display.flip()
#código a nivel de módulo
run_game()
