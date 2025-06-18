import pygame
pygame.init()

disp=pygame.display.set_mode((500,500))
f=pygame.font.Font('freesansbold.ttf',12)
b,g=(0,0,102),(0,100,0)
t=f.render('Blixen Company',True,g,b)
tr=t.get_rect()
tr.center=(500//2,500//2)

loop=True
while loop:
    disp.fill((255,255,255))

    disp.blit(t,tr)

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            loop=False

    pygame.display.flip()

pygame.quit()