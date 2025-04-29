#!/usr/bin/env python3
import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = (
            pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        )
        a = self.position + forward * self.radius  # pyright: ignore
        b = self.position - forward * self.radius - right  # pyright: ignore
        c = self.position - forward * self.radius + right  # pyright: ignore
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            screen, "white", self.triangle(), 2  # pyright: ignore
        )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        # Make a unit vector pointing straight up (0, 0) -> (0, 1)
        # Then rotate the unit vector in the direction of the player
        forward_vector = pygame.Vector2(0, 1).rotate(self.rotation)

        # Adjust player speed and move the player
        self.position += forward_vector * PLAYER_SPEED * dt
