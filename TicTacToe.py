import pygame
import Matriz_custom as draw_custom

pygame.init() #initialize all modules

screen = pygame.display.set_mode((640,480)) # window size

pygame.display.set_caption("Tic Tac Toe")   # window name

clock = pygame.time.Clock()

run = True

##x = 270
##y = 190

tabuleiro_display = []

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1

    #draw_custom.draw_matriz((5,5),(100,100,(0,0,255))) #TODO: testar dps

    tabuleiro_display = draw_custom.draw_matriz((3,3),(100,100,(255,255,255)))

    #pygame.draw.rect(screen, (255,0,0), (x,y,100,100))
    
    pygame.display.update()
    clock.tick(60) #60fps
     
pygame.quit()   #closes all modules previously init()
print(tabuleiro_display)
#quit()         #quit python shell
