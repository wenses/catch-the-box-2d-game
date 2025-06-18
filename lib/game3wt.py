import pygame,random,time,tkinter
from pygame import mixer
from tkinter import messagebox
from tkinter import *
pygame.init()

#MAIN MENU CODE GOES HERE
def menu():
    disp=Tk()
    disp.config(bg='black')
    disp.title('Catch The Box')
    disp.geometry('700x500')
    disp.resizable(FALSE,FALSE)

    song=mixer.music.load('01.mp3')
    mixer.music.play(-1)

    fn=('Consolas',17,'bold')

    def continuegame():
        logdata=open('ctb_log.txt','r').read()

        if logdata!='':
            scorelog=logdata

            if scorelog=='2':
                disp.destroy()
                level2()

            elif scorelog=='3':
                disp.destroy()
                level3()

            elif scorelog=='':
                messagebox.showerror('NO SAVED DATA','THERE IS NO SAVED DATA')


            else:
                messagebox.showwarning('NO SAVED DATA','IT SEEMS THERE WAS NO SAVED DATA THE GAME SHALL START FROM BEGINNING')

    def newgame():
        global mouse_controller
        info=Entry.get(e1)
        info=str(info)
        info=info.lower()
        if info=='mouse':
            mouse_controller=True
        else:
            mouse_controller=False
        disp.destroy()
        newlog=''
        lgf=open('ctb_log.txt','w').write(newlog)
        level1()

    def howtoplay():
        instructions='''
THE CHARACTER IS THE BLUE BALL THE AIM IS TO EAT AS MANY YELLOW BOXES YOU CAN SEE
WHEN YOU EAT A YELLOW BOX YOUR FOOD BAR IS FILLED MAKE SURE YOU FEED YOURSELF BEFORE TIME RUNS
OUT,THE GREEN BAR REPRESENTS TIME AS YOU PLAY IT KEEPS ON DECREASING MAKE SURE YOU EAT ALL THE
BOXES BEFORE IT IS OVER(TIME) YOU CAN CONTROL THE CHARATER BY USING ARROW KEYS
NOTE:YOU CANNOT CONTINUE GAME IF YOU HAVENT ACCOMPLISHED LEVEL
ALSO IF YOU WANT TO USE MOUSE TYPE MOUSE ON THE BAR IF YOU DONT WANT WRITE SOMETHING ELSE'''
        messagebox.showinfo('HOW TO PLAY THE GAME',instructions)

    def credits():
        credit='''
THIS GAME WAS PROGRAMMED AND MADE BY WENSESLAUS BAHATI
TESTED AND DESIGNED BY LEON EXIMIUS'''
        messagebox.showinfo('CREDITS',credit)


    b1=Button(disp,text='CONTINUE GAME',fg='white',bg='green',font=fn,command=continuegame)
    b1.place(x=200,y=100)

    b2=Button(disp,text='NEW GAME',fg='white',bg='blue',font=fn,command=newgame)
    b2.place(x=200,y=200)

    b3=Button(disp,text='HOW TO PLAY GAME',fg='white',bg='yellow',font=fn,command=howtoplay)
    b3.place(x=200,y=300)

    b4=Button(disp,text='CREDITS',fg='white',bg='light blue',font=fn,command=credits)
    b4.place(x=200,y=400)

    l1=Label(disp,text='USE MOUSE OR ARROWS:(mouse/arrows):',font=('Consolas',9,'italic'),fg='white',bg='black')
    l1.place(x=0,y=450)
    e1=Entry(disp,bd=4,width=65)
    e1.place(x=250,y=450)

    disp.mainloop()

#LEVEL 3 CODE GOES HERE

