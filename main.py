# Import pygame to simplify code
import pygame
# Imports of other project files
from constants import *
def main():
    pygame.init()
    clock = pygame.time.Clock() # Define the clock for later use controlling framerate
    dt = 0 # DeltaTime, used along side the clock
    # Initialization messages, useful for confirming constants
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Use constants to define the play area
    while True: # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Closes the game when the window closes, preventing need to also cancel from the terminal
                return
        screen.fill("black") # Color play area
        pygame.display.flip() # Displays updated state in the play area
        dt = clock.tick(60) / 1000 # Controls framerate and updates the DeltaTime


if __name__ == "__main__": # Run the game only from the launch file, protects from accidently calling in other file
    main()