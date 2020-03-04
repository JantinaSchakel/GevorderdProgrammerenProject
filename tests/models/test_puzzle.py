from models.puzzle import Puzzle


class TestPuzzleCreate:
    def test_initialization(self):
        # TODO: make this semi random based on the word list
        pangram = 'oertijd'
        possible_words = {'oertijd'}
        # possible_words = {'tijd', 'rijd', 'doet'}
        puzzle = Puzzle(pangram)

        assert puzzle.getPangram() == pangram
        assert puzzle.getPossibleWords() == possible_words
        assert puzzle.getPrimaryLetter() not in puzzle.getSecondaryLetters()