def level3():
    global mouse_controller
    pygame.init()
    w1,h1=700,500
    win=pygame.display.set_mode((w1,h1))
    pygame.display.set_caption('Catch The Box:Level 3')
    pygame.display.set_icon(pygame.image.load('yellowbox.png'))
    bg=pygame.image.load('bg2.jpg')
    #mouse_controller=True
    hbw=1000

    eatfx=mixer.Sound('eatfx.mp3')
    winfx=mixer.Sound('wins1.mp3')
    losefx=mixer.Sound('losefx.mp3')

    score_length=0

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
        hbw-=1
        if hbw==0:
        
            to.play()
            messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')
            loop=False

        timebar=pygame.draw.rect(win,(0,255,0),(10,10,hbw,10))
        scoreborder=pygame.draw.rect(win,(255,255,255),(10,35,425,10))
        scorebar=pygame.draw.rect(win,(255,255,0),(10,35,score_length,10))

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

        if mouse_controller==True:
            mpos=pygame.mouse.get_pos()
            cx,cy=mpos


        #cx+=2
        if boundary:cx,cy=600,100
        if boundary2:cx,cy=100,500
        if boundary3:cx,cy=103,210
        if boundary4:cx,cy=10,200

        if collide:
            eatfx.play()
            score_length+=25
            x,y=random.randrange(w1),random.randrange(h1)
            r+=5
            score+=10
            print(f'score {score}')

            if r==95:
                winfx.play()
                #messagebox.showinfo('CONGRATULATIONS','YOU WON LEVEL 3')
                loop=False
                #level3()
                messagebox.showinfo('CONGRATULATIONS','YOU HAVE OFFICIALLY WON CATCH THE BOX PREPARE FOR YOUR GIFT')


        if collide2:
            losefx.play()
            messagebox.showerror('GAME OVER!','SORRY YOU LOST')
            loop=False

        if collide3:
            losefx.play()
            messagebox.showerror('GAME OVER!','SORRY YOU LOST')
            loop=False

        #if seconds>25:
         #   mixer.music.stop()
         #   to.play()
         #   messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')

        k=pygame.key.get_pressed()

        if k[pygame.K_UP]:cy-=10
        elif k[pygame.K_DOWN]:cy+=10
        elif k[pygame.K_LEFT]:cx-=10
        elif k[pygame.K_RIGHT]:cx+=10

        pygame.display.update()

        win.fill((0,0,0))

    pygame.quit()



#LEVEL 2 CODE GOES HERE 
def level2():
    global mouse_controller
    pygame.init()
    width,height=700,500
    win=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Catch The Box:Level 2')
    pygame.display.set_icon(pygame.image.load('yellowbox.png'))
    bg=pygame.image.load('bg3.png')
    song=mixer.music.load('01.mp3')
    mixer.music.play(-1)
    eatfx=mixer.Sound('eatfx.mp3')
    to=mixer.Sound('timeover.mp3')
    winfx=mixer.Sound('wins1.mp3')
    losefx=mixer.Sound('losefx.mp3')
    #mouse_controller=True
    hbw=1250
    cheat_code=False
    score_length=0
    #starting point of game
    st=pygame.time.get_ticks()
    x,y=width//2,height//2
    lx,ly=0,700
    lx1,ly1=700,10
    lx2,ly2=700,490
    lx3,ly3=690,700
    bx,by=400,200
    bx2,by2=200,400
    bx3,by3=315,599
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
        hbw-=1
        if hbw==0:
            
            to.play()
            messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')
            loop=False
        #mixer.music.play(-1)


        #song=pygame.mixer.music.load('01.mp3')
        timebar=pygame.draw.rect(win,(0,255,0),(10,10,hbw,10))
        scoreborder=pygame.draw.rect(win,(255,255,255),(10,35,375,10))
        scorebar=pygame.draw.rect(win,(255,255,0),(10,35,score_length,10))


        rectangle=pygame.draw.rect(win,(255,255,0),(x,y,40,40))
        block=pygame.draw.rect(win,(255,0,0),(bx,by,20,1000))
        block2=pygame.draw.rect(win,(255,0,0),(bx2,by2,1000,20))
        block3=pygame.draw.rect(win,(255,0,0),(bx3,by3,600,20))
        char1=pygame.draw.circle(win,(0,102,255),(cx,cy),r)

        border=pygame.draw.line(win,(255,255,255),(lx,ly),(lx,0))
        border2=pygame.draw.line(win,(255,255,255),(lx1,ly1),(0,ly1))
        border3=pygame.draw.line(win,(255,255,255),(lx2,ly2),(0,ly2))
        border4=pygame.draw.line(win,(255,255,255),(lx3,ly3),(lx3,0))

        if mouse_controller==True:
            mpos=pygame.mouse.get_pos()
            cx,cy=mpos


        #cx-=2

        k=pygame.key.get_pressed()

        if k[pygame.K_UP]:cy-=10
        elif k[pygame.K_DOWN]:cy+=10
        elif k[pygame.K_LEFT]:cx-=10
        elif k[pygame.K_RIGHT]:cx+=10

        point=pygame.mouse.get_pos()
        collide=rectangle.collidepoint(cx,cy)
        collide2=block.collidepoint(cx,cy)
        collide02=block2.collidepoint(cx,cy)
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
        #if seconds>20:
         #   mixer.music.stop()
          #  to.play()
          #  messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')'''
            
            
            #loop=False
        if collide:
            eatfx.play()
            score_length+=25
            x,y=random.randrange(width-100),random.randrange(400)
            r+=5
            score+=10
            print(f'score {score}')
            print(f'you{cx,cy}')
            print(f'yellow box:{x,y}')



            if r==85:
                winfx.play()
                #messagebox.showinfo('CONGRATULATIONS!','YOU WIN ROUND 1')
                loop=False
                lgdata=str(3)
                logfile=open('ctb_log.txt','w').write(lgdata)
                level3()

            elif x in range(bx) or y in range(by):
                x+=10
                y+=10

            elif x in range(bx) and y in range(by):
                x+=10
                y+=10

        if collide2:
            mixer.music.stop()
            losefx.play()
            messagebox.showerror('GAME OVER!','SORRY YOU LOST THE GAME!')
            loop=False

        if collide02:
            mixer.music.stop()
            losefx.play()
            messagebox.showerror('GAME OVER!','SORRY YOU LOST THE GAME!')
            loop=False

        if collide3:
            cx,cy=105,206

        if cheat_code==True:
            if k[pygame.K_w]:cx,cy=x,y


        
        pygame.display.update()
        win.fill((0,0,0))
    pygame.quit()


