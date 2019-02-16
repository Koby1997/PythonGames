from random import randint
import time
import pygame
import math


WIDTH = 1000
HEIGHT = 800


score = 0
game_over = False
speed = 2.0
clock_time = 8
color = "green"


clock_1 = pygame.time.Clock()
seconds = 0.0



fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200



def draw():
    screen.fill(color)
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", fontsize=35, topleft=(10,10))
    screen.draw.text("Time to beat: " + str(round(clock_time,3)), color="black", fontsize=35, topleft=(250,10))
    screen.draw.text("Your time: " + "{}".format(round(seconds,1)), color="black", fontsize=35, topright=(700,10))
    screen.draw.text("Speed: " + str(speed), color="black", fontsize=35, topright=(950,10))

    if game_over == True:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft = (300,400), fontsize = 60)



def change_color(): #sweeeeeeet cool colors
    global color

    x = randint(1,10)   #picks a random color, makes it fun
    if x == 1:
        color = "red"
    elif x == 2:
        color = "yellow"
    elif x == 3:
        color = "orange"
    elif x == 4:
        color = "black" #hard to see time and score, why not make it bonus too
    elif x == 5:
        color = "blue"
    elif x == 6:
        color = "green"
    elif x == 7:
        color = "white"
    elif x == 8:
        color = "purple"
    elif x == 9:
        color = "gold"  #hard to see coin, so perfect, bonus points
    elif x == 10:
        color = "grey"
    



    

def place_coin():
    coin.x = randint(20, (WIDTH - 20))      # within 20 pixles of the box
    coin.y = randint(20, (HEIGHT -20))


def update():

    global score
    global speed
    global color
    global clock_time
    global seconds
    global clock_1
    global game_over
    global speedup_change




    if seconds >= clock_time:   #if you are too slow, you are a loser
        game_over = True
    
    seconds += clock_1.tick_busy_loop()/1000    #each tic is 1 millisecond now



#Movement    
    if keyboard.up and keyboard.left:   #these needed to be added to go diagonally
        fox.x = fox.x - speed
        fox.y = fox.y - speed
        
    elif keyboard.up and keyboard.right:
        fox.x = fox.x + speed
        fox.y = fox.y - speed
        
    elif keyboard.down and keyboard.left:
        fox.x = fox.x - speed
        fox.y = fox.y + speed

    elif keyboard.down and keyboard.right:
        fox.x = fox.x + speed
        fox.y = fox.y + speed
        
    elif keyboard.left:
        fox.x = fox.x - speed
        
    elif keyboard.right:
        fox.x = fox.x + speed

    elif keyboard.up:
        fox.y = fox.y - speed

    elif keyboard.down:
        fox.y = fox.y + speed



    if fox.x <= 0 or fox.x >= 1000:     #if the fox hits the edge of the box, game over
        game_over = True

    if fox.y <= 0 or fox.y >= 800:
        game_over = True





#Things to do if the coin is collected

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        speed = speed + 0.1 #when the fox picks up a coin, he gets a little faster
        seconds = 0         #reset the time


        if color == "black" or color == "gold":    #harder to see coin or time, so extra points!!
            score = score + 50
        else:
            score = score + 10

        if score % 100 == 0:
                change_color()      #why not change color for every 100 points?!




        speedup = math.floor(speed) #round down

        #less time the faster you get

        if speedup > 15:
            clock_time = 1      #lowest time is one second

        elif speedup >= 7:
            clock_time -= 0.025

        elif speedup >= 4:
            clock_time -= 0.05

        elif speedup == 3:
            clock_time = 5

        place_coin()
        speed = round(speed, 2)