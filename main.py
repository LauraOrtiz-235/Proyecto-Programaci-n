import pygame
from game import Game

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    # Inicialización de todos los módulos importados de pygame y que se usaron
    pygame.init()
    # Se pone el ancho y el altura de la pantalla 
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Establecer el título de la ventana emergente
    pygame.display.set_caption("MACCtemáticas")
    # Bucle hasta que el usuario oprima el boton de cerrar la ventana
    done = False
    # Se usa para manejar que tan rápido se actializa la pantalla
    clock = pygame.time.Clock()
    # Se crea el objeto game
    game = Game()
    # Bucle Principal del Programa 
    while not done:
        # Se procesan los eventos (pulsaciones de tecla, clicks,etc)
        done = game.process_events(screen)
        # Lógica del juego
        game.run_logic()
        # Se dibuja los recuadros de la pantalla
        game.display_frame(screen)
        # Se limita a 30 recuadros por segundo
        clock.tick(30)

    # Se cierra la ventana
    pygame.quit()

if __name__ == '__main__':
    main()

