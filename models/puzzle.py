'''
File:        puzzle.py
Author:      Wessel Poelman
Last change: March 4, 2020
Description:
    This is the main Puzzle class that is used for the game.
    ** add more info later **
'''

import random


class Puzzle:
    '''
    '''

    def __init__(self, pangram, possible_words):
        ''' Assign the initial variables
            ** maybe possible words is created already, otherwise
            we may need a method here to do so **
        '''
        self.pangram = pangram
        self.possible_words = possible_words

        self.letters = list(self.pangram)
        self.random_index = random.randint(0, 6)
        self.main_letter = self.letters[self.random_index]
        self.secondary_letters = self.letters[:self.random_index] + self.letters[self.random_index + 1:]

    def getPangram(self):
        return self.pangram

    def getPossibleWords(self):
        return self.possible_words

    def getMainLetter(self):
        return self.main_letter

    def getSecondaryLetters(self):
        return self.secondary_letters

    def __str__(self):
        '''Returns a string with the pangram'''
        return "Puzzle with pangram: {}".format(self.pangram)
