from main_game.alphabet_soup.alphasoup import AlphabetSoup
from main_game.cfg.games_cfg import GAME_FILES


class Game:
    def __init__(self):
        self.variable = 0

    def solve_alphabet_soup(self, game):
        self.variable = 1
        line = ''
        palabras = []
        tablero = []
        with open(GAME_FILES + game) as file:
            while line != ".":
                line = file.readline()[:-1]
                if line != ".":
                    palabras.append(line)

            while line != '':
                line = file.readline()[:-1]
                if line != '':
                    tablero.append(line)

        AlphabetSoup(tablero, palabras).solve()


n = Game()
n.solve_alphabet_soup("sopa1.txt")
