class AlphabetSoup:
    def __init__(self, table, words):
        """ 8 possible values for self.dir:
        1 2 3
        4 w 5
        6 7 8
        """
        self.table = table
        self.words = words
        self.height = len(self.table)
        self.width = len(self.table[0])
        self.dir = 0

    def solve(self):
        for w in self.words:
            found = False
            for i in range(self.height):
                if found: break     # if word was found, do not keep looking
                for j in range(self.width):
                    if found: break     # if word was found, do not keep looking
                    result = self.explore_word(w, i, j)
                    if result is not None:
                        print("Palabra {} encontrada entre ({}, {}) y ({}, {}).".format(w, i, j, result[0], result[1]))
                        found = True

            if not found: print("Palabra {} no encontrada.".format(w))

    def explore_word(self, word, row, col):
        """ method to analyze if the letter (row, col) begins word"""
        # first of all, check if table[row][col] equals our word's first letter
        if word[0] != self.table[row][col]: return None
        # get the direction to explore the word
        self.dir = self.get_dir(word, row, col)
        if self.dir is None: return None
        for i in range(1, len(word)):
            # get the next coords counting from (row, col)
            row, col = self.get_next_index(row, col)
            # stop seeking if the ith letter is different from the selected one in the table
            # or if (row, col) is outside the table
            try:
                if word[i] != self.table[row][col]:
                    return None
            except IndexError:
                return None
        # if we reach the end of the word, return its finish coords
        return row, col

    def get_dir(self, word, row, col):
        try:
            if self.table[row - 1][col - 1] == word[1]: return 1
        except IndexError:
            return None
        try:
            if self.table[row - 1][col] == word[1]: return 2
        except IndexError:
            return None
        try:
            if self.table[row - 1][col + 1] == word[1]: return 3
        except IndexError:
            return None
        try:
            if self.table[row][col - 1] == word[1]: return 4
        except IndexError:
            return None
        try:
            if self.table[row][col + 1] == word[1]: return 5
        except IndexError:
            return None
        try:
            if self.table[row + 1][col - 1] == word[1]: return 6
        except IndexError:
            return None
        try:
            if self.table[row + 1][col] == word[1]: return 7
        except IndexError:
            return None
        try:
            if self.table[row + 1][col + 1] == word[1]: return 8
        except IndexError:
            return None

    def get_next_index(self, row, col):
        if 1 == self.dir: return row - 1, col - 1
        if 2 == self.dir: return row - 1, col
        if 3 == self.dir: return row - 1, col + 1
        if 4 == self.dir: return row, col - 1
        if 5 == self.dir: return row, col + 1
        if 6 == self.dir: return row + 1, col - 1
        if 7 == self.dir: return row + 1, col
        if 8 == self.dir: return row + 1, col + 1
