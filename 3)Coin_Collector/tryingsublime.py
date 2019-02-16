from random import randint
import time




WIDTH = 1000
HEIGHT = 800


score = 0
game_over = False
coin_grab = False   #used to reset timer after picking up a coin
speed = 2
clock_time = 5
color = "green"




fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200




def draw():

    screen.fill(color)
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color = "black", topleft=(10,10))


    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft = (10,10), fontsize = 60)

def change_color():
    global color

    x = randint(1,10)
    if x == 1:
        color = "red"
    elif x == 2:
        color = "yellow"
    elif x == 3:
        color = "orange"
    elif x == 4:
        color = "black"
    elif x == 5:
        color = "blue"
    elif x == 6:
        color = "green"
    elif x == 7:
        color = "white"
    elif x == 8:
        color = "purple"
    elif x == 9:
        color = "gold"
    elif x == 10:
        color = "grey"
    



    

def place_coin():
    coin.x = randint(20, (WIDTH - 20))      # within 20 pixles of the box
    coin.y = randint(20, (HEIGHT -20))



def time_up():
    global game_over        #Need to call global to get the boolean at the beginning
    global coin_grab

    if coin_grab == False:
        game_over = True
    elif coin_grab == True:
        coin_grab = False
        run_game()


def update():

    global score
    global coin_grab
    global speed
    global color
    
    if keyboard.up and keyboard.left:
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
        time_up()
    if fox.y <= 0 or fox.y >= 800:
        game_over = True
        time_up()

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        coin_grab = True
        speed = speed + 0.1 #when the fox picks up a coin, he gets a little faster
        score = score + 10
        if score % 100 == 0:
                change_color()

        if speed > 15:
            clock_time = 0.5
        elif speed > 10:
            clock_time = 1.0
        elif speed > 5:
            clock_time = 2.0
        elif speed > 4:
            clock_time = 2.5
        elif speed > 3:
            clock_time = 3.5

        place_coin()


def run_game():

    clock.schedule(time_up, 4)    #After 7 seconds, it will call the time_up funtion




  

run_game()



