import pygame
import random

from pygame.transform import rotate
import circleshape as cs
from constants import ASTEROID_MIN_RADIUS

class Asteroid(cs.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2