#LEVEL 1 CODE GOES HERE


def level1():

    global mouse_controller

    pygame.init()
    width,height=700,500
    win=pygame.display.set_mode((width,height))
    pygame.display.set_caption('Catch The Box:Level 1')
    pygame.display.set_icon(pygame.image.load('yellowbox.png'))

    #mouse_controller=True

    #logdata=open('ctb_log.txt','r').read()

    bg=pygame.image.load('bg1.png')
    song=mixer.music.load('01.mp3')
    mixer.music.play(-1)
    eatfx=mixer.Sound('eatfx.mp3')
    to=mixer.Sound('timeover.mp3')
    winfx=mixer.Sound('wins1.mp3')
    losefx=mixer.Sound('losefx.mp3')
    hbw=1450
    cheat_code=False
    score_length=0
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
        hbw-=1
        if hbw==0:
            
            to.play()
            messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')
            loop=False
        #mixer.music.play(-1)


        #song=pygame.mixer.music.load('01.mp3')
        timebar=pygame.draw.rect(win,(0,255,0),(10,10,hbw,10))
        scoreborder=pygame.draw.rect(win,(255,255,255),(10,35,325,10))
        scorebar=pygame.draw.rect(win,(255,255,0),(10,35,score_length,10))


        rectangle=pygame.draw.rect(win,(255,255,0),(x,y,40,40))
        block=pygame.draw.rect(win,(255,0,0),(bx,by,20,1000))
        char1=pygame.draw.circle(win,(0,102,255),(cx,cy),r)

        border=pygame.draw.line(win,(255,255,255),(lx,ly),(lx,0))
        border2=pygame.draw.line(win,(255,255,255),(lx1,ly1),(0,ly1))
        border3=pygame.draw.line(win,(255,255,255),(lx2,ly2),(0,ly2))
        border4=pygame.draw.line(win,(255,255,255),(lx3,ly3),(lx3,0))

        if mouse_controller==True:
            mpos=pygame.mouse.get_pos()
            cx,cy=mpos


        #cx-=2

        k=pygame.key.get_pressed()

        if k[pygame.K_UP]:cy-=10
        elif k[pygame.K_DOWN]:cy+=10
        elif k[pygame.K_LEFT]:cx-=10
        elif k[pygame.K_RIGHT]:cx+=10

        point=pygame.mouse.get_pos()
        collide=rectangle.collidepoint(cx,cy)
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
        #if seconds>30:
        #    mixer.music.stop()
        #    to.play()
        #    messagebox.showerror('TIME OVER','YOU LOST DUE TO TIME OVER')
            
            
        #  loop=False
        if collide:
            eatfx.play()
            score_length+=25
            x,y=random.randrange(width-100),random.randrange(400)
            r+=5
            score+=10
            print(f'score {score}')
            print(f'you{cx,cy}')
            print(f'yellow box:{x,y}')



            if r==75:
                winfx.play()
                #messagebox.showinfo('CONGRATULATIONS!','YOU WIN ROUND 1')
                loop=False
                lgdata=str(2)
                logfile=open('ctb_log.txt','w').write(lgdata)
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
            messagebox.showerror('GAME OVER!','SORRY YOU LOST THE GAME!')
            loop=False

        if collide3:
            cx,cy=105,206

        if cheat_code==True:
            if k[pygame.K_w]:cx,cy=x,y


        
        pygame.display.update()
        win.fill((0,0,0))
    pygame.quit()
    t2=time.time()

#level1()
menu()