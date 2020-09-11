from random import randint

apple = Actor("apple")

global score
score = 0


def draw():
    screen.clear()
    apple.draw()
    


def place_apple():
    apple.x = randint(10,750)
    apple.y = randint(10,600)


def on_mouse_down(pos):
    global score
    
    if apple.collidepoint(pos):
        print("Good shot!")
        score = score + 1
        place_apple()

  
    else:
        print("You missed! Game over")
        print("Your final score is:")
        print(score)
        quit()

