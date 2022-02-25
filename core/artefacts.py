import pygame
from pygame.sprite import AbstractGroup

from core.base_artefact import BaseArtefact
from core.animated_artefacts import AnimatedArtefact


class Artefact(BaseArtefact):

    def __init__(self, image, pos_x=0, pos_y=0, *groups: AbstractGroup):
        super().__init__(image, pos_x, pos_y, *groups)
