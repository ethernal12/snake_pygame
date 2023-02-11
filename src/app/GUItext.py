import pygame

def messages(canvas, text, title, poistionX, positionY):
    # Nastavi font
    font = pygame.font.Font('freesansbold.ttf', 30)
    # Ustvari text podlago
    text_podlaga = font.render(f'{title} {str(text)}', True, (0, 0, 0))
    # Nariši text na canvas
    canvas.blit(text_podlaga, (poistionX, positionY))
    pygame.display.update()
