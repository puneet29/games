import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (200, 200, 0)
red = (200, 0, 0)
cyan = (0, 255, 255)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

carImg = pygame.image.load("car.png")
carWidth = 64
carHeight = 64
pause = False

pygame.mixer.music.load("Surreal-Chase.mp3")
crash_sound = pygame.mixer.Sound("crash.wav")

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("this is our gameeeee, boyyyyyy")
pygame.display.set_icon(carImg)
clock = pygame.time.Clock()

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+ str(count), True, black)
    gameDisplay.blit(text,(10,10))

def things(thing1_x, thing1_y, thing2_x, thing2_y, thing3_x, thing3_y, thing4_x, thing4_y, thing_w, thing_h, thing_color):
    pygame.draw.rect(gameDisplay, thing_color, [thing1_x, thing1_y, thing_w, thing_h])
    pygame.draw.rect(gameDisplay, thing_color, [thing2_x, thing2_y, thing_w, thing_h])
    pygame.draw.rect(gameDisplay, thing_color, [thing3_x, thing3_y, thing_w, thing_h])
    pygame.draw.rect(gameDisplay, thing_color, [thing4_x, thing4_y, thing_w, thing_h])


def car (x, y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont("comicsansms" , 115)
    TextSurf, TextRect = text_objects(text, largeText, red)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)
    gameLoop()

def quitGame():
    pygame.quit()
    quit()

def unpause():
    pygame.mixer.music.unpause()

    global pause
    pause = False

def paused():
    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText, yellow)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        button("Continue",100, 450, 150, 50,green,bright_green,unpause)
        button("Quit",550, 450, 150, 50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText, red)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

        button("Play Again",100, 450, 150, 50,green,bright_green,gameLoop)
        button("Quit",550, 450, 150, 50,red,bright_red,quitGame)

        pygame.display.update()
        clock.tick(15)

def button(msg, x, y, w, h, ac, ic, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if(x+w>mouse[0]>x and y+h>mouse[1]>y):
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if (click[0]== 1 and action!= None):
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitGame()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("One last ride!", largeText, black)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 100, 450, 150, 50, bright_green, green, gameLoop)
        button("Quit!", 550, 450, 150, 50, bright_red, red, quitGame)

        pygame.display.update()
        clock.tick(15)


def gameLoop():
    pygame.mixer.music.play(-1)

    global pause

    x = (display_width * 0.48)
    y = (display_height * 0.88)
    dodged = 0
    x_change = 0

    thing_width = 100
    thing_height = 100
    thing1_startx = random.randrange(0 , 270-thing_width)
    thing1_starty = -(random.randrange(600 , 800))
    thing2_startx = random.randrange(270, 540-thing_width)
    thing2_starty = -(random.randrange(800 , 1000))
    thing3_startx = random.randrange(540, display_width-thing_width)
    thing3_starty = -(random.randrange(1000 , 1200))
    thing4_startx = random.randrange(540, display_width-thing_width)
    thing4_starty = -(random.randrange(1200 , 1400))
    thing_speed = 7
    thing_count = 1

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x+= x_change

        gameDisplay.fill(white)

        things(thing1_startx, thing1_starty, thing2_startx, thing2_starty, thing3_startx, thing3_starty, thing4_startx, thing4_starty, thing_width, thing_height, cyan)
        thing1_starty+=thing_speed
        thing2_starty+=thing_speed
        thing3_starty+=thing_speed
        thing4_starty+=thing_speed

        car(x, y)
        things_dodged(dodged)

        if (x > display_width - 48 or x < -16):
            crash()

        if (thing1_starty>display_height):
            thing1_starty = 0 - thing_height
            thing1_startx = random.randrange(0 , 200-thing_width)
            dodged+=1
            thing_speed+=0.02

        if (thing2_starty>display_height):
            thing2_starty = 0 - thing_height
            thing2_startx = random.randrange(200, 400-thing_width)
            dodged+=1
            thing_speed+=0.02

        if (thing3_starty>display_height):
            thing3_starty = 0 - thing_height
            thing3_startx = random.randrange(400, 600-thing_width)
            dodged+=1
            thing_speed+=0.02

        if (thing4_starty>display_height):
            thing4_starty = 0 - thing_height
            thing4_startx = random.randrange(600, display_width-thing_width)
            dodged+=1
            thing_speed+=0.02

        if (thing1_starty+thing_height>y and thing1_starty<y+carHeight):
            if (thing1_startx+thing_width>x and thing1_startx<x+carWidth):
                crash()

        if (thing2_starty+thing_height>y and thing2_starty<y+carHeight):
            if (thing2_startx+thing_width>x and thing2_startx<x+carWidth):
                crash()

        if (thing3_starty+thing_height>y and thing3_starty<y+carHeight):
            if (thing3_startx+thing_width>x and thing3_startx<x+carWidth):
                crash()

        if (thing4_starty+thing_height>y and thing4_starty<y+carHeight):
            if (thing4_startx+thing_width>x and thing4_startx<x+carWidth):
                crash()

        # sentdex's method:
        # if (thing_starty+thing_height>y):
        #     if ((thing_startx + thing_width>x and x>thing_startx) or (x + carWidth > thing_startx and x + carWidth < thing_startx + thing_width)) :
        #         crash()

        pygame.display.update()
        clock.tick(100)

gameIntro()
