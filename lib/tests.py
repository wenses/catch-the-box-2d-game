import pygame
from pygame import mixer

pygame.init()
win=pygame.display.set_mode((500,500))

#n=int(input('Enter number'))
winsfx=mixer.Sound('wins1.mp3')
clock=pygame.time.Clock()
loop=True
st=pygame.time.get_ticks()
print(st)
while loop:
    clock.tick(10)

    for x in pygame.event.get():
        if x.type==pygame.QUIT:
            loop=False
    s=(pygame.time.get_ticks()-st)/1000
    print(s)
    if s>10:
        loop=False
    pygame.draw.rect(win,(0,102,200),(250,250,40,40))
    pygame.display.flip()
    win.fill((0,0,0))

pygame.quit()

