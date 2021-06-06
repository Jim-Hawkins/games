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
                    if w[0] == self.table[i][j]:
                        result = self.explore_word(w, i, j)
                        if result is not None:
                            print("Palabra {} encontrada entre ({}, {}) y ({}, {}).".format(w, i, j, result[0], result[1]))
                            found = True

            if not found: print("Palabra {} no encontrada.".format(w))

    def explore_word(self, word, row, col):
        self.dir = self.get_dir(word, row, col)
        # print("self.dir ", self.dir)
        for i in range(1, len(word)):
            result = self.get_next_index(row, col)
            if result is None:
                return result
            row, col = result
            # print("row, col, i ", row, col, i)
            try:
                if word[i] != self.table[row][col]:
                    return None
            except IndexError:
                return None
        return row, col

    def get_dir(self, word, row, col):
        try:
            if self.table[row - 1][col - 1] == word[1]: return 1
        except IndexError:
            pass
        try:
            if self.table[row - 1][col]     == word[1]: return 2
        except IndexError:
            pass
        try:
            if self.table[row - 1][col + 1] == word[1]: return 3
        except IndexError:
            pass
        try:
            if self.table[row][col - 1]     == word[1]: return 4
        except IndexError:
            pass
        try:
            if self.table[row][col + 1]     == word[1]: return 5
        except IndexError:
            pass
        try:
            if self.table[row + 1][col - 1] == word[1]: return 6
        except IndexError:
            pass
        try:
            if self.table[row + 1][col]     == word[1]: return 7
        except IndexError:
            pass
        try:
            if self.table[row + 1][col + 1] == word[1]: return 8
        except IndexError:
            pass

    def get_next_index(self, row, col):
        if 1 == self.dir: return row - 1, col - 1
        if 2 == self.dir: return row - 1, col
        if 3 == self.dir: return row - 1, col + 1
        if 4 == self.dir: return row, col - 1
        if 5 == self.dir: return row, col + 1
        if 6 == self.dir: return row + 1, col - 1
        if 7 == self.dir: return row + 1, col
        if 8 == self.dir: return row + 1, col + 1


tablero = [["A", "G", "U", "A"],
           ["P", "I", "R", "T"],
           ["N", "A", "R", "F"],
           ["X", "Q", "S", "E"]]
palabras = ["AIRE", "AGUA", "TIERRA"]
AlphabetSoup(tablero, palabras).solve()
