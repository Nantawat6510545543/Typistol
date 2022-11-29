from Enemy import Enemy
import random
import json


class Stage:
    def __init__(self, difficulty=1):
        with open("word.txt") as data_file:
            self.__all_word = data_file.read().splitlines()
        self.__word_list = []
        self.__difficulty = difficulty
        self.__score = 0
        self.__enemy = Enemy(self.__difficulty)

    @property
    def all_word(self):
        return self.__all_word

    @property
    def word_list(self):
        return self.__word_list

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def score(self):
        return round(self.__score)

    @property
    def enemy(self):
        return self.__enemy

    def typist(self):
        self.__word_list = []
        while True:
            n = random.choice(self.__all_word)
            if n not in self.__word_list and len(n) <= self.difficulty * 2:
                self.__word_list.append(str(n))
            if sum([len(i) for i in self.__word_list]) >= self.__difficulty \
                    or len(self.__word_list) == 4:
                return self.__word_list

    def summon(self):
        self.__enemy = Enemy(self.__difficulty)

    def fight(self, attacker, target):
        target.damage(max(attacker.attack - target.defense, self.__difficulty))

    def next(self, player, time):
        if self.enemy.health <= 0:
            self.__difficulty += 1
            player.leveling(self.enemy.experience_drop)
            self.summon()
            self.__score += 10 * self.__difficulty / time
            return True
        return False

    def record(self, name, time):
        new_data = {
            name: {
                "score": self.__score,
                "time": time
            }
        }
        try:
            with open("record.json", "r") as date_file:
                data = json.load(date_file)
            data.update(new_data)
            with open("record.json", "w") as date_file:
                json.dump(data, date_file, indent=4)
        except FileNotFoundError:
            with open("record.json", "w") as date_file:
                json.dump(new_data, date_file, indent=4)


def __repr__(self):
    return f"word_list: {self.__word_list}, " \
           f"difficulty : {self.__difficulty}, " \
           f"score : {self.__score}\n" \
           f"enemy : {self.__enemy}\n"
