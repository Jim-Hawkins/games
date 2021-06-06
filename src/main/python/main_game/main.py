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
                    if len(line) < 2:
                        raise Exception
                    palabras.append(line)

            while line != '':
                line = file.readline()[:-1]
                if line != '':
                    tablero.append(line)

            for i in range(len(tablero)):
                if len(tablero[i]) != len(tablero[0]):      # take first line as reference for length control
                    raise Exception

        AlphabetSoup(tablero, palabras).solve()


# n = Game()
# n.solve_alphabet_soup("sopa1.txt")
