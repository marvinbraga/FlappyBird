import pygame
from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class Coin(Artefact):

    def __init__(self, x, y, *groups: AbstractGroup):
        self.file_name = "assets/{}.png"
        super().__init__(self.file_name.format(0), x, y, *groups)
        self.ticks = 0

    def update(self, *args):
        self.move()
        self.animate()

    def move(self):
        self.rect[0] -= 2
        if self.rect[0] <= -100:
            self.kill()

    def animate(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load(self.file_name.format(self.ticks))
