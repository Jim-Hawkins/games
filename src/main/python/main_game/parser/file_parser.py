""" Parser to adapt and check the input for the game solver"""

from main_game.cfg.games_cfg import GAME_FILES
from main_game.exceptions.game_exception import GameException


class FileParser:
    """ Class that implements a parser"""
    def __init__(self, game_file):
        self.__file = game_file
        self.__content = self.__parse_file()
        self.__validate_file()

    def __parse_file(self):
        data = []
        try:
            with open(GAME_FILES + self.__file) as file:
                for line in file:
                    line = line.replace("Ã‘", "Ñ")  # python reading does weird things with Ñ
                    line = line.replace("Ã±", "Ñ")
                    data.append(line)
        except FileNotFoundError:
            raise GameException("Game file {} not found".format(self.__file))

        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')

        return data

    def __validate_file(self):
        if len(self.__content) == 0:
            raise GameException("Incorrect format. Game file corrupted.")

        iter = 0
        while self.__content[iter] != ".":       # examine the words
            if len(self.__content[iter]) < 2:
                raise GameException("Search words must be at least two letters long.")
            # the second check is important for spanish speakers
            if not self.__content[iter].isalpha() and "Ñ" not in self.__content[iter]:
                print(self.__content[iter], not self.__content[iter].isalpha(), "Ñ" not in self.__content[iter])
                raise GameException("Incorrect format. Game file corrupted.")

            iter += 1
            if iter >= len(self.__content):      # no point was found and iter is out of bounds
                raise GameException("Incorrect format. Game file corrupted.")

        # in case no words were found
        if 0 == iter:
            raise GameException("Wordlist must contain at least one word.")

        iter += 1           # iter is currently in the line of the separator, so we increase it by 1

        # in case there is no table
        if len(self.__content) == iter:
            raise GameException("Incorrect format. No table found.")

        reference = iter                  # reference will be used to check consistency of the board
        while iter < len(self.__content):  # examine board until the end of the list _content
            if len(self.__content[iter]) != len(self.__content[reference]):
                raise GameException("Incorrect table format.")
            # the second check is important for spanish speakers
            if not self.__content[iter].isalpha() and "Ñ" not in self.__content[iter]:
                raise GameException("Incorrect format. Game file corrupted.")

            iter += 1

    def content(self):
        words = []
        board = []
        iter = 0
        while self.__content[iter] != ".":
            words.append(self.__content[iter].upper())
            iter += 1

        iter += 1
        while iter < len(self.__content):
            board.append(self.__content[iter].upper())
            iter += 1

        return words, board
