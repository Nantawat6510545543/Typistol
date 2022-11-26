from math import exp, sqrt


class Enemy:
    def __init__(self, name="Enemy", difficulty=1):
        self.__name = name
        self.__difficulty = difficulty
        self.__health = round(difficulty * 1.5)

    @property
    def health(self):
        return self.__health

    @property
    def experience_drop(self):
        return round(self.__difficulty * 1.25)

    @property
    def attack(self):
        return round(self.__difficulty * 1.5)

    @property
    def defense(self):
        return round(self.__difficulty * 1.3)

    @property
    def damage(self):
        return round(self.__difficulty * 1.1)

    def drop_rate(self):
        return 100 * (1 / (1 + exp(-0.02 * self.__difficulty)))

    def __repr__(self):
        return f"Enemy's name : {self.__name}, " \
               f"Difficulty : {self.__difficulty}\n" \
               f"Health : {self.__health}, " \
               f"Attack : {self.attack}, " \
               f"Defense : {self.defense}"
