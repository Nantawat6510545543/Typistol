from Enemy import Enemy
from random import randrange, choice
import json


class Stage:
    """
    Stage class represented as the main operator that
    controls the game's progress.
    """

    def __init__(self, difficulty=1):
        try:
            with open("word.txt") as data_file:
                self.__all_word = data_file.read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError("word.txt not found")
        self.__word_list = []
        self.__difficulty = difficulty
        self.__score = 0
        self.__enemy = [Enemy(i) for i in
                        range(difficulty - 1, difficulty + 1)]
        self.__elite = randrange(0, 2)

    @property
    def all_word(self):
        return self.__all_word

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def score(self):
        return round(self.__score)

    @property
    def enemy(self):
        return self.__enemy[self.__elite]

    def typist(self):
        """
        Choose some words at random from the word list.
        """
        self.__word_list = []
        max_length = self.difficulty * 2

        while True:
            n = choice(self.__all_word)

            if n not in self.__word_list and len(n) <= max_length:
                self.__word_list.append(str(n))
                if max_length - len(n) <= 0 or len(self.__word_list) == 5:
                    return self.__word_list
                max_length = max(3, max_length - len(n))

    def summon(self):
        """
        Create a list of enemies and randomly increases the difficulty.
        """
        self.__enemy = [Enemy(i) for i in
                        range(self.__difficulty - 1, self.__difficulty + 1)]
        self.__elite = randrange(0, 2)

    def fight(self, attacker, target):
        """
        Inflicts damage to the target
        with a minimum depending on the difficulty.
        """
        target.damage(max(attacker.attack - target.defense, self.__difficulty))

    def next(self, player, time):
        """
        Check if the enemy is alive.
        If an enemy dies, give the player experience and loot,
        then create a new enemy.
        """
        if self.enemy.health <= 0:
            self.__difficulty += 1
            player.leveling(self.enemy.experience_drop)
            self.drop(player)
            self.summon()
            self.__score += max(0, 10 * self.__difficulty - time)
            return True
        return False

    def drop(self, player):
        """
        Random item for player
        """
        if randrange(0, 10000) / 10000 < self.enemy.drop_rate():
            if randrange(0, 100) <= 20:
                buff = randrange(0, 2)
                status = round(self.__difficulty + randrange(-5, 5) / 2)
                if buff == 0:
                    player.get_equipment("HP", status)
                elif buff == 1:
                    player.get_equipment("ATK", status)
                else:
                    player.get_equipment("DEF", status)
            else:
                size = randrange(0, 100)
                if size < 10:
                    player.get_item("L", randrange(1, 2))
                elif size < 50:
                    player.get_item("M", randrange(1, 3))
                else:
                    player.get_item("S", randrange(1, 5))

    def record(self, name, time):
        """
        Record player data
        """
        new_data = {
            name: {
                "score": self.score,
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
