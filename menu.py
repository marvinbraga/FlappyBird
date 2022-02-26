import pygame
from pygame.sprite import AbstractGroup

from core.artefacts import Artefact
from core.text import Text
from score_data import ScoreData


class Menu:

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

        self.background1 = Artefact("assets/sky.png", 0, 0, self.all_sprites)
        self.background2 = Artefact("assets/sky.png", 360, 0, self.all_sprites)
        self.ground1 = Artefact("assets/ground.png", 0, 480, self.all_sprites)
        self.ground2 = Artefact("assets/ground.png", 360, 480, self.all_sprites)

        self.get_ready = Artefact("assets/getready.png", 60, 100, self.all_sprites)
        self.table_score = Artefact("assets/score.png", 25, 180, self.all_sprites)
        self.button_go = Artefact("assets/go.png", 100, 400, self.all_sprites)

        self.change_scene = False
        self.valid_keys = [pygame.K_SPACE]
        self.max_score = ScoreData.load()
        self.score = Text("0", 100, color=(255, 255, 255))
        self.score_shadow = Text("0", 100, color=(125, 101, 35))

    def set_score(self, value):
        if value > self.max_score:
            self.max_score = value
            ScoreData.save(value)
            self.score.update(str(self.max_score))
            self.score_shadow.update(str(self.max_score))

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_go.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True

    def check_keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_scene = True

    def draw(self, window):
        self.all_sprites.draw(window)
        self.score_shadow.draw(window, 173, 253)
        self.score.draw(window, 170, 250)

    def update(self):
        self.move_artefact(self.background1, self.background2, 1)
        self.move_artefact(self.ground1, self.ground2, 2)
        self.score.update(str(self.max_score))
        self.score_shadow.update(str(self.max_score))
        self.all_sprites.update()

    def move_artefact(self, artefact1, artefact2, velocity):
        artefact1.rect[0] = 0 if artefact1.rect[0] <= -360 else artefact1.rect[0] - velocity
        artefact2.rect[0] = 360 if artefact2.rect[0] <= 0 else artefact2.rect[0] - velocity
        return self
