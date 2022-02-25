import pygame
from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class Bird(Artefact):

    def __init__(self, x, y, *groups: AbstractGroup):
        self.file_name = "assets/bird{}.png"
        super().__init__(self.file_name.format(0), x, y, *groups)
        self.ticks = 0
        self.velocity = 4
        self.gravity = 1
        
    def update(self, *args):
        self.animate()
        self.move()
    
    def animate(self):
        self.ticks = (self.ticks + 1) % 4
        self.image = pygame.image.load(self.file_name.format(self.ticks))        

    def move(self):
        ground = 440
        velocity = 15

        key = pygame.key.get_pressed()
        self.velocity += self.gravity
        self.rect[1] += self.velocity

        if self.velocity >= velocity:
            self.velocity = velocity

        if key[pygame.K_SPACE]:
            self.velocity -= 5

        if self.rect[1] >= ground:
            self.rect[1] = ground
        if self.rect[1] <= 0:
            self.rect[1] = 0
            self.velocity = 4
