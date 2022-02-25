import random

import pygame.sprite

from core import settings
from core.artefacts import Artefact
from pipe import Pipe, PipeType


class Game:

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.background1 = Artefact("assets/sky.png", 0, 0, self.all_sprites)
        self.background2 = Artefact("assets/sky.png", 360, 0, self.all_sprites)
        self.ground1 = Artefact("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Artefact("assets/ground.png", 360, 480, self.all_sprites)

        self.pipes = []
        self.create_pipes()
        self.ticks = 0

    def create_pipes(self):
        pos = random.randrange(300, 450)
        self.pipes += [
            Pipe(PipeType.BOTTOM, 360, pos, self.all_sprites),
            Pipe(PipeType.TOP, 360, pos - 550, self.all_sprites)
        ]

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.move_artefact(self.background1, self.background2, 1)
        self.move_artefact(self.ground1, self.ground2, 2)
        self.spawn_pipes()
        self.all_sprites.update()

    def move_artefact(self, artefact1, artefact2, velocity):
        artefact1.rect[0] = 0 if artefact1.rect[0] <= -360 else artefact1.rect[0] - velocity
        artefact2.rect[0] = 360 if artefact2.rect[0] <= 0 else artefact2.rect[0] - velocity
        return self

    def spawn_pipes(self):
        self.ticks = 0 if self.ticks >= random.randrange(4, 5) * settings.FPS else self.ticks + 1
        if not self.ticks:
            self.create_pipes()
