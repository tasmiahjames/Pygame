#Import pygame midule and ranom for random number generator
import pygame 
import random 
import sys

#Initialize the pygame modules to get everything started.
pygame.init() 

#Create a game screen by inserting a width and heigth
screen_width = 1050
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))

#creates the enemies and player characters 
player = pygame.image.load("player1.jpg")
enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("enemy2.png")
enemy3 = pygame.image.load("enemy3.png")
mysterymachine = pygame.image.load("mysterymachine.png")

enemy_list = [enemy1, enemy2, enemy3]
#Get the width and height of the images in order to ensure that the characters stay within the screen size
player = pygame.transform.scale(player, (151, 153))
enemy1 = pygame.transform.scale(enemy1, (312, 312))
enemy2 = pygame.transform.scale(enemy2, (312, 312))
enemy3 = pygame.transform.scale(enemy3, (312, 312))
mysterymachine = pygame.transform.scale(mysterymachine, (435, 201))

player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
mysterymachine_height = mysterymachine.get_height()
mysterymachine_width = mysterymachine.get_width()

#Print out the widths and heights of each character
print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))
print("This is the height of enemy 1 image: " +str(enemy1_height))
print("This is the width of enemy 1 image: " +str(enemy1_width))
print("This is the height of enemy 2 image: " +str(enemy2_height))
print("This is the width of enemy 2 image: " +str(enemy2_width))
print("This is the height of enemy 3 image: " +str(enemy3_height))
print("This is the width of enemy 3 image: " +str(enemy3_width))
print("This is the height of mystery machine image: " +str(mysterymachine_height))
print("This is the width of mystery machine image: " +str(mysterymachine_width))

#Store the positions of the player and enemy as variables so that you can change them later. 
playerXPosition = 100
playerYPosition = 50
enemy1XPosition = 165
enemy1YPosition = 165
enemy2XPosition = 25
enemy2YPosition = 25
enemy3XPosition = 100
enemy3YPosition = 100
mysterymachineXPosition = 50
mysterymachineYPosition = 50

#Make the enemies start off screen and at a random y position.
enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)
enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)
mysterymachineXPosition = screen_width
mysterymachineYPosition = random.randint(0, screen_height - mysterymachine_height)

#Check if the up or down keys are pressed and set it to a boolean value
keyUp= False
keyDown = False
keyLeft = False
keyRight = False

#Loop the game code until the game is closed or ended 
while 1:

    screen.fill(0) #Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(mysterymachine, (mysterymachineXPosition, mysterymachineYPosition))
    
    #This updates the screen with the characters
    pygame.display.flip()
    
    #This loops through events in the game.
    for event in pygame.event.get():
    
        #Checks if the user quits the program and if true it exits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Checks if the user presses key down
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want
            if event.key == pygame.K_UP:
                keyUp = True

            if event.key == pygame.K_DOWN:
                keyDown = True

            if event.key == pygame.K_LEFT:
                keyLeft = True

            if event.key == pygame.K_RIGHT:
                keyRight = True

        # Checks if the key is not up/not pressed
        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want
            if event.key == pygame.K_UP:
                keyUp = False

            if event.key == pygame.K_DOWN:
                keyDown = False

            if event.key == pygame.K_LEFT:
                keyLeft = False

            if event.key == pygame.K_RIGHT:
                keyRight = False

    #Check key pressed values and move player accordingly
    #This keeps the user moving the player off the top of the screen
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
    
    #This makes sure that the user does not move the player below the screen
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1
    
    if keyLeft == True:
        if playerXPosition > 0 :
            playerXPosition -= 1
    
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1

    #Check if the player collides with the enemies by chceking the interaction of the
    #bounding boxes around each character
    
    #Set a bounding box for the player
    playerBounding = pygame.Rect(player.get_rect())
    
    #This makes sure the bounding box stays around the player image
    playerBounding.top = playerYPosition
    playerBounding.left = playerXPosition
    
    #Set a bounding box for the enemies
    enemy1Bounding = pygame.Rect(enemy1.get_rect())
    enemy1Bounding.top = enemy1YPosition
    enemy1Bounding.left = enemy1XPosition
    enemy2Bounding = pygame.Rect(enemy2.get_rect())
    enemy2Bounding.top = enemy2YPosition
    enemy2Bounding.left = enemy2XPosition
    enemy3Bounding = pygame.Rect(enemy3.get_rect())
    enemy3Bounding.top = enemy3YPosition
    enemy3Bounding.left = enemy3XPosition
    mysterymachineBounding = pygame.Rect(mysterymachine.get_rect())
    mysterymachineBounding.top = mysterymachineYPosition
    mysterymachineBounding.left = mysterymachineXPosition

    #Check collision of the boxes
    if playerBounding.colliderect(enemy1Bounding):
        #Print the loss
        print("You lose! :(")
        #Quite the game and exit the window: 
        pygame.quit()
        exit(0)
    elif playerBounding.colliderect(enemy2Bounding):
        print("You lose! :(")
        pygame.quit()
        exit(0)
    elif playerBounding.colliderect(enemy3Bounding):
        print("You lose! :(")
        pygame.quit()
        exit(0)
    elif playerBounding.colliderect(mysterymachineBounding):
        print("You hit the prize object! You win!!")
        pygame.quit()
        exit(0)
        
    #If the enemy is off the screen the user wins the game
    if enemy1XPosition < 0 - enemy1_width and enemy2XPosition < 0 - enemy2_width and enemy3XPosition < 0 - enemy3_width:
        print("You win! YAY!!")
        pygame.quit()
        exit(0)
    
 
    
    #Make enemy approach the player.
    enemy1XPosition -= 0.4000
    enemy2XPosition -= 0.6000
    enemy3XPosition -= 0.8000
    mysterymachineXPosition -= 0.7000
    