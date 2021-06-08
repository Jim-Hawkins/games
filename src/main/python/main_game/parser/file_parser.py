""" Parser to adapt and check the input for the game solver"""

from main_game.cfg.games_cfg import GAME_FILES
from main_game.exceptions.game_exception import GameException


class FileParser:
    """ Class that implements a parser"""
    def __init__(self, game_file):
        self._file = game_file
        self._content = self._parse_file()
        self._validate_file()

    def _parse_file(self):
        try:
            with open(GAME_FILES + self._file) as file:
                data = file.readlines()
        except FileNotFoundError:
            raise GameException("Game file {} not found".format(self._file))

        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')
        return data

    def _validate_file(self):
        iter = 0
        while self._content[iter] != ".":       # examine the words
            if len(self._content[iter]) < 2:
                raise GameException("Search words must be at least two letters long.")
            if not self._content[iter].isalpha():
                raise GameException("Incorrect format. Game file corrupted.")

            iter += 1
            if iter >= len(self._content):      # no point was found and iter is out of bounds
                raise GameException("Incorrect format. Game file corrupted.")

        iter += 1           # iter is currently in the line of the separator, so we increase it by 1
        reference = iter                  # reference will be used to check consistency of the board
        while iter < len(self._content):  # examine board until the end of the list _content
            if len(self._content[iter]) != len(self._content[reference]):
                raise GameException("Incorrect table format.")
            if not self._content[iter].isalpha():
                raise GameException("Incorrect format. Game file corrupted.")

            iter += 1

    def content(self):
        words = []
        board = []
        iter = 0
        while self._content[iter] != ".":
            words.append(self._content[iter].upper())
            iter += 1

        iter += 1
        while iter < len(self._content):
            board.append(self._content[iter].upper())
            iter += 1

        return words, board
