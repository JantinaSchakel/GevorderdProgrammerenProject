from models.puzzle import Puzzle


class TestPuzzleCreate:
    def test_adjectives_1(self):
        puzzle_test = Puzzle('opties', ['iets'])
        print(puzzle_test.getPangram())
        print(puzzle_test.getMainLetter())
        print(puzzle_test.getPossibleWords())
        print(puzzle_test.getSecondaryLetters())
        print(puzzle_test)
