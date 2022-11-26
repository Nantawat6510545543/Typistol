from Enemy import Enemy
from Player import Player
import random


class Stage:
    def __init__(self):
        with open("word.txt") as data_file:
            self.__all_word = data_file.read().splitlines()
        self.__word_list = []
        self.__difficulty = 1
        self.__score = 0

    def typist(self):
        for i in range(self.__difficulty):
            n = random.choice(self.__all_word)
            self.__word_list.append(n)
            if sum([len(i)/2 for i in self.__word_list]) > self.__difficulty:
                return self.__word_list

    def summon(self):
        return Enemy(f"Enemy difficulty{self.__difficulty}", self.__difficulty)

    def __repr__(self):
        return f"word_list: {self.__word_list}, " \
               f"difficulty : {self.__difficulty}" \
               f"score : {self.__score}, "