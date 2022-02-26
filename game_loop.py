from core.abstract_game_loop import AbstractGameLoop
from game import Game
from menu import Menu


class GameLoop(AbstractGameLoop):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game = Game()
        self.menu = Menu()
        self._valid_keys += self.menu.valid_keys

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update()
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
            if self.game.finished:
                self.game_restart()

    def game_restart(self):
        self.menu.change_scene = False
        self.menu.set_score(self.game.bird.points)
        del self.game
        self.game = Game()

    def check_keys(self, event):
        self.menu.check_keys(event)

    def check_events(self, event):
        self.menu.events(event)
