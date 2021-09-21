# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 08:06:11 2021

@author: DELL
"""

#Import the pygame library and initialise the game engine
import pygame
from random import randint

#Let's import the Paddle Class & the Ball Class
from paddle import Paddle
from ball import Ball
from brick import Brick

BLACK = (0, 0, 0)

## Paddle, Ball, Brick
"""
class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the ball, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)


class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700:               # scree size - paddle length
          self.rect.x = 700
"""

pygame.init()

# Define some colors
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

score = 0
lives = 3

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

#Create the Paddle
paddle = Paddle(ORANGE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 580

bullets = []
bullet = Paddle(ORANGE, 10, 10)

#Create the ball sprite
ball = Ball(WHITE, 10, 10)
ball.rect.x = randint(100, 600)
ball.rect.y = randint(100, 500)

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add the paddle to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_sprites_list.add(bullet)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Time counter for brick falling
time_counter = 0

brick_fall = pygame.USEREVENT + 1
set_timer = pygame.USEREVENT + 2
pygame.time.set_timer(brick_fall, 5000)
pygame.time.set_timer(set_timer, 1000)


class Unit():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300    

    def fire(self):
        # fire gun, only if cooldown has been 0.3 seconds since last
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    """
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
              carryOn = False  # Flag that we are done so we exit this loop
    
    for e in pygame.event.get():
        time_counter = clock.get_time()
        print("t",time_counter)
        if e.type == brick_fall:
            print("Hello")
            for brick in all_bricks:
                brick.rect.y += 5
    """
    time_counter = clock.get_time()
    #print("t", time_counter)
    if time_counter % 3000 == 0:
        print(time_counter)
        for brick in all_bricks:
            brick.rect.y += 5
        time_counter = 0
    #for brick in all_bricks:
        #brick.rect.y += 1
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop
            
        if e.type == pygame.MOUSEBUTTONUP:
            #print("hello mouse")
            last = pygame.time.get_ticks()
            #if now - last >= 300:
            now = pygame.time.get_ticks()
            last = now
            bullet = Paddle(ORANGE, 10, 10)
            all_sprites_list.add(bullet)
            bullet.rect.x = paddle.rect.x
            bullet.rect.y = paddle.rect.y
            bullets.append(bullet)
        if e.type == brick_fall:
            for brick in all_bricks:
                brick.rect.y += 5

    #Moving the paddle when the use uses the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # --- Game logic should go here
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            #Display Game Over Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Stop the Game
            carryOn = False

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks) == 0:
          #Display Level Complete Message for 3 seconds
          font = pygame.font.Font(None, 74)
          text = font.render("LEVEL COMPLETE", 1, WHITE)
          screen.blit(text, (200, 300))
          pygame.display.flip()
          pygame.time.wait(3000)

          #Stop the Game
          carryOn = False
    #Check if there is the ball collides with any of bullets
    for bullet in bullets:

        brick_collision_list = pygame.sprite.spritecollide(
            bullet, all_bricks, False)
        #print("bullets",brick_collision_list)
        for brick in brick_collision_list:
          #ball.bounce()
          score += 1
          brick.kill()
          bullet.kill()
          bullets.remove(bullet)
          if len(all_bricks) == 0:
              #Display Level Complete Message for 3 seconds
              font = pygame.font.Font(None, 74)
              text = font.render("LEVEL COMPLETE", 1, WHITE)
              screen.blit(text, (200, 300))
              pygame.display.flip()
              pygame.time.wait(3000)

              #Stop the Game
              carryOn = False
    #------Brick falling down ---------

    for bullet in bullets:
        bullet.rect.y -= 1
    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650, 10))

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(45)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
