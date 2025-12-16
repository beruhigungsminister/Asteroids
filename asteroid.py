import pygame
from circleshape import CircleShape
import constants
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        splitting_angle = random.uniform(20, 50)
        asteroid1_vector = self.velocity.rotate(splitting_angle)
        asteroid2_vector = self.velocity.rotate(-splitting_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = 1.2 * asteroid1_vector
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = 1.2 * asteroid2_vector