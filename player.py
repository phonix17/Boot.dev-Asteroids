import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot

class player(CircleShape):
    def __init__(self, x, y): # Create player object using Circle class as base; PLAYER_RADIUS comes from constants.py
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    reload = 0

    def triangle(self): # Method taken from  boot.dev https://www.boot.dev/lessons/c504a055-69b9-49a9-a9cf-40a30556af92
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): # Override of method from Circle class
            pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt): # Defines rotation amount of the player using the DeltaTime and constant turn speed
         self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt): # Allows forward/backward motion based on current rotation; vector math provided courtesy of Boot.dev https://www.boot.dev/lessons/f3c2de4d-3646-42c0-8639-71f0c4c01eaa
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt): # Creates a bullet coming from player facing
        if self.reload > 0:
            return
        fired_shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        fired_shot.velocity += forward * PLAYER_SPEED * dt * PLAYER_SHOOT_SPEED
        self.reload = PLAYER_SHOT_COOLDOWN

    def update(self, dt): # Moves player object if WASD pressed or shoots if SPACE is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # Rotate left when "a" pressed
            self.rotate(0 - dt)
        if keys[pygame.K_d]: # Rotate right when "d" pressed
            self.rotate(dt)
        if keys[pygame.K_w]: # Rotate forward when "w" pressed
            self.move(dt)
        if keys[pygame.K_s]: # Rotate backward when "d" pressed
            self.move(0 - dt)
        if keys[pygame.K_SPACE]: # Create shot when space pressed
            self.shoot(dt)
        self.reload -= dt