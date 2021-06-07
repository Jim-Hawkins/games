from main_game.alphabet_soup.alphasoup import AlphabetSoup
from main_game.parser.file_parser import FileParser
from main_game.cfg.games_cfg import GAME_FILES
from main_game.exceptions.game_exception import GameException


class Game:
    def __init__(self):
        self.variable = 0

    def solve_alphabet_soup(self, game):
        self.variable = 1
        palabras, tablero = FileParser(game).content()

        AlphabetSoup(tablero, palabras).solve()


# n = Game()
# n.solve_alphabet_soup("ce_as_001.txt")
