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

    def __init__(self, pangram):
        ''' Assign the initial variables.

            The pangram needs to be exactly 7 letters long,
            has to have all unique letters and needs to be lower case.
        '''
        self.pangram = pangram.lower()

        self.letters = list(self.pangram)
        self.random_index = random.randint(0, 6)
        self.primary_letter = self.letters[self.random_index]
        self.secondary_letters = self.letters[:self.random_index] + \
            self.letters[self.random_index + 1:]

        self.possible_words = self.__generatePossibleWords()

    def getPangram(self):
        return self.pangram

    def getPossibleWords(self):
        return self.possible_words

    def getPrimaryLetter(self):
        return self.primary_letter

    def getSecondaryLetters(self):
        return self.secondary_letters

    def __generatePossibleWords(self):
        ''' Generates a collection of all possible words that
            can be formed with the given pangram.

            Rules:
                - Words need to be >= 4 characters
                - Words must not contain special characters,
                  numbers, uppercase letters etc.
                  (is responsibility of the word_list).
                - Words must to contain the primary_letter.
                - Words can use all letters
                  (primary and secondary) multiple times
                - The pangram is part of the possible words
        '''

        possible_words = set([self.pangram])

        # use wordlist here + finding possibilities

        return possible_words

    def __str__(self):
        '''Returns a string with the pangram'''
        return "Puzzle with pangram: {}".format(self.pangram)
