from main_game.alphabet_soup.alphasoup import AlphabetSoup
from main_game.parser.file_parser import FileParser


class Game:
    def __init__(self):
        pass

    def solve_alphabet_soup(self, game):
        palabras, tablero = FileParser(game).content()
        return AlphabetSoup(palabras, tablero).solve()
