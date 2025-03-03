import pygame
pygame.init()

# Creating screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Pongy!")

# Variables
speed_x = 300
force = 0
paddle_width = 190
paddle_height = 30
paddle_y = 700
Fps = 60
clock = pygame.time.Clock()

# Ball variables
ball_x = 400
ball_y = 400
ball_radius = 40
ball_speed_x = 5
ball_speed_y = 5
Score = 0
line_x = 798
line_y = 798
line_width = 2
line_height = 2
BG = pygame.image.load("Pongy/Buggati.png").convert_alpha()
BG = pygame.transform.scale(BG,(800,800))
#Functions
Font = pygame.font.SysFont("Comicsans",55)
def write(text,font,colour,x,y):
    img = font.render(text,True,colour)
    screen.blit(img,(x,y))
# Loops
run = True
while run:
    # Background colour
    screen.blit(BG,(0,0))
    pygame.draw.rect(screen, (255, 0, 255), (speed_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (0,0,0),(line_x,line_y,line_width,line_height))
    pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius)
    write("Score: "+str(Score),Font,(255,255,255),20,30)
    pygame.display.update()
    clock.tick(Fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                force = -10
            if event.key == pygame.K_RIGHT:
                force = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                force = 0

    # Update paddle position
    speed_x += force * 2
    if speed_x < 0:
        speed_x = 0
    if speed_x > 800 - paddle_width:
        speed_x = 800 - paddle_width

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with screen edges
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 800:
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 800:
        ball_speed_y *= -1
    #Collision with the paddle
    if ball_y + ball_radius >= paddle_y and ball_y + ball_radius < paddle_y + paddle_height and ball_x >= speed_x and ball_x <= speed_x + paddle_width:
        ball_speed_y *= -1 
        Score += 1  
    #Game over
    if abs(ball_y - line_y) <= ball_radius:
        write("Game Over",Font,(0,0,0),300,400)
        pygame.display.update()
        pygame.time.wait(2000)
        run = False     

pygame.quit()