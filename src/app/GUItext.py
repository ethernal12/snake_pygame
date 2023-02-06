import pygame


def messages(canvas, text):
    # Nastavi font
    font = pygame.font.Font('freesansbold.ttf', 30)
    # Ustvari text podlago
    text_podlaga = font.render(f'Points: {str(text)}', True, (0, 0, 0))
    # Nariši text na canvas
    canvas.blit(text_podlaga, (0, 0))
    pygame.display.update()
