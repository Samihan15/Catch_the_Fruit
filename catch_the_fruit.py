import pygame
import os
import sys
import random
import math
import time
from pygame import mixer

pygame.init()  # initializing the pygame

# size of the screen 
window_size = (400,600)
screen = pygame.display.set_mode((window_size),0,32)  #setting the screen size

# background
background = pygame.image.load('background.jpg')


# background music
mixer.music.load(r'bgm.mp3')
mixer.music.play(-1)


# title and icon 
pygame.display.set_caption("Catch the fruit")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# game over
over_font = pygame.font.Font('freesansbold.ttf',64)

# score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10


# player 
playerImg = pygame.image.load('player.png')
playerX = 160
playerY = 500
playerX_change = 0
playerY_change = 0

# fruit
fruitImg = pygame.image.load('fruit.png')
fruitX = random.randint(0,400)
fruitY = 0
fruitX_change = fruitX + 10
fruitY_change = fruitY + 10
speed = 0.2

def show_Score(x,y):
    score = font.render("score :"+ str(score_value),True,(0,0,0))
    screen.blit(score, (x , y))


def player(x,y):
    screen.blit(playerImg,(x,y))


def img_fruit():
    screen.blit(fruitImg,(fruitX,fruitY))


def update_fruit():
    global fruitY , fruitY_change ,fruitX_change ,fruitX , score_value , speed
    fruitY += speed
    if score_value > 10 and score_value <= 20:
        speed = 0.4
    if score_value > 20 and score_value <= 30:
        speed = 0.6
    if score_value > 30 and score_value <= 37:
        speed = 0.8
    if score_value > 38 and score_value <=49:
        speed = 1.2
    if score_value >= 50:
        speed = 1.5
    if fruitY >= 436:
        fruitX = random.randint(0,400)
        fruitY = 0

def collide(playerX , playerY , fruitX , fruitY):
    distance = math.sqrt((math.pow(playerX-fruitX , 2)) + (math.pow(playerY-fruitY, 2)))
    if distance < 36:
        return True
    else:
        return False

def game_over():
    if fruitY >= 435:
        over_text = over_font.render("GAME OVER",True,(0,0,0))
        screen.blit(over_text, (30 , 70))
        time.sleep(1)

running =True
while running:

    # filling black color 
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    # loop for display the screen untill user press quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # keystroke
        if event.type == pygame.KEYDOWN:
                # for x axis
                if event.key == pygame.K_LEFT:
                    playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    playerX_change = 1

                # for y axis 
                if event.key == pygame.K_UP:
                    playerY_change = 1
                if event.key == pygame.K_DOWN:
                    playerY_change = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    # plyar movement in x direction 
    playerX += playerX_change
    playerY -= playerY_change


    # collision
    collision = collide(playerX , playerY , fruitX , fruitY)
    if collision:
        music = pygame.mixer.Sound((r'music1.wav'))
        music.play()
        update_fruit()
        score_value += 1 
        fruitX = random.randint(0,400)
        fruitY = 0
       
    # boundry for the player
    # x axis
    if playerX <=0:
        playerX = 0
    elif playerX >= 336:
        playerX = 336
    # y axis
    if playerY <=0:
        playerY = 0
    elif playerY >= 436:
        playerY = 436

    # border for fruit
    if fruitX <=0:
        fruitX = 0
    elif fruitX >= 336:
        fruitX = 336
    if fruitY <=0:
        fruitY = 0
    elif fruitY >= 436:
        fruitY = 436

    # game over                       
    if fruitY >= 435:
        game_over()
        break

    img_fruit()
    update_fruit()
    player(playerX,playerY)
    show_Score(textX,textY)
    collide(playerX , playerY , fruitX , fruitY)
    pygame.display.update()  # updating the loop