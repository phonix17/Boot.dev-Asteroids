# Import pygame to simplify code
import pygame
# Imports of other project files
from constants import *
from circleshape import CircleShape
from player import player
from asteroid import Asteroid
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)

def main():
    pygame.init()
    clock = pygame.time.Clock() # Define the clock for later use controlling framerate
    dt = 0 # DeltaTime, used along side the clock
    Player = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # Create the player object
    field = AsteroidField()
    
    # Initialization messages, useful for confirming setup functioning
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Use constants to define the play area
    
    while True: # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Closes the game when the window closes, preventing need to also cancel from the terminal
                return
        screen.fill("black") # Color play area
        for objects in drawable:
            objects.draw(screen) # Render the player object
        updatable.update(dt) # Updates rotation of player based on pressed keys
        pygame.display.flip() # Displays updated state in the play area
        dt = clock.tick(60) / 1000 # Controls framerate and updates the DeltaTime


if __name__ == "__main__": # Run the game only from the launch file, protects from accidently calling in other file
    main()