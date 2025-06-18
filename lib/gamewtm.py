import pygame,random,time
from pygame import mixer
from tkinter import messagebox
pygame.init()


def level2():
    pygame.init()
    w1,h1=700,500
    win=pygame.display.set_mode((w1,h1))
    pygame.display.set_caption('level2')
    bg=pygame.image.load('bg1.png')

    eatfx=mixer.Sound('eatfx.mp3')
    winfx=mixer.Sound('wins1.mp3')
    losefx=mixer.Sound('losefx.mp3')

    st=pygame.time.get_ticks()

    song=mixer.music.load('01.mp3')
    mixer.music.play(-1)

    to=mixer.Sound('timeover.mp3')
    
    x,y=w1//2,h1//2
    lx,ly=0,700
    lx1,ly1=700,10
    lx2,ly2=700,490
    bx,by=200,400
    bx1,by1=319,129
    cx,cy=100,200
    score=0 
    loop=True

    r=10

    while loop:
        pygame.time.delay(15)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                loop=False

        win.blit(bg,(0,0))

        seconds=(pygame.time.get_ticks()-st)/1000
        print(f'{seconds}')

        rectangle=pygame.draw.rect(win,(255,255,0),(x,y,40,40))
        char1=pygame.draw.circle(win,(0,102,255),(cx,cy),r)
        block1=pygame.draw.rect(win,(255,0,0),(bx,by,20,1000))
        block2=pygame.draw.rect(win,(255,0,0),(bx1,by1,1000,50))

        border=pygame.draw.line(win,(255,255,255),(lx,ly),(lx,0))
        border2=pygame.draw.line(win,(255,255,255),(lx1,ly1),(0,ly1))
        border3=pygame.draw.line(win,(255,255,255),(lx2,ly2),(0,ly2))
        
        border4=pygame.draw.line(win,(255,255,255),(690,700),(690,0))

        collide=rectangle.collidepoint(cx,cy)
        collide2=block1.collidepoint(cx,cy)
        collide3=block2.collidepoint(cx,cy)
        boundary=border.collidepoint(cx,cy)
        boundary2=border2.collidepoint(cx,cy)
        boundary3=border3.collidepoint(cx,cy)
        boundary4=border4.collidepoint(cx,cy)


        #cx+=2
        if boundary:cx,cy=600,100
        if boundary2:cx,cy=100,500
        if boundary3:cx,cy=103,210
        if boundary4:cx,cy=10,200

        if collide:
            eatfx.play()
            x,y=random.randrange(w1),random.randrange(h1)
            r+=5
            score+=10
            print(f'score {score}')

            if r==85:
                winfx.play()
                messagebox.showinfo('CONGRATULATIONS','YOU WON LEVEL 2')
                loop=False
                level3()


        if collide2:
            losefx.play()
            messagebox.showerror('LOST','SORRY YOU LOST')
            loop=False

        if collide3:
            losefx.play()
            messagebox.showerror('LOST','SORRY YOU LOST')
            loop=False

        if seconds>15:
            mixer.music.stop()
            to.play()
            messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')

        k=pygame.key.get_pressed()

        if k[pygame.K_UP]:cy-=10
        elif k[pygame.K_DOWN]:cy+=10
        elif k[pygame.K_LEFT]:cx-=10
        elif k[pygame.K_RIGHT]:cx+=10

        pygame.display.update()

        win.fill((0,0,0))

    pygame.quit()






#LEVEL 3 CODE GOES HERE 

width,height=700,500
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('Catch The Box')
bg=pygame.image.load('bg1.png')
song=mixer.music.load('01.mp3')
mixer.music.play(-1)
eatfx=mixer.Sound('eatfx.mp3')
to=mixer.Sound('timeover.mp3')
winfx=mixer.Sound('wins1.mp3')
losefx=mixer.Sound('losefx.mp3')
#starting point of game
st=pygame.time.get_ticks()
x,y=width//2,height//2
lx,ly=0,700
lx1,ly1=700,10
lx2,ly2=700,490
lx3,ly3=690,700
bx,by=400,200
cx,cy=100,200
score=0
loop=True
r=10

while loop:

    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            loop=False

    win.blit(bg,(0,0))
    seconds=(pygame.time.get_ticks()-st)/1000
    print(f'{seconds} Seconds')
    #mixer.music.play(-1)


    #song=pygame.mixer.music.load('01.mp3')
    
    mouse=pygame.mouse.get_pos()

    rectangle=pygame.draw.rect(win,(255,255,0),(x,y,40,40))
    block=pygame.draw.rect(win,(255,0,0),(bx,by,20,1000))
    char1=pygame.draw.circle(win,(0,102,255),(cx,cy),r)

    border=pygame.draw.line(win,(255,255,255),(lx,ly),(lx,0))
    border2=pygame.draw.line(win,(255,255,255),(lx1,ly1),(0,ly1))
    border3=pygame.draw.line(win,(255,255,255),(lx2,ly2),(0,ly2))
    border4=pygame.draw.line(win,(255,255,255),(lx3,ly3),(lx3,0))


    #cx-=2

    k=pygame.key.get_pressed()

    if k[pygame.K_UP]:cy-=10
    elif k[pygame.K_DOWN]:cy+=10
    elif k[pygame.K_LEFT]:cx-=10
    elif k[pygame.K_RIGHT]:cx+=10

    point=pygame.mouse.get_pos()
    collide=rectangle.collidepoint(cx,cy)
    collide1=rectangle.collidepoint(mouse)
    collide2=block.collidepoint(cx,cy)
    collide3=char1.collidepoint(width,height)
    boundary=border.collidepoint(cx,cy)
    boundary2=border2.collidepoint(cx,cy)
    boundary3=border3.collidepoint(cx,cy)
    boundary4=border4.collidepoint(cx,cy)

    
    if boundary:
        cx,cy=600,100
    if boundary2:
        cx,cy=100,500
    if boundary3:
        cx,cy=103,210
    if boundary4:
        cx,cy=10,200
    if collide1:
        eatfx.play()
        cx,cy=x,y
        x,y=random.randrange(width-100),random.randrange(400)
        r+=5

        if r==75:
            winfx.play()
            messagebox.showinfo('CONGRATULATIONS','YOU WIN LEVEL 1')
            loop=False
            level2()
    if seconds>15:
        mixer.music.stop()
        to.play()
        messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')
        
        
        loop=False
    if collide:
        eatfx.play()
        
        x,y=random.randrange(width-100),random.randrange(400)
        r+=5
        score+=10
        print(f'score {score}')
        print(f'you{cx,cy}')
        print(f'yellow box:{x,y}')

        if r==75:
            winfx.play()
            messagebox.showinfo('CONGRATULATIONS!','YOU WIN ROUND 1')
            loop=False
            level2()

        elif x in range(bx) or y in range(by):
            x+=10
            y+=10

        elif x in range(bx) and y in range(by):
            x+=10
            y+=10

    if collide2:
        mixer.music.stop()
        losefx.play()
        messagebox.showerror('LOST','SORRY YOU LOST THE GAME!')
        loop=False

    if collide3:
        cx,cy=105,206


    
    pygame.display.update()
    win.fill((0,0,0))
pygame.quit()
t2=time.time()

