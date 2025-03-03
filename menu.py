import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Menu')
Font = pygame.font.SysFont("comicsans", 55)

def write_text(text, font, colour, x, y):
    text = font.render(text, True, colour)
    screen.blit(text, (x, y))

run = True
while run:
    screen.fill((228, 202, 248))  # Fill the screen first
    write_text('SPACE to start', Font, (255, 255, 255),150, 200)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                run = False  # Stop the menu loop to start the game
                import pongy  # Import the game module to start the game

pygame.quit()