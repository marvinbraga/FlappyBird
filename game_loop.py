from core.abstract_game_loop import AbstractGameLoop
from game import Game


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = Game()

    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def check_keys(self, event):
        pass

    def check_events(self, event):
        pass
