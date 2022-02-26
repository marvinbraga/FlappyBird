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
        self.power = 1
        self.is_alive = True
        self.points = 0
        
    def update(self, *args):
        self.is_alive = self.power > 0
        self.animate()
        self.move()
    
    def animate(self):
        if self.is_alive:
            self.ticks = (self.ticks + 1) % 4
            self.image = pygame.image.load(self.file_name.format(self.ticks))

    def move(self):
        ground = 440
        velocity = 20
        if self.is_alive:
            key = pygame.key.get_pressed()
            self.velocity += self.gravity
            self.rect[1] += self.velocity

            if self.velocity >= velocity:
                self.velocity = velocity

            if key[pygame.K_SPACE]:
                self.velocity -= 5
        else:
            self.velocity += self.gravity
            self.rect[1] += self.velocity
            self.rect[0] -= 2

        if self.rect[1] >= ground:
            self.rect[1] = ground
        if self.rect[1] <= 0:
            self.rect[1] = 0
            self.velocity = 4

    def check_collide(self, group, kill=False):
        is_collide = False
        if self.is_alive:
            is_collide = pygame.sprite.spritecollide(self, group, kill)
        return is_collide
