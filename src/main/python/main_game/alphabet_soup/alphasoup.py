""" Module containing an alphabet soup-solving class"""


class AlphabetSoup:
    """ Class that implements an alphabet soup"""
    def __init__(self, words, table):
        """ 8 possible values for self.dir:
        1 2 3
        4 w 5
        6 7 8
        """
        self.__table = table
        self.__words = words
        self.__height = len(self.__table)
        self.__width = len(self.__table[0])
        self.__directions = []
        self.__results = []

    def solve(self):
        """ Method that implements the algorithm to solve the alphabet soup"""
        for word in self.__words:
            found = False
            for i in range(self.__height):
                if found: break     # if word was found, do not keep looking
                for j in range(self.__width):
                    if found: break     # if word was found, do not keep looking
                    result = self.explore_word(word, i, j)
                    if result is not None:
                        self.__results.append("Palabra {} encontrada entre ({}, {}) y ({}, {})."
                                              .format(word, i, j, result[0], result[1]))
                        found = True

            if not found:
                self.__results.append("Palabra {} no encontrada.".format(word))

        return self.__results

    def explore_word(self, word, row, col):
        """ method to analyze if the letter (row, col) begins word"""
        # first of all, check if table[row][col] equals our word's first letter
        if word[0] != self.__table[row][col]: return None

        # get the directions to explore the word
        self.__directions = self.get_dir(word, row, col)
        if len(self.__directions) == 0: return None

        for candidate in self.__directions:
            # poi (principle of innocence: the word is out there until proved false)
            poi = True
            try_row, try_col = row, col
            for i in range(1, len(word)):
                # get the next coordinates counting from (row, col)
                try_row, try_col = self.get_next_index(candidate, try_row, try_col)
                # stop seeking if the ith letter is different from the selected one in the table
                # or if (row, col) is outside the table (remember that negative indexes are allowed)
                try:
                    if try_row < 0 or try_col < 0 or word[i] != self.__table[try_row][try_col]:
                        poi = False
                        break
                except IndexError:
                    poi = False
                    break
            # if we reach the end of the word, return its finish coordinates
            if poi:
                return try_row, try_col
        # if all candidates are exhausted with no results, return None
        return None

    def get_dir(self, word, row, col):
        """ Fills a list with all candidates to explore.
            If an index is out of bounds, we skip that case and examine
            the next one"""
        possible_dirs = []
        try:
            if row - 1 >= 0 and col - 1 >= 0 and self.__table[row - 1][col - 1] == word[1]:
                possible_dirs.append(1)
        except IndexError:
            pass
        try:
            if row - 1 >= 0 and self.__table[row - 1][col] == word[1]:
                possible_dirs.append(2)
        except IndexError:
            pass
        try:
            if row - 1 >= 0 and self.__table[row - 1][col + 1] == word[1]:
                possible_dirs.append(3)
        except IndexError:
            pass
        try:
            if col - 1 >= 0 and self.__table[row][col - 1] == word[1]:
                possible_dirs.append(4)
        except IndexError:
            pass
        try:
            if self.__table[row][col + 1] == word[1]:
                possible_dirs.append(5)
        except IndexError:
            pass
        try:
            if col - 1 >= 0 and self.__table[row + 1][col - 1] == word[1]:
                possible_dirs.append(6)
        except IndexError:
            pass
        try:
            if self.__table[row + 1][col] == word[1]:
                possible_dirs.append(7)
        except IndexError:
            pass
        try:
            if self.__table[row + 1][col + 1] == word[1]:
                possible_dirs.append(8)
        except IndexError:
            pass
        return possible_dirs

    def get_next_index(self, direction, row, col):
        """ gets the new coordinates from (row, col) based on the value of self.dir:
            1 2 3      for example: if self.dir is 5, keep in the same row and
            4 w 5      advance 1 column
            6 7 8
        """
        if 1 == direction: return row - 1, col - 1
        if 2 == direction: return row - 1, col
        if 3 == direction: return row - 1, col + 1
        if 4 == direction: return row, col - 1
        if 5 == direction: return row, col + 1
        if 6 == direction: return row + 1, col - 1
        if 7 == direction: return row + 1, col
        if 8 == direction: return row + 1, col + 1
