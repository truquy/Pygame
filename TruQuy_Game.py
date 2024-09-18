# Pygame Project
# Tru Quy
# ProLang
# 09/17/2024

import pygame
import sys

class Game:

    def __init__(self):
    

        # Initialize pygame
        pygame.init()

        # Set screen resolution
        screen_res = (640, 480)
        self.screen = pygame.display.set_mode(screen_res)
        pygame.display.set_caption('Tru Quy\'s Game')
        self.clock = pygame.time.Clock()

        # Load image and set color
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0,0,0))

        # Set position of image on screen
        self.img_pos = [160, 260]

        # Set movement of image with keyboard
        self.movement = [False, False]

        # Set collision area for the image
        self.collision_area = pygame.Rect(50, 50, 300, 50)  # Create a rectangle for collision detection

    def run(self):
        # Game loop
        # This will run until the user decides to quit
        # It will update the screen, check for events, and limit the frame rate to 60 frames per seconddel
        while True:
            # Set screen background to green color (Red, Green, Blue) (255,255,255)
            self.screen.fill((0, 0, 0))
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (255, 255, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), self.collision_area)
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the user clicked the close button, exit the game
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False


            # Update movement
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            # Place image on screen
            self.screen.blit(self.img, self.img_pos)  # Place the image at (100, 200) coordinates on the screen    
            
            # Update the display
            pygame.display.update()

            # Limit the frame rate to 60 frames per second
            self.clock.tick(60)
        
Game().run()                              