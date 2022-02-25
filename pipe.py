from enum import Enum

from pygame.sprite import AbstractGroup

from core.artefacts import Artefact


class PipeType(Enum):
    BOTTOM = 1
    TOP = 2


class Pipe(Artefact):

    def __init__(self, pipe_type=PipeType.BOTTOM, pos_x=0, pos_y=0, *groups: AbstractGroup):
        self._file_name = "assets/pipe{}.png"
        super().__init__(self._file_name.format(pipe_type.value), pos_x, pos_y, *groups)

    def update(self):
        self._move()

    def _move(self):
        self.rect[0] -= 2
        if self.rect[0] <= -100:
            self.kill()
