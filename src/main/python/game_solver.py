""" Module to allow the user interact with the games with a prompt-like style"""

import argparse
from main_game.main import Game

WELCOME = "Welcome to the ultimate game solver! Type game --help for more information"
USAGE = "game_solver.py [-h] [-p {alphabet_soup,cross_word}] [-t TEMPLATE]\n\
       game_solver.py [-h] [-c TITLE] [-create TITLE]"


my_parser = argparse.ArgumentParser(description=WELCOME, usage=USAGE)

my_parser.add_argument("-p", "--play",
                       choices=["alphabet_soup", "cross_word"],
                       help="type of game you want to solve")
my_parser.add_argument("-t", "--template",
                       default="stdin",
                       help="name of a template inside game_files folder")
my_parser.add_argument("-c", "--create",
                       help="title for a template defined in the command line")

args = my_parser.parse_args()

n = Game()

if args.play == "alphabet_soup":
    results = n.solve_alphabet_soup(args.template)
    for i in results:
        print(i)

if args.play == "cross_word":
    print("Working on it, cross word will be available soon")

if args.create:
    title = input("Give a title for your game: ")
    if ".txt" not in title:
        title += ".txt"
    game = []
    typing = True
    print("First, enter the wordlist, one word at a time. When you are done, enter a point (.)")
    while typing:
        game.append(input("Enter a word: "))
        if game[-1] == ".":
            typing = False

    print("Now, enter the alphabet soup one line at a time. When you are done, press enter again")
    typing = True
    while typing:
        line = input("Enter a line: ")
        if line == '\n':
            typing = False
        else:
            game.append(line)

    print("Creating game file...")
    with open("../../game_files" + title, "w+") as outfile:
        for item in game:
            outfile.write(item)
    print("Game file created with success in the game_files folder!")
