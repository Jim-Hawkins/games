from main_game.main import Game

n = Game()
results = n.solve_alphabet_soup("ms_as_001.txt")
for i in results:
    print(i)
