#!/usr/bin/env python3
import pygame

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

    # Instantiate a `Player` object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start a game loop
    while True:
        # Exit the game loop if the user has closed the window
        # It will make the window's close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
