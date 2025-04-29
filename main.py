#!/usr/bin/env python3
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()

    # Create a GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Make a pygame Clock object
    game_clock = pygame.time.Clock()

    # Make a delta time variable for the game
    dt = 0

    # Make groups for game objects
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set groups as containers for game objects
    Player.containers = (updatables, drawables)  # pyright: ignore
    Asteroid.containers = (asteroids, updatables, drawables)  # pyright: ignore
    AsteroidField.containers = (updatables,)  # pyright: ignore

    # Instantiate game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Start a game loop
    while True:
        # Exit the game loop if the user has closed the window
        # It will make the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Call `.update()` method on updatables
        updatables.update(dt)

        # Draw drawables individually
        for thing in drawables:
            thing.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
