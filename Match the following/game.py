import pygame
pygame.init()

screen = pygame.display.set_mode((750,750))
screen.fill((255,255,255))
pygame.display.update()

cc = pygame.image.load("CandyCrush.jpg")
ludo = pygame.image.load("Ludo.png")
ss = pygame.image.load("SubwaySurfers.png")
tr = pygame.image.load("TempleRun.png")

screen.blit(cc,(100,100))
screen.blit(ludo,(100,250))
screen.blit(ss,(100,400))
screen.blit(tr,(100,550))

font = pygame.font.SysFont("Times New Roman", 35)

cctext = font.render("Candy Crush", True, (0,0,0))
ludotext = font.render("Ludo", True, (0,0,0))
sstext = font.render("Subway Surfers", True, (0,0,0))
trtext = font.render("Temple Run", True, (0,0,0))

screen.blit(trtext,(500,100))
screen.blit(sstext,(500,250))
screen.blit(ludotext,(500,400))
screen.blit(cctext,(500,550))

while 1:
    event = pygame.event.poll()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (100,50,155), (pos), 10, 0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos1 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (100,50,155), (pos),(pos1), 7)
        pygame.draw.circle(screen, (100,50,155), (pos1), 10, 0)
        pygame.display.update()