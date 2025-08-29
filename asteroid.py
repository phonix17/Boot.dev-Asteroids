import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        first_child_vector = pygame.math.Vector2.rotate(self.velocity, new_angle)
        second_child_vector = pygame.math.Vector2.rotate(self.velocity, -new_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        first_child_asteroid = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        second_child_asteroid = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        first_child_asteroid.velocity = first_child_vector * 1.2
        second_child_asteroid.velocity = second_child_vector * 1.2