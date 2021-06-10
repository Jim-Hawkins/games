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
            with open(GAME_FILES + self.__file, encoding="UTF-8") as file:
                for line in file:
                    data.append(line)
        except FileNotFoundError:
            raise GameException("Game file {} not found".format(self.__file))

        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')

        return data

    def __validate_file(self):
        self.check_empty_file()
        index = 0
        while self.__content[index] != ".":       # examine the words
            self.check_len(index)
            self.check_alphabetic(index)
            index += 1
            self.check_overflow(index)

        self.check_no_words(index)
        index += 1         # index is currently in the line of the separator, so we increase it by 1
        self.check_no_table(index)

        reference = index                # reference will be used to check consistency of the board
        while index < len(self.__content):  # examine board until the end of the list _content
            self.check_consistency(index, reference)
            self.check_alphabetic(index)
            index += 1

    def check_no_table(self, index):
        """check case there is no table"""
        if len(self.__content) == index:
            raise GameException("Incorrect format. No table found.")

    def check_no_words(self, index):
        """check case no words were found"""
        if index == 0:
            raise GameException("Wordlist must contain at least one word.")

    def check_overflow(self, index):
        """check case no point was found and iter is out of bounds"""
        if index >= len(self.__content):
            raise GameException("Incorrect format. Game file corrupted.")

    def check_empty_file(self):
        """check case the file is empty"""
        if len(self.__content) == 0:
            raise GameException("Incorrect format. Game file corrupted.")

    def check_consistency(self, current, reference):
        """check that all lines in the table have the same length"""
        if len(self.__content[current]) != len(self.__content[reference]):
            raise GameException("Incorrect table format.")

    def check_alphabetic(self, index):
        """check all characters are alphabetic"""
        if not self.__content[index].isalpha():
            raise GameException("Incorrect format. Game file corrupted.")

    def check_len(self, index):
        """check that words have at least length 2"""
        if len(self.__content[index]) < 2:
            raise GameException("Search words must be at least two letters long.")

    def content(self):
        """return a list of words and a matrix for the table from __content"""
        words = []
        board = []
        index = 0
        while self.__content[index] != ".":
            new_word = self.__content[index].upper()
            if new_word not in words:  # avoid repeating words
                words.append(new_word)
            index += 1

        index += 1
        while index < len(self.__content):
            board.append(self.__content[index].upper())
            index += 1

        return words, board
