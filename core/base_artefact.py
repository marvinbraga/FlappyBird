from abc import ABCMeta

import pygame
from pygame.sprite import AbstractGroup


class BaseArtefact(pygame.sprite.Sprite):

    def __init__(self, image, pos_x=0, pos_y=0, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos_x
        self.rect[1] = pos_y

    def draw(self, window):
        return self
