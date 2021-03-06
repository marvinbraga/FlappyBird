import random

import pygame.sprite

from bird import Bird
from coin import Coin
from core import settings
from core.artefacts import Artefact
from core.text import Text
from pipe import Pipe, PipeType


class Game:

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.all_pipes = pygame.sprite.Group()
        self.all_coins = pygame.sprite.Group()
        self.all_birds = pygame.sprite.Group()
        self.background1 = Artefact("assets/sky.png", 0, 0, self.all_sprites)
        self.background2 = Artefact("assets/sky.png", 360, 0, self.all_sprites)
        self.ground1 = Artefact("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Artefact("assets/ground.png", 360, 480, self.all_sprites)
        self.bird = Bird(50, 320, self.all_sprites, self.all_birds)

        self.score_shadow = Text("0", 100, color=(35, 103, 125))
        self.score = Text("0", 100, color=(255, 255, 255))
        self.finished = False
        self.create_pipes()
        self.ticks = 0
        self._base_pos = 300

        self.change_scene = False

    def create_pipes(self):
        self._base_pos = random.randrange(300, 450)
        Pipe(PipeType.BOTTOM, 360, self._base_pos, self.all_sprites, self.all_pipes),
        Pipe(PipeType.TOP, 360, self._base_pos - 550, self.all_sprites, self.all_pipes)
        self.create_coin()

    def create_coin(self):
        Coin(388, self._base_pos - 120, self.all_sprites, self.all_coins)

    def draw(self, window):
        self.all_sprites.draw(window)
        self.score_shadow.draw(window, 173, 23)
        self.score.draw(window, 170, 20)

    def update(self):
        self.move_artefact(self.background1, self.background2, 1)
        self.move_artefact(self.ground1, self.ground2, 2)
        self.spawn_pipes()
        self.check(
            self.bird.check_collide(self.all_pipes),
            self.bird.check_collide(self.all_coins, True)
        )
        self.score.update(str(self.bird.points))
        self.score_shadow.update(str(self.bird.points))
        self.all_sprites.update()

    def check(self, is_pipe_collide, is_coin_collide):
        if is_pipe_collide:
            self.bird.power -= 1
            print(f"Chance: {self.bird.power}")
        if is_coin_collide:
            self.bird.points += 1
            print(f"Pontos: {self.bird.points}")
        self.finished = not self.bird.is_alive

    def move_artefact(self, artefact1, artefact2, velocity):
        artefact1.rect[0] = 0 if artefact1.rect[0] <= -360 else artefact1.rect[0] - velocity
        artefact2.rect[0] = 360 if artefact2.rect[0] <= 0 else artefact2.rect[0] - velocity
        return self

    def spawn_pipes(self):
        self.ticks = 0 if self.ticks >= random.randrange(4, 5) * settings.FPS else self.ticks + 1
        if not self.ticks:
            self.create_pipes()
