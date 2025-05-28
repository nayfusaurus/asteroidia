import pygame
import circleshape as cs
from constants import SHOT_RADIUS


class Shot(cs.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)