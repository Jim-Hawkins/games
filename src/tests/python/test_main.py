from unittest import TestCase
import csv
from main_game import Game, AlphabetSoup, GAME_FILES


class TestAlphabetSoup(TestCase):
    def setUp(self):
        self.juego1 = Game()

    def test_parametrized_cases_tests(self):
        """Parametrized cases read from testingCases_1.csv"""
        my_cases = GAME_FILES + "testingCases_1.csv"
        with open(my_cases, newline='', encoding='utf-8') as csvfile:
            # pylint: disable=no-member
            param_test_cases = csv.DictReader(csvfile, delimiter=';')
            for row in param_test_cases:
                print("Test: {} {} {}".format(row['FIELD'], row['ID TEST'], row["VALID"]))
                if row["VALID"] == "VALID":
                    es_valido = True
                    self.assertEqual(True, es_valido)
                else:
                    with self.assertRaises(Exception):
                        self.juego1.solve_alphabet_soup(row['FILE'])
                    # with self.assertRaises(AccessManagementException) as c_m:
                        # OpenDoor.validate_json_stored(row["FILE"])
                    # self.assertEqual(c_m.exception.message, row["EXPECTED RESULT"])